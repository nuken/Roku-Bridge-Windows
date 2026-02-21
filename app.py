import os
import sys
import json
import time
import socket
import logging
import threading
import webbrowser
import requests
from flask import Flask, request, Response, render_template, jsonify
from waitress import serve

# ==========================================
# 1. PyInstaller MEIPASS & Path Configuration
# ==========================================
# When PyInstaller compiles an .exe, it extracts static files to a hidden temp folder.
# We must explicitly tell Flask to look there, otherwise it crashes looking for status.html.
if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
    
    # We want to save the user's config file in the folder where the .exe actually lives,
    # NOT in the temporary MEIPASS folder which gets deleted when the app closes.
    base_dir = os.path.dirname(sys.executable)
else:
    app = Flask(__name__)
    base_dir = os.getcwd()

app_data_dir = os.path.join(os.getenv('LOCALAPPDATA', base_dir), 'RokuBridge')
os.makedirs(app_data_dir, exist_ok=True)
CONFIG_FILE = os.path.join(app_data_dir, 'roku_channels.json')

# ==========================================
# 2. Global Variables & Setup
# ==========================================
TUNERS = []
CHANNELS = []
APP_PORT = 5006
APP_VERSION = "5.0.0-LEAN-WIN"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
roku_session = requests.Session()

# ==========================================
# 3. Network Discovery Functions
# ==========================================
def get_lan_ip():
    """Forces the OS to reveal its primary local network IP address."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(('8.8.8.8', 80))
            return s.getsockname()[0]
    except Exception:
        return '127.0.0.1'

def find_available_port(starting_port=5006):
    """Scans for an open port starting at 5006 to prevent conflicts."""
    port = starting_port
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('127.0.0.1', port)) != 0:
                return port
        port += 1

# ==========================================
# 4. Configuration Management
# ==========================================
def load_config():
    global TUNERS, CHANNELS, APP_PORT
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            data = json.load(f)
            TUNERS = data.get('tuners', [])
            CHANNELS = data.get('channels', [])
            APP_PORT = data.get('app_port', 5006)
    else:
        # First Run: Find a safe port and generate a default config file
        APP_PORT = find_available_port()
        save_config_to_disk()

def save_config_to_disk():
    with open(CONFIG_FILE, 'w') as f:
        json.dump({"app_port": APP_PORT, "tuners": TUNERS, "channels": CHANNELS}, f, indent=2)

# ==========================================
# 5. Core Proxy & Tuning Logic
# ==========================================
def execute_fast_tune(roku_ip, channel_data):
    """Uses the ECP Launch endpoint for instantaneous deep-linking."""
    content_id = channel_data.get('deep_link_content_id')
    app_id = channel_data.get('roku_app_id')

    if content_id and app_id:
        url = f"http://{roku_ip}:8060/launch/{app_id}?contentId={content_id}&mediaType=live"
        try:
            logging.info(f"Tuning {roku_ip} to app {app_id} with content {content_id}")
            roku_session.post(url, timeout=2)
            time.sleep(channel_data.get("tune_delay", 3))
        except Exception as e:
            logging.error(f"Tuning failed on {roku_ip}: {e}")

@app.route('/stream/<channel_id>')
def proxy_stream(channel_id):
    """Proxies the raw TS bytes from the LinkPi to the client (Channels DVR/Browser)."""
    channel_data = next((c for c in CHANNELS if c['id'] == channel_id), None)
    if not channel_data:
        return "Channel Not Found", 404

    # Simplified round-robin tuner selection for the Lean build
    tuner = TUNERS[0] if TUNERS else None
    if not tuner:
        return "No Tuners Available", 503

    # Fire the deep-link command on a background thread so the proxy can start buffering
    threading.Thread(target=execute_fast_tune, args=(tuner['roku_ip'], channel_data)).start()

    def generate():
        try:
            with requests.get(tuner['encoder_url'], stream=True, timeout=5) as r:
                r.raise_for_status()
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        yield chunk
        except Exception as e:
            logging.error(f"Proxy stream failed: {e}")

    return Response(generate(), mimetype='video/mp2t')

# ==========================================
# 6. Web UI & M3U Generator
# ==========================================
@app.route('/status')
def status_page():
    # Pass settings so the UI can display the correct version
    global_settings = {"app_version": APP_VERSION}
    return render_template('status.html', global_settings=global_settings)

@app.route('/api/config', methods=['GET', 'POST'])
def api_config():
    global TUNERS, CHANNELS
    if request.method == 'POST':
        data = request.json
        TUNERS = data.get('tuners', [])
        CHANNELS = data.get('channels', [])
        save_config_to_disk()
        return jsonify({"status": "success"})
    return jsonify({"tuners": TUNERS, "channels": CHANNELS, "app_port": APP_PORT})

@app.route('/channels.m3u')
def generate_m3u():
    """Generates the Channels DVR playlist using the true LAN IP."""
    requested_playlist = request.args.get('playlist')
    lan_ip = get_lan_ip()
    host_url = f"{lan_ip}:{APP_PORT}"
    
    m3u_content = [f"#EXTM3U x-tvh-max-streams={len(TUNERS)}"]
    for channel in CHANNELS:
        if requested_playlist and channel.get('playlist') != requested_playlist:
            continue
            
        stream_url = f"http://{host_url}/stream/{channel['id']}"
        extinf = f'#EXTINF:-1 channel-id="{channel["id"]}" tvc-guide-stationid="{channel.get("gracenote_id", "")}"'

        if 'playlist' in channel and channel['playlist']:
            extinf += f' group-title="{channel["playlist"]}"'

        extinf += f',{channel["name"]}'
        m3u_content.extend([extinf, stream_url])

    return Response("\n".join(m3u_content), mimetype='audio/x-mpegurl')
    
@app.route('/preview/<channel_id>')
def preview_stream(channel_id):
    """Renders an embedded web player to preview the raw TS stream."""
    channel_data = next((c for c in CHANNELS if c['id'] == channel_id), None)
    if not channel_data:
        return "Channel Not Found", 404

    stream_url = f"http://{request.host}/stream/{channel_id}"
    
    # We serve an inline HTML page with mpegts.js to decode the raw TS stream in the browser
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Preview - {channel_data['name']}</title>
        <script src="https://cdn.jsdelivr.net/npm/mpegts.js@1.7.3/dist/mpegts.min.js"></script>
        <style>
            body {{ background: #1a1a1a; color: white; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; margin: 0; font-family: sans-serif; }}
            video {{ width: 80%; max-width: 1280px; border: 2px solid #404040; border-radius: 8px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }}
            a {{ color: #7dd3fc; text-decoration: none; margin-top: 20px; font-size: 1.2em; }}
        </style>
    </head>
    <body>
        <h2>Previewing: {channel_data['name']}</h2>
        <video id="videoElement" controls autoplay muted></video>
        <a href="/status"><i class="fa-solid fa-arrow-left"></i> Back to Status</a>
        
        <script>
            if (mpegts.getFeatureList().mseLivePlayback) {{
                var videoElement = document.getElementById('videoElement');
                var player = mpegts.createPlayer({{
                    type: 'mse',
                    isLive: true,
                    url: '{stream_url}'
                }});
                player.attachMediaElement(videoElement);
                player.load();
                player.play();
            }} else {{
                alert("Your browser does not support TS stream playback.");
            }}
        </script>
    </body>
    </html>
    """
    return html_content

