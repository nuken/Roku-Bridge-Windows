# Roku Bridge (Windows Edition)

A lightweight, native Windows background service that acts as a proxy bridge between raw LinkPi Transport Streams and Channels DVR. It dynamically assigns local network ports and issues Roku External Control Protocol (ECP) commands to automate live TV tuning for HDMI encoders.

This version has been completely rewritten to run natively on Windows without requiring Docker or Linux environments. 

##  Features
* **Zero Dependencies:** Runs entirely natively on Windows. No Python installation, Docker, or WSL required for the end user.
* **Auto-Configuration:** Automatically discovers the host machine's local IP address and scans for an open port (starting at 5006) to prevent conflicts with other services.
* **Waitress Multi-Threaded Engine:** Handles raw `.ts` video streaming efficiently in the background without locking up the UI.
* **Automated Firewall Management:** The installer automatically configures Windows Defender Firewall to allow local network streaming.
* **Auto-Start:** Installs directly to the Windows Startup folder so your streams are always ready when your PC boots.
* **Built-in Web Player:** Preview your LinkPi streams directly in the browser using `mpegts.js`.

##  Installation (For Users)

1. Navigate to the **[Releases](../../releases)** tab on the right side of this repository.
2. Download the latest `RokuBridge_Setup_vX.X.X.exe`.
3. Double-click the installer. 
4. The setup wizard will automatically install the application, add the necessary firewall exceptions, and create a shortcut.
5. Once installed, the application will silently launch in the background and automatically open the configuration interface in your default web browser.

##  Configuration & Usage

When the application launches for the first time, it will generate a `roku_channels.json` file in your user `AppData\Local\RokuBridge` folder to safely store your settings.

1. Use the web interface to add your **LinkPi Encoder URL** and your **Roku IP Address**.
2. Add your desired channels (including the Deep Link Content ID and Roku App ID).
3. Copy the generated M3U playlist link from the status page.
4. Paste the M3U link into your **Channels DVR** custom source settings. 

Channels DVR will now seamlessly tune your Roku and capture the LinkPi stream whenever you select a channel.

##  Building from Source (For Developers)

This project uses `PyInstaller` and `Inno Setup` to compile the Python scripts into a standalone Windows installer.

### Prerequisites:
* Python 3.10+
* [Inno Setup 6](https://jrsoftware.org/isinfo.php)

### Local Build Instructions:
1. Clone the repository to your Windows machine.
2. Double-click the `build.bat` script. This will automatically create a Python virtual environment, install the requirements, and use PyInstaller to compile `app.py` into a standalone `RokuBridge.exe` inside the `\dist` folder.
3. Once compiled, right-click the `setup.iss` file and select **Compile** using Inno Setup. 
4. The final, distributable Windows Setup Wizard will be generated in the `\Output` folder.

### CI/CD Pipeline
This repository contains a GitHub Actions workflow (`.github/workflows/build-unsigned.yml`) that automatically compiles the Waitress server and generates the Inno Setup executable in the cloud. 

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

