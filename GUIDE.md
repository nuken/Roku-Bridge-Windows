
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
* **Add Channels:** Select provider app fron dropdown (e.g., YTTV or DirecTV) and the specific deep-link Content ID for the channel you want to tune. [Gracenote Finder App](https://nukenlms.com/nuken/ChannelsDvrFinder.zip)
* **Generate the Playlist:** Once your tuners and channels are saved, the bridge will instantly generate an M3U playlist link on the status page.

## 4. Connecting to Channels DVR

* Copy the generated M3U link from the bridge interface.
* Open your Channels DVR web dashboard, navigate to your sources, and add a new **Custom Channel** source.
* Paste the M3U link. Channels DVR will now seamlessly route through the background bridge to tune your Roku and capture the LinkPi stream.

## 5. Partial YTTV Channels with Gracenotes IDs

| Channel Name | Gracenotes ID |
| :---- | :---- |
| Animal Planet  | 57394  |
| BBC America  | 18332  |
| BBC News  | 89542  |
| BET  | 10051  |
| BET Her  | 97358  |
| Bounce  | 55314  |
| ABC News Live  | 113380  |
| ACC Network  | 124806  |
| AMC  | 10021  |
| Bravo  | 10057  |
| Cartoon Network  | 60048  |
| CHARGE\!  | 91578  |
| Cheddar News  | 107241  |
| CMT  | 10138  |
| CNBC  | 10139  |
| CNN  | 10142  |
| Comedy Central  | 64599  |
| Court TV  | 111043  |
| Cozi  | 112981  |
| Dabl  | 112976  |
| Discovery Channel  | 56905  |
| Disney Channel  | 59684  |
| Disney Junior  | 75004  |
| Disney XD  | 60006  |
| ESPN  | 10179  |
| ESPN2  | 12444  |
| ESPNews  | 16485  |
| ESPNU  | 45654  |
| Food Network  | 12574  |
| FOX Business  | 58718  |
| FOX News  | 60179  |
| FOX SOUL  | 119212  |
| FOX Weather  | 123194  |
| Freeform  | 59615  |
| FX  | 14321  |
| FXM  | 14988  |
| FXX  | 17927  |
| Go Channel  | 61854  |
| Hallmark Channel  | 66268  |
| Hallmark Drama  | 105723  |
| Hallmark Movies & Mysteries  | 46710  |
| HGTV  | 49788  |
| HLN  | 64549  |
| HSN  | 62077  |
| ID  | 16615  |
| IFC  | 14873  |
| ION  | 18633  |
| Magnolia Network East  | 18544  |
| MotorTrend  | 111101  |
| MTV  | 10986  |
| MTV2  | 16361  |
| Nat Geo  | 143571  |
| NBA TV  | 32382  |
| NBC News NOW  | 114174  |
| NewsNation  | 91096  |
| NFL Network  | 34710  |
| Nick Jr.  | 105857  |
| OWN  | 70387  |
| Paramount  | 59186  |
| QVC  | 60222  |
| Scripps News  | 96827  |
| SEC Network  | 89714  |
| Smithsonian Channel  | 65799  |
| Start TV  | 109758  |
| SYFY  | 24533  |
| Tastemade  | 107076  |
| TBS  | 11867  |
| USA  | 11208  |
| MTV Classic  | 59054  |
| MSNBC  | 16300  |


