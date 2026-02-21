
# Roku Bridge (Windows Edition) - User Guide

## 1. Preparing Your Roku Device

Before the bridge can automate your channel surfing, your Roku must be configured to accept network commands.

* **Find Your Roku's IP Address:** On your Roku remote, press the **Home** button, then navigate to **Settings > Network > About**. Note the IP Address.
* **Enable Control by Mobile Apps:** This is critical. On your Roku, navigate to **Settings > System > Advanced system settings > Control by mobile apps** and ensure "Network access" is set to **Default** or **Permissive**.

## 2. Installing the Application

This lightweight Windows version is completely standalone and requires no Docker, Python, or Linux environments.

* Download the latest `RokuBridge_Setup.exe` file from the Releases page.
* Run the installer. The setup wizard will automatically configure the necessary Windows Defender Firewall exceptions to allow seamless local network streaming.
* It will also install a background shortcut so the bridge automatically starts whenever Windows boots.
* Once installation finishes, the background server will launch silently, and the configuration interface will pop open in your default web browser.

## 3. Configuring Tuners and Channels

All of your settings are safely generated and stored in your local Windows `AppData` folder.

* **Add a Tuner:** In the web interface, enter your LinkPi Encoder URL and the Roku IP Address you found in Step 1.
* **Add Channels:** Enter the target application's App ID (e.g., use `140474` for DirecTV) and the specific deep-link Content ID for the channel you want to tune.
* **Generate the Playlist:** Once your tuners and channels are saved, the bridge will instantly generate an M3U playlist link on the status page.

## 4. Connecting to Channels DVR

* Copy the generated M3U link from the bridge interface.
* Open your Channels DVR web dashboard, navigate to your sources, and add a new **Custom Channel** source.
* Paste the M3U link. Channels DVR will now seamlessly route through the background bridge to tune your Roku and capture the LinkPi stream.
