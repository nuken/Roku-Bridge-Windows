
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

## 5. Partial YTTV Channels with Gracenotes IDs and Deeplinks

| Channel Name | Gracenotes ID | Deeplink |
| :---- | :---- | :---- |
| Animal Planet  | 57394  | mw9Me0tRb1o  |
| BBC America  | 18332  | AW1cFldgulo  |
| BBC News  | 89542  | 1GwexN1oIoU  |
| BET  | 10051  | Yg5WWtf94zs  |
| BET Her  | 97358  | V2MqwQ\_yPSg  |
| Bounce  | 55314  | QpasdibYhXs  |
| ABC News Live  | 113380  | aPjdvvXLh0Q  |
| ACC Network  | 124806  | HmB4f8\_5kwE  |
| AMC  | 10021  | TMr6pjcOURI  |
| Bravo  | 10057  | DurE2ZuaaTY  |
| Cartoon Network  | 60048  | kAmvwwpbNu4  |
| CHARGE\!  | 91578  | EGPTfTwk2r4  |
| Cheddar News  | 107241  | Pz2lY8YBMU4  |
| CMT  | 10138  | Ucgh88JpN6o  |
| CNBC  | 10139  | cw87fKrpKUc  |
| CNN  | 10142  | TJSwwtXbvLw  |
| Comedy Central  | 64599  | kJ3ZXGnZJ7w  |
| Court TV  | 111043  | LY-eEqIL4uA  |
| Cozi  | 112981  | MK8aGohCXkE  |
| Dabl  | 112976  | eiozN0vCFtA  |
| Discovery Channel  | 56905  | E60WtflxDlI  |
| Disney Channel  | 59684  | H7VG7o4WMkA  |
| Disney Junior  | 75004  | TAzAjlIZziw  |
| Disney XD  | 60006  | qGIQE6SsblU  |
| ESPN  | 10179  | ferg3lVdMOg  |
| ESPN2  | 12444  | qHoTWZ9M9gw  |
| ESPNews  | 16485  | ReMgHDtmz\_w  |
| ESPNU  | 45654  | 6x-T96Q-5eY  |
| Food Network  | 12574  | yfmTgboH4Cw  |
| FOX Business  | 58718  | dfo8tRrx8Yc  |
| FOX News  | 60179  | SBwjcDPe99c  |
| FOX SOUL  | 119212  | PENBHLpKmkQ  |
| FOX Weather  | 123194  | z\_28T8Abx2Q  |
| Freeform  | 59615  | 80YOERQkKR8  |
| FX  | 14321  | rQHdCIn6MnA  |
| FXM  | 14988  | EG697gmYM30  |
| FXX  | 17927  | hvecVlnuToc  |
| Go Channel  | 61854  | ll39j\_Jw-yM  |
| Hallmark Channel  | 66268  | pAy3YPzYicI  |
| Hallmark Drama  | 105723  | \-ZVgCkR9B5M  |
| Hallmark Movies & Mysteries  | 46710  | yblxP\_RHnxs  |
| HGTV  | 49788  | bUKPbMvjH8k  |
| HLN  | 64549  | xtNZF9VoiZo  |
| HSN  | 62077  | 7jTOZAu4-Dk  |
| ID  | 16615  | BADYkbtoS0s  |
| IFC  | 14873  | bo1k-dRqpno  |
| ION  | 18633  | IOCfIKtSRkY  |
| Magnolia Network East  | 18544  | RhlR8RSAdfQ  |
| MotorTrend  | 111101  | ku9CWpmV0as  |
| MTV  | 10986  | hlbUTBOnqAY  |
| MTV2  | 16361  | X2kCRiHIED8  |
| Nat Geo  | 143571  | Xy4xoelKu\_M  |
| NBA TV  | 32382  | ykTstVbuNpg  |
| NBC News NOW  | 114174  | Nh3k-ZdqSwY  |
| NewsNation  | 91096  | rSrSw8F49RM  |
| NFL Network  | 34710  | mZX19YFSU  |
| Nick Jr.  | 105857  | rCEj4Hmu0KE  |
| OWN  | 70387  | NMpjTBLEMZY  |
| Paramount  | 59186  | szy2hZPK3b8  |
| QVC  | 60222  | xROqZvIHJyE  |
| Scripps News  | 96827  | 7HxFyw2B-x0  |
| SEC Network  | 89714  | LU-XElpC4Zo  |
| Smithsonian Channel  | 65799  | xyYQUFnlBs8  |
| Start TV  | 109758  | IXstJ7HgGf4  |
| SYFY  | 24533  | ibAlErp11ME  |
| Tastemade  | 107076  | pa8\_mj6fH4U  |
| TBS  | 11867  | vv\_r1X6N3sc  |
| USA  | 11208  | ZgiS2N0QkbU  |
| MTV Classic  | 59054  | DEF-HmJXK4M  |

---