# ==========================================
# 7. Remote Control Endpoints
# ==========================================
@app.route('/remote')
def remote_page():
    return render_template('remote.html')
    
@app.route('/remote/devices', methods=['GET'])
def get_remote_devices():
    """Feeds the saved Roku tuners to the remote control dropdown menu."""
    return jsonify(TUNERS)

@app.route('/api/remote/keypress', methods=['POST'])
def handle_keypress():
    data = request.json
    key = data.get('key')
    tuner_ip = data.get('tuner_ip')
    if key and tuner_ip:
        try:
            url = f"http://{tuner_ip}:8060/keypress/{key}"
            requests.post(url, timeout=1)
            return jsonify({"status": "success"})
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500
    return jsonify({"status": "error"}), 400
    
@app.route('/api/tuners', methods=['GET'])
def get_tuners():
    """Provides the remote control UI with the list of available tuners."""
    return jsonify({"tuners": TUNERS})

@app.route('/api/status_data', methods=['GET'])
def api_status_data():
    """Provides general status data if the frontend expects it."""
    return jsonify({"tuners": TUNERS, "channels": CHANNELS})

# ==========================================
# 8. Waitress Server & Auto-Launch
# ==========================================
if __name__ == '__main__':
    # 1. Load config and claim our port
    load_config()
    lan_ip = get_lan_ip()
    
    # 2. Fire up the browser automatically
    def open_browser():
        time.sleep(1.5) # Give the server a second to boot
        target_url = f"http://{lan_ip}:{APP_PORT}/status"
        logging.info(f"Opening browser to {target_url}")
        webbrowser.open(target_url)
        
    threading.Thread(target=open_browser, daemon=True).start()
    
    # 3. Start the Windows-native WSGI server
    # threads=32 ensures video previews won't lock up the UI
    logging.info(f"Starting Waitress Server v{APP_VERSION} on port {APP_PORT}...")
    serve(app, host='0.0.0.0', port=APP_PORT, threads=32)