# Roku Bridge (Windows Edition) - User Guide

## Table of Contents
* [1. Preparing Your Roku Device](#1-preparing-your-roku-device)
* [2. Installing the Application](#2-installing-the-application)
* [3. Configuring Tuners and Channels](#3-configuring-tuners-and-channels)
* [4. Connecting to Channels DVR](#4-connecting-to-channels-dvr)
* [5. Partial YTTV Channels with Gracenotes IDs and Deeplinks](#5-partial-yttv-channels-with-gracenotes-ids-and-deeplinks)
* [6. Partial DirecTv Channels with Gracenotes IDs and Deeplinks](#6-partial-directv-channels-with-gracenotes-ids-and-deeplinks)

---

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

## 6. Partial DirecTv Channels with Gracenotes IDs and Deeplinks

| Channel Name | Gracenotes ID | Deeplink |
| --- | --- | --- |
| NBC-WTMJ | 25020 | a43c615d-ce14-fb04-1ccc-6f0e87de3bcc |
| FOX-WITI | 30924 | 63846e66-2f3d-56d8-9bd2-a819daf182ca |
| PBS-WMVS | 19633 | 6f9c68ae-cb51-9cc1-f2ea-560b2828b457 |
| ABC-WISN | 32367 | 652caee6-6aa6-b4aa-49ba-584a6a1298b1 |
| CW-WVTV | 35541 | 7ce2fcc2-cfbd-a78e-3455-1b66b3dfb6e8 |
| MyNet-WVTV-D2 | 89743 | 24f1a3f7-644d-4082-ac29-c58effa7ad19 |
| CBS-WDJT | 30192 | a6ec2f4f-5f44-ff82-72d1-fc88aa331ef9 |
| MeTV | 122696 | 83321f4e-2ac2-9dc4-a1fd-7b0a0f8c1e5f |
| Cozi TV | 89994 | 9fd00aad-1cc7-cf23-ba3e-bae853bd6165 |
| GRIT | 89922 | 3097b4cc-3b54-14e3-c801-796f2316040f |
| BounceTV | 73067 | 19a0169f-323e-b251-99e0-56b7209b4dca |
| GET | 132748 | 23f0fc84-d285-c4a1-a4c9-dfb383ed77db |
| CNNHD | 58646 | d3603aea-f5d8-e789-786c-43c5e8799428 |
| HLN | 10145 | 6d1f5d8a-9616-b2aa-fd67-190f5f108591 |
| ESPN HD | 32645 | dede9246-d012-a0b5-3a0d-47e1dab9aad8 |
| ESPNEWS | 16485 | 12a35cc1-19d8-d1c1-1fac-4ca6b264dbed |
| ESPNU HD | 60696 | 9ecd95cc-35c3-6edf-f374-ba56a30479c0 |
| ESPN2 HD | 45507 | 86803936-4000-2af7-19e9-81ba8fa148d8 |
| NFL Red Zone | 89351 | 16118543-23f0-cd3a-bb5b-3c97438c34f5 |
| NFL Network | 45399 | b7effab4-2677-a11a-6505-d5e1ef60f465 |
| MLB Network | 62081 | a65b11b9-e803-3bc8-1efc-49c5dd66d689 |
| MLB Network Alternate | 62085 | 7c04b18e-9534-d6a4-dbd8-790561ee75a6 |
| NHL Network HD | 58690 | f70c4f77-652e-bfc0-6f4d-65f32fc3f2ba |
| NBA TV | 45526 | d340c4c5-abad-9bc1-6dbc-3cd499b796a7 |
| Tennis Channel HD | 60316 | f0d90008-caa2-97c8-93c3-7ff6a575486f |
| Golf Channel | 61854 | 2dd56923-6e9f-b6ef-a3d6-d6c0c5aa6ab0 |
| FOX Sports 1 | 82547 | 5c55c82f-c5cb-2aa5-6376-cc868d5cdc32 |
| CBS Sports Network HD | 59250 | 143250f9-2f97-19ea-1070-b1b64a7589be |
| Shop LC | 56032 | c697423f-24ae-9691-cf3e-b0753f8ad23a |
| HGTV | 14902 | deaa46a3-836f-58f3-f897-73a42289a940 |
| Magnolia Network | 67375 | 25ad7277-733d-16f9-965d-6e80308a64fa |
| Food Network | 12574 | 7822f08f-c09d-d890-2b46-948766f9f571 |
| Cooking Channel | 68065 | dcccb5d2-a567-e7a7-a1a2-c12d4b83c0c8 |
| GSN HD | 68827 | dd504770-d338-5864-8d11-e0ae78330990 |
| Tastemade | 107076 | 6a0016fd-74ec-7d3e-973f-da042697284d |
| E HD | 61812 | b4bd8603-8a28-c738-450b-b43807610760 |
| Bravo | 58625 | aad256ef-1e09-f926-a05e-2591a809ffff |
| ReelzChannel HD | 68385 | c3fbdc9f-44b7-76e3-23e9-cde81c5b3117 |
| Sundance TV | 71280 | d94cb013-806e-43f9-c316-31ed9073b3d3 |
| HSN HD | 62077 | b26807c7-7513-c72e-261c-6270efc1cad4 |
| Paramount TV | 59186 | 6924fc10-8306-4009-6495-714764f0dbf6 |
| USA Network | 58452 | 28bbbe87-9c3b-5da7-4ad4-9868916b173d |
| Syfy HD | 58623 | 148e9301-574b-e202-9f1d-5eaac40731ac |
| TNT HD | 42642 | acf51074-6940-81d8-2355-c2eb610e0afc |
| truTV HD | 64490 | e7971467-59df-3be6-5711-8b9f72b70787 |
| TBS HD | 58515 | ded1f9a7-a3e2-503d-7129-3e31e5257fae |
| FX HD | 58574 | f1281894-b977-5b3a-596d-5cf3b1b176ca |
| Comedy Central | 62420 | 853e2bbe-abda-d6b7-26c9-69fbe2d007ef |
| Oxygen True Crime | 70522 | a7ee26db-54eb-601b-b8df-1a67ad0cff4d |
| Lifetime | 60150 | bab3ef03-eeac-b5b1-a157-1a98bf4fbbde |
| LMN HD | 55887 | 3d967c45-3b9b-f223-db5f-b4d7ef756744 |
| AMC HD | 59337 | 91f974cf-5346-2c4a-47c6-ad3326597a6b |
| TCM HD | 64312 | cca34ba0-ffc4-bcdd-16d1-20469ae2f1c9 |
| FX Movie Channel | 70253 | a56d1955-3f16-b9d1-a531-89755221ccf2 |
| FXX HD | 66379 | 79dfae40-37b1-adf0-d95b-97c72f792a02 |
| WE TV | 59296 | af87404f-791a-a30f-c3f9-484abfce0452 |
| Discovery Life | 16125 | 2c3c77b4-8941-7de6-291c-a33ad50f6504 |
| BBC America | 64492 | aade5336-7457-df09-bcfe-7485240a2f8d |
| A&E HD | 51529 | 703b7a51-6290-4d92-6826-c52f4e23519f |
| FYI HD | 58988 | 2238cd22-7e7a-89d3-d219-aea6b94d292f |
| EarthxTV | 126128 | 76c132b0-fa3f-ac34-bc39-b0fecdc68e49 |
| HISTORY | 57708 | 3d2a7de5-af2e-b845-da1c-17d51e5f156a |
| VICE HD | 65732 | 5d43cf2a-99f7-f804-499b-4409953e578d |
| LOGO HD | 46762 | cdb44de7-e993-8772-28fb-1158b49137aa |
| POP HD | 68796 | d7f25adf-9813-5570-bdaa-83d1aef41777 |
| Ovation HD | 69061 | 334adfc3-a627-41bd-7724-f313e9101697 |
| QVC HD | 60222 | 15d2ac39-3429-e4c3-eafa-9bd6f477344d |
| National Geographic Channel | 49438 | 2b76c29e-325d-a699-9a6c-99bbe6a7c765 |
| Travel Channel | 59303 | d1fd34a4-4dcc-dd0d-6310-6c25aabf20ff |
| DSC HD | 56905 | 1755a18d-4cf4-8440-8f4a-bd73849cd9d6 |
| OWN HD | 70388 | c88d76e7-6a4c-435c-65f2-5ea6c63a3c9e |
| TLC HD | 57391 | 88bbbc54-9107-45ec-26b0-a79707a87bb2 |
| MotorTrend | 31046 | 649c0044-750a-d41a-9d3d-55229567a62f |
| Animal Planet | 57394 | 6b8b578e-eaa0-8086-4803-340763f93d36 |
| Nat Geo WILD | 67331 | 219e6ef1-a7d1-b89d-fbb8-f190e7832bd2 |
| Science | 57390 | c6874cea-e0ae-8bda-80b4-a347b0e09a43 |
| Investigation Discovery | 65342 | 29ef0716-ed45-4e47-5185-d4384199b291 |
| Destination America HD | 60468 | d5ad3ec8-623a-b0ae-9335-a2d09fbc850c |
| American Heroes | 78808 | 61295f1d-b338-1427-befc-e0ec881a9599 |
| Disney Junior HD | 74885 | 74b13512-5e2c-8c70-15d0-d1c8b9fda9b2 |
| Disney Channel HD | 59684 | 22f13b87-4c9d-9674-f01d-328925c190e9 |
| Disney XD HD | 60006 | d5b8d53c-1409-d612-3436-d7bccebc4e04 |
| Baby First HD | 50338 | dc98eaf2-8e61-8222-e2a3-54dcb9e3d08a |
| Discovery Family Channel | 67749 | 524c81fb-5d82-3ad0-c1e2-d8434692cf6b |
| Universal Kids | 70225 | d41f94b9-92a0-5134-1de2-88672cb415c5 |
| Cartoon Network | 60048 | 2336facb-8e11-c83b-b49f-4e54682104e3 |
| BOOM | 21883 | e331455c-dfa0-7d05-2b47-2d22768394b9 |
| Nickelodeon | 59432 | ed9654e0-a239-473b-2654-f45e655b183c |
| Nick Jr. HD | 82649 | e1468b46-28cd-bb84-4d8c-fa9b86fa6d6b |
| Nicktoons | 30420 | 2e8de275-8a57-a07e-2748-45df074e06da |
| TeenNick | 59036 | dacae6da-950d-bc52-9e77-a120799ca097 |
| TV Land | 73541 | b24b7b6f-c840-e216-e73c-7d32d9eecbda |
| ION | 76894 | a6740f2c-81c8-f263-90ea-ac83df064f10 |
| NewsNation | 91096 | 870c91a5-e875-37f0-3c4f-d1b41ec6b831 |
| Freeform HD | 59615 | d3046aab-71b5-2d44-1b53-fcab4c9d7cad |
| Hallmark Channel | 66268 | a2236f35-6af2-3c7f-bf9d-979acaec1251 |
| Jewelry TV | 16604 | 7886d5c2-2559-9822-f009-3c72a2f6fb69 |
| Family Movie Classics | 122068 | 57b6cb4b-1a42-2381-901c-16a2813c6492 |
| QVC2 | 82682 | 2f0bc776-8b8f-d6a5-2123-a9c940121c63 |
| QVC3 | 101260 | f02bab27-3ac4-7e0c-7e6d-624804fb7c06 |
| Scientology Network | 102490 | 5fe9e66f-bdb4-dbb1-ace0-504734ce970c |
| FETV | 73413 | 3ef9f466-918c-40c8-a141-280f8d15f623 |
| Great American Family | 82892 | eaf8f979-a1ee-40e1-9162-77dc4873c9a4 |
| CMT | 10138 | 61086ae5-48ce-8085-6d40-1da956771eba |
| TV One | 61960 | 95d012f3-9276-a155-be33-96d29a3bf2e5 |
| BET HD | 63236 | 1c362f35-5526-952d-b892-b1b8492d3d54 |
| BHER | 14897 | 2cb67cc0-5cbd-c28e-5cb3-efd2c063ab05 |
| MTV HD | 60964 | 9ec54b53-8d07-7efc-99a7-349057b95eed |
| MTV2 HD | 75077 | 721ab65b-5333-8c23-4a03-3fff869176c9 |
| IFC HD | 59444 | 156dda5e-4d82-707a-ee92-cd9fd017f425 |
| VH1 HD | 60046 | f4d9239f-9378-1beb-9ab3-23c07a0b1473 |
| MTVClassic | 22561 | 2f3603ca-cc66-e8b0-b2da-7c88d527c969 |
| UPTV | 44940 | ce75e450-1ad3-1794-1b74-351de95ea6ad |
| Fuse HD | 59116 | 5ba91416-92dc-84ab-73fb-c7e10f4620e3 |
| AXSTV | 28506 | d0c3c9df-90af-6f4a-5ad0-ab0e0d646dd5 |
| Cleo TV | 110289 | abb3ce13-34f9-a681-7a07-ccee20166ee1 |
| theGrio | 132272 | bdc5570f-ff4d-776f-157d-cf398c4d0853 |
| RFD-TV | 63717 | 8653742c-ddfd-32d3-e9c9-8c3489892ff6 |
| BBC News | 89690 | 2d96572a-55c8-828a-2430-66f99477d46a |
| The First | 114934 | 4bdf80f2-d09d-45d5-b98a-86da258f373e |
| Newsmax TV | 97163 | 533f3fad-e91d-5cbf-6f80-82db799e4953 |
| C-SPAN | 10161 | c167f6c4-9128-4043-d798-50a8df3f29de |
| C-SPAN2 | 10162 | 49943603-c8bb-1a02-9621-15c8e95ecf7c |
| Bloomberg TV | 71799 | 862d91ba-d234-e4bc-1caa-79726755fd67 |
| Cheddar News | 109333 | 3180919e-9228-678f-baa7-88a09c369a95 |
| CNBC HD | 58780 | a2ce2e53-bc11-775d-b070-e3c2d4a62d99 |
| MSNBC | 64241 | 6ea83d29-e16f-7ab5-397e-6efb32bbcba9 |
| CNBC World | 26849 | 5d12e358-4ec1-3905-b5fd-f7fca4700aa6 |
| CNNi HD | 10146 | ad9a7dfd-d780-1be2-adf2-a449399254f1 |
| Fox Business Network | 58718 | b0129946-46f3-f80f-42ea-315f64eeaac0 |
| Fox News Channel | 60179 | 5f3323ab-7390-8fcc-177f-bf9cc8000bcf |
| AccuWeather | 91994 | dc033f1c-cc4a-adb2-fc2e-9188dc2d36ec |
| The Weather Channel HD | 58812 | 171bd2ee-b0d3-da59-a26a-231e199a438c |
| FOXWX | 93141 | ecd16979-bf5c-6f24-2575-11788b27f387 |
| INSPHD | 82773 | 175ff6e3-db6f-1f74-327a-ac998f93b987 |
| Daystar HD | 87001 | 6ee7980c-e134-7e7a-7bd0-ddc88fb558cb |
| Aspire HD | 97409 | 63976b4a-449a-c192-ff84-10c5d0c18fd2 |
| Comedy TV | 82470 | ca96e2f7-a27a-f202-cb2d-31975539c9e3 |
| Justice Central HD | 78850 | cf7d17e0-f70e-9775-73a4-bd109035b169 |
| Revolt HD | 83098 | 541dd341-6a6d-19e4-58cf-b1d6469c4c05 |
| Heroes & Icons | 110477 | 3e228444-bc03-2b53-fe94-311f35388702 |
| FM HD | 72094 | 953bc9f7-4dc5-93b4-8052-2a3ba1cfe4af |
| RECIPE | 71294 | 74271fce-8ac1-6eed-e9ab-3a25833e0f85 |
| Univision | 68049 | 91e8d5f2-ef1b-d3c5-17e7-cb3da2da015b |
| Galavision | 68367 | f2cc0b38-5662-8586-4358-4e6746e76bb2 |
| UniMas | 68040 | 3b2dc438-4244-ecf9-a2f6-f967c524712c |
| UNIVERSO | 91588 | d51f7b37-e63c-5d6d-3222-c237108f1d28 |
| TUDN HD | 77033 | 4e32e1d2-6ed0-e6fb-b3a0-f4c409ee7799 |
| STARZ ENCORE East | 36225 | b9ddc1ac-7daf-5f96-9817-5c2c142bfbb7 |
| STARZ ENCORE West | 17125 | 97d47e36-15d9-6ea9-596b-de55223b9689 |
| STARZ ENCORE Classic | 14764 | 18b2939c-782e-e13d-e764-297f9edd0238 |
| STARZ ENCORE Westerns | 102906 | 7a0cf3c9-df1a-d67f-2cfd-c31c23d42773 |
| STARZ ENCORE Suspense | 14766 | 71fa3714-c586-f978-bc41-a9abbf696c7a |
| STARZ ENCORE Black | 14870 | 5c48e0e5-2d7d-e713-9165-5dcb43014173 |
| STARZ ENCORE Action | 72015 | d2d065bf-aac0-7ed9-bdc5-35a713bccca8 |
| STARZ ENCORE Family | 102903 | 1dd535f5-7229-7230-2ae5-44f0b5da59d9 |
| HFM | 105723 | a19bb823-2d6a-925b-6e8a-d94f3610813b |
| Hallmark Mystery | 46710 | d120a585-8155-4df6-b294-2808d6e3f640 |
| HDNM | 33668 | 427146c7-ba72-f092-5c39-a973864c1429 |
| Smithsonian Channel HD | 58532 | 1653bae3-dad0-8d4f-7524-8090a1a46e86 |
| CIHD | 61621 | e9009898-3c52-499b-ccaf-d02581e11039 |
| Shorts TV HD | 67454 | 24c133b3-ae88-b1b2-efdb-357127a9d1d7 |
| FanDuel TV | 21345 | cbad9aaa-dacc-3f9a-e799-5cbd192a6744 |
| Pursuit Channel | 60111 | aefee661-f332-a0e1-9232-17775d8eb624 |
| Sportsman Channel | 33930 | c0e8a1c8-61fb-6d94-7023-bd57672fea7a |
| BIG10HD | 49466 | 6e59cfb6-e9cf-f265-1fc3-d8fb0085b829 |
| SEC Network | 89714 | 59806c1a-3da5-504b-ad47-fd7c44397445 |
| ACC Network | 111871 | a39b5a6b-fcba-4d31-53be-12190003e171 |
| FOX Sports 2 | 59305 | 996701b2-525f-4b9e-ba56-222e80ff45ac |
| Next Level Sports HD | 8981 | 3b0c3d09-1b7f-eb8e-cc5a-451bafbfc1b5 |
| Willow HD | 3291 | 9d3706a3-90cb-f05d-4791-ea4013d5e994 |
| Willow Xtra | 3292 | 28ae8df2-4955-4e64-e9dd-6dbf9ee2a9e2 |
| NESN | 10996 | 31f3edfb-3e42-f36e-4ac4-e6399f1d11d6 |
| NBC Sports Boston | 11104 | 654cd6e9-85c7-aae8-ca96-d3a8e0e39950 |
| YES Network | 30017 | 7ec4c3a9-52a4-fc75-7ae3-4c5cc56cc9e8 |
| MSG | 80169 | d8e66c4b-8fd7-b378-eeec-237da090517d |
| MSG Sportsnet | 70285 | 99c9bc89-9aa5-6a4a-e5b8-f0b6437c9393 |
| SportsNet New York | 49603 | 14d4252a-b378-278a-f51a-c30eb2df9427 |
| MASN | 46817 | 4561b79f-8d5d-82cc-4229-d28b27b4d0c3 |
| Monumental Sports Network | 10271 | 4876f881-1191-93f6-a860-d511ce3fa6ab |
| Bally Sports South | 75057 | 6b1b1fd0-f99e-21a3-3c9b-4e203159542d |
| Bally Sports Southeast | 89889 | a4d30cc4-b643-f450-edeb-780912f11235 |
| Bally Sports Sun | 96010 | c2cb18d4-8522-98ed-5ed7-e82dbe72b713 |
| Bally Sports Florida | 102053 | 54991b93-7c1e-3469-f8bd-8143a3614564 |
| SportsNet Pittsburgh | 26028 | fdc8df0a-27b2-af5c-794f-83c2e5b9ef26 |
| Bally Sports Ohio | 11106 | 3328cf65-3f83-e0a9-c434-88598604efad |
| Bally Sports Great Lakes | 50167 | 54376de0-5f07-7a27-8aba-b537ad9181d6 |
| Bally Sports Detroit | 96250 | 5c3de28e-b0f5-2318-d1f5-b9b5dbeece65 |
| Marquee Sports Network | 116034 | d33b3eb7-916a-43b5-ea7c-1c0f246f2032 |
| NBC Sports Chicago | 65369 | 2a4e8565-4ba2-5608-9915-604ac84ce45f |
| Bally Sports North | 10977 | 3bf48966-a192-91e3-9acb-e272aad57d20 |
| Bally Sports Wisconsin | 16348 | ea121788-f35d-2f61-89e9-7c0bf55483a0 |
| Bally Sports Midwest | 69825 | 7886070f-db0c-eb9c-6d5f-52d1e7fc1e91 |
| Space City Home Network | 77744 | 43a6c1eb-9080-1c82-84d3-c54e2a96e907 |
| Bally Sports Southwest | 108428 | e343d71b-402e-134e-e085-73b8a3d83343 |
| Altitude Sports | 44263 | 9c72b3a5-c4ec-de97-c2ac-9d5f5 |
---
