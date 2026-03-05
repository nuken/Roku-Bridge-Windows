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
| 20/20 | 161600 | 8577d10d-6f28-4021-a475-8b2f5277b709 |
| 50 Cent Action Channel | 178243 | 53aae7e8-b14a-4f7a-b6f0-09d6b465a36c |
| A&E | 51529 | 703b7a51-6290-4d92-6826-c52f4e23519f |
| ABC Localish | 118952 | 2f296390-5b67-48c8-9eff-32d763ae1b05 |
| ABC News Live | 113380 | 98ceb614-f506-4b24-81bd-1d7af542471e |
| ABC-KABC | 19570 | 1d9905ac-4a9c-de63-70e8-9ffb7b13f620 |
| ACC Digital Network | 124806 | 23335f8e-1b24-401a-a0e9-03131827ebf0 |
| AccuWeather | 91994 | dc033f1c-cc4a-adb2-fc2e-9188dc2d36ec |
| Acorn TV Mysteries | 180558 | a0b307a4-c7fa-4b49-bf28-b18b9ea3cef5 |
| Adult Swim | 92425 | db83890f-f06c-4ce8-adf8-5dcaaf75e464 |
| Alien Nation by DUST | 112881 | ec31ae21-6876-da59-e7e9-11aff3deb2c9 |
| All Reality WeTV | 115679 | 195e8347-998c-46df-8073-c3488c89b450 |
| All Women's Sports | 167374 | 302151ca-ec3d-4af0-8fc0-25c20f47428c |
| Always Funny | 134109 | f9501ac5-5f64-4bf7-ba71-93e92d5eedcf |
| AMC | 59337 | 91f974cf-5346-2c4a-47c6-ad3326597a6b |
| American Heroes | 18284 | 61295f1d-b338-1427-befc-e0ec881a9599 |
| America's Funniest Home Videos | 198929 | 86c20454-8d40-42d8-981f-74165c0abc29 |
| America's Got Talent | 189132 | 5ad61225-cf92-4c08-ad84-4203c39d94eb |
| America's Test Kitchen | 115365 | 18b2d611-1f8a-4959-8acc-0fc48a591b2b |
| Anger Management | 125128 | ea4750ec-88c0-2614-6e48-5c7a1e0c4bab |
| Animal Planet | 57394 | 6b8b578e-eaa0-8086-4803-340763f93d36 |
| Are We There Yet | 120377 | d9f37007-5b1d-1b8b-c2da-ca0dacbccf5d |
| ASPIRE | 76126 | 63976b4a-449a-c192-ff84-10c5d0c18fd2 |
| AT HOME with family handyman | 127174 | 228ddde9-918a-2002-c1ae-bc9fd727541c |
| Ax Men | 123425 | 52b935c1-f5da-699a-f12c-ee11c4f965b1 |
| BBC America | 64492 | aade5336-7457-df09-bcfe-7485240a2f8d |
| BBC News | 76774 | 2d96572a-55c8-828a-2430-66f99477d46a |
| Beach Day | 180082 | 69830b96-ff93-4413-9554-5ab0555ec059 |
| beIN SPORTS XTRA | 113143 | 79639ffe-a7f7-4200-8eca-05539c786b33 |
| BET | 63236 | 1c362f35-5526-952d-b892-b1b8492d3d54 |
| Big 12 | 163942 | e850fec6-0fec-4ac0-813e-45a030b1eefe |
| Billiard TV | 120469 | aeb549dd-7657-4b25-9fee-2c036cdc303b |
| Bizarre Foods with Andrew Zimmern | 169593 | 21f2e190-cf1a-43e6-9d58-39c8a976671c |
| Bloomberg TV | 71799 | 862d91ba-d234-e4bc-1caa-79726755fd67 |
| Bob Ross Channel | 114491 | b3d135b1-cf35-2eeb-8348-4ffd98c85f55 |
| BounceTV | 73067 | 19a0169f-323e-b251-99e0-56b7209b4dca |
| Bravo | 58625 | aad256ef-1e09-f926-a05e-2591a809ffff |
| Bravo Vault | 138400 | 678d73a7-6a83-465b-b577-909e0dbe1125 |
| Buzzr | 113452 | affd33fa-627b-43d7-9123-6d80501cc8d1 |
| Car Chase Channel | 182036 | 6185c768-0d60-4ee4-9fe3-bf09ca8f37e4 |
| CBS-KCBS | 19567 | bf371dfd-d753-2555-d682-58fa39264652 |
| Cheddar News | 101103 | 3180919e-9228-678f-baa7-88a09c369a95 |
| Cleo TV | 110289 | abb3ce13-34f9-a681-7a07-ccee20166ee1 |
| CMT | 59440 | 61086ae5-48ce-8085-6d40-1da956771eba |
| CNBC | 58780 | a2ce2e53-bc11-775d-b070-e3c2d4a62d99 |
| CNBC World | 26849 | 5d12e358-4ec1-3905-b5fd-f7fca4700aa6 |
| CNN | 58646 | d3603aea-f5d8-e789-786c-43c5e8799428 |
| CNNi HD East | 83110 | ad9a7dfd-d780-1be2-adf2-a449399254f1 |
| Cold Case Files | 129137 | 30334a98-90b4-dd3e-28ec-fb2c6689ccb2 |
| Comedy Central | 62420 | 853e2bbe-abda-d6b7-26c9-69fbe2d007ef |
| Comedy Dynamics | 115447 | 24efb9da-18f6-4119-63e3-25f7b7a9fb0f |
| Confess by Nosey | 151953 | 47a34fd7-50f1-4c7f-9cb2-70b251049ef2 |
| Cooking Channel | 68065 | dcccb5d2-a567-e7a7-a1a2-c12d4b83c0c8 |
| Cosmic Frontiers | 135380 | 5ac49b16-917a-49fc-98db-4da3dacb32be |
| Court TV | 123605 | fca7a1e2-cbb5-dd08-7dbd-4198fabef15d |
| Cozi TV | 89994 | 9fd00aad-1cc7-cf23-ba3e-bae853bd6165 |
| Crime 360 | 113780 | 5aa81392-22af-431b-3379-20654730f148 |
| Crime Scenes | 138028 | 41f8d9f1-5210-429d-a594-f905c61c59bc |
| C-SPAN | 10161 | c167f6c4-9128-4043-d798-50a8df3f29de |
| C-SPAN2 | 10162 | 49943603-c8bb-1a02-9621-15c8e95ecf7c |
| C-SPAN3 | 68332 | eae4c8fa-0c66-4b8a-9608-344ff4337d4d |
| Curiosity Now | 123667 | fbba6327-6393-4ddf-89b1-8d3a647406e2 |
| CUT | 178858 | 6233c872-0a33-46cc-a579-bb369f1f2d8b |
| Dance Moms by Lifetime | 126369 | 6ff68577-ae85-4554-99f2-c4fe5c950ab0 |
| Danger TV | 120204 | 61115cfa-4c6d-4c79-90d7-e62e7052c93b |
| Dateline 24/7 | 113957 | 09b070d4-1d26-454d-a7a1-be9cd80ad7e4 |
| DAZN Ringside | 144738 | 0d005767-4d77-4074-9fdb-879405e916a5 |
| Deal Zone | 123432 | 351adaee-7e8b-d0bc-4ff6-e4fdea86464f |
| Declassified | 130514 | f86e2408-155f-4f8e-8ee3-911cbd44a824 |
| Destination America HD | 60468 | d5ad3ec8-623a-b0ae-9335-a2d09fbc850c |
| Discovery | 56905 | 1755a18d-4cf4-8440-8f4a-bd73849cd9d6 |
| Discovery Life | 16125 | 2c3c77b4-8941-7de6-291c-a33ad50f6504 |
| Documentary+ | 129672 | e4b94113-a7bd-4ce8-80e2-199ad7a4c0d8 |
| Dog Whisperer | 147688 | 763575a1-3a58-bee6-4857-83152247068c |
| Dove TV | 110480 | ca52a885-706a-aa11-d31e-52dbfa61ba54 |
| DraftKings | 138277 | 6cf48a68-9b16-41c7-b912-f158b7b3897b |
| Drool | 160302 | e3cf52b0-1667-46f7-8f0d-2366742810ea |
| Duck Dynasty | 131429 | 5677757f-7d33-342e-4f8a-c565414e2cae |
| E! | 61812 | b4bd8603-8a28-c738-450b-b43807610760 |
| E! Keeping Up | 138393 | 34dc8bc4-d8fb-4db4-ac49-96d0e0bcc21d |
| Earth Touch | 159242 | 35c6ab1d-7a0e-45b6-ac2f-4b1432ead2ae |
| EarthX | 126128 | 76c132b0-fa3f-ac34-bc39-b0fecdc68e49 |
| Ebony TV | 146144 | bd572399-bf07-7b4e-39f5-92b97ba92ecc |
| El Rey Rebel | 124328 | 8bdb5846-80f2-3a63-7417-4ce193c45964 |
| ESPN8: The Ocho | 161567 | d2fe50c4-73f0-415b-942a-1f7979cd5966 |
| Fail Army | 121204 | f9a3cac9-385b-e100-25f2-381fb599ea0f |
| Family Entertainment Television | 73413 | 3ef9f466-918c-40c8-a141-280f8d15f623 |
| Family Feud (Steve Harvey) | 125192 | 8405f3bb-a303-4137-a475-c888e5eb83b2 |
| Family Movie Classics | 127501 | 57b6cb4b-1a42-2381-901c-16a2813c6492 |
| Fight Network | 123170 | 6eba1d55-1d1a-41e7-a4f7-cf68e18f111a |
| Food Network | 50747 | 7822f08f-c09d-d890-2b46-948766f9f571 |
| Fox Business Network | 58718 | b0129946-46f3-f80f-42ea-315f64eeaac0 |
| Fox News Channel | 60179 | 5f3323ab-7390-8fcc-177f-bf9cc8000bcf |
| FOX Soul | 119212 | 8d634c15-ddbf-8231-1912-9ac32ab4a62b |
| Fox Sports | 141469 | 155d2ce8-256f-4f0c-a725-b0465c135dab |
| FOX Weather | 93141 | ecd16979-bf5c-6f24-2575-11788b27f387 |
| FOX-KTTV | 20450 | d431bbbe-f58f-5cce-56b1-6bcb51a1fc5e |
| Freeform HD | 121949 | d3046aab-71b5-2d44-1b53-fcab4c9d7cad |
| Fuel TV | 116115 | 8a481e27-81a5-ae7d-a069-895a331fab88 |
| FX | 58574 | f1281894-b977-5b3a-596d-5cf3b1b176ca |
| FX Movie Channel | 14988 | a56d1955-3f16-b9d1-a531-89755221ccf2 |
| FXX | 66379 | 79dfae40-37b1-adf0-d95b-97c72f792a02 |
| FYI | 58988 | 2238cd22-7e7a-89d3-d219-aea6b94d292f |
| GET | 82563 | 23f0fc84-d285-c4a1-a4c9-dfb383ed77db |
| Ghosts are Real | 138030 | f0e1d116-981b-4ff8-8f17-35359bfb2c5f |
| GolfPass | 114142 | 52b8799b-58ad-4e57-bc91-348c8449a088 |
| GoTraveler | 124225 | d2b40a56-a108-4bb2-8cda-28ae08ad0718 |
| Great American Family | 82892 | eaf8f979-a1ee-40e1-9162-77dc4873c9a4 |
| Great American Romcoms | 129134 | c2c70e40-45c4-4dc2-9cbd-4fb0534ae275 |
| GRIT | 89922 | 3097b4cc-3b54-14e3-c801-796f2316040f |
| GSN HD | 68827 | dd504770-d338-5864-8d11-e0ae78330990 |
| Gusto TV | 111140 | a4b4a389-42c8-4be6-8d01-31f6c4f318e0 |
| Hallmark Channel | 66268 | a2236f35-6af2-3c7f-bf9d-979acaec1251 |
| Hallmark Family | 105723 | a19bb823-2d6a-925b-6e8a-d94f3610813b |
| Hallmark Mystery | 46710 | d120a585-8155-4df6-b294-2808d6e3f640 |
| Heroes & Icons | 120460 | 3e228444-bc03-2b53-fe94-311f35388702 |
| HerSphere | 135378 | 36a7cbf5-53bc-8dd0-7bd2-1e83efc3353a |
| HGTV | 49788 | deaa46a3-836f-58f3-f897-73a42289a940 |
| HISTORY | 57708 | 3d2a7de5-af2e-b845-da1c-17d51e5f156a |
| History & Warfare | 135379 | 30d05dca-fbe8-436f-9000-558e2176f42e |
| HLN | 64549 | 6d1f5d8a-9616-b2aa-fd67-190f5f108591 |
| Horror by Alter | 124998 | da8a95fd-dbce-2b8c-85af-df62756536f7 |
| How To | 138031 | 7ebdc1da-4f7a-4759-8d5c-ecd88fce57bf |
| I (Almost) Got Away With It | 154436 | 901c06ce-8674-4cb0-8647-3f4dc9592cfb |
| i24 News | 102309 | e259b90c-9d27-43d5-b0ab-2d2771a9948a |
| Ice Road Truckers | 123426 | 94ad1f48-8f6b-e7f8-fe76-d59a9f70aefd |
| IFC | 59444 | 156dda5e-4d82-707a-ee92-cd9fd017f425 |
| INFAST | 118699 | 39917eff-a7da-623e-55bc-9808e95a0aaf |
| INSP HD | 82773 | 175ff6e3-db6f-1f74-327a-ac998f93b987 |
| INSP Western Bound | 127279 | cc4d03e3-5f72-41f4-9e99-5897edd5ee05 |
| Investigation Discovery | 65342 | 29ef0716-ed45-4e47-5185-d4384199b291 |
| INWONDER | 129477 | 7fdaa256-b9f3-49a3-b6a9-7d346ee1211f |
| ION East | 76894 | a6740f2c-81c8-f263-90ea-ac83df064f10 |
| Jamie Oliver | 176039 | 77d041f6-bb8a-4003-8699-a25831c47d83 |
| Joel Osteen | 156961 | d5b3d5aa-e900-4d74-b531-38271e916999 |
| Let's Make a Deal | 163434 | 346adee2-5fd6-4f45-ade6-a48a75436b70 |
| Lifetime | 60150 | bab3ef03-eeac-b5b1-a157-1a98bf4fbbde |
| Lifetime Movie Network | 55887 | 3d967c45-3b9b-f223-db5f-b4d7ef756744 |
| Lionsgate Collection | 190287 | 71941139-7289-4189-889c-85ac86dc1101 |
| Living With Evil | 170382 | 64400029-c7b5-4c86-bbd2-136da48192d4 |
| Love After Lockup | 185538 | 15895412-93f2-4b54-b2e4-67c757f11e54 |
| Love Kills | 170369 | 258d73b5-e7b5-42df-92d8-a0f6b1794e5e |
| Love Nature | 157909 | 608db494-74ae-63bb-7b98-fff85bd1f6c3 |
| MagellanTV Wildest | 119209 | 82a0350e-5ee8-48fb-a0ec-a77a627b1267 |
| Magnolia Network | 67375 | 25ad7277-733d-16f9-965d-6e80308a64fa |
| MeatEater | 149441 | c0c13c65-6794-c180-d49c-191d4d4b29b2 |
| MeTV | 122696 | 83321f4e-2ac2-9dc4-a1fd-7b0a0f8c1e5f |
| Military Heroes | 126439 | 7bec5559-8a6f-41c2-a20e-ebc6f08ce253 |
| Million Dollar Listing Vault | 164081 | 2b1500c5-1699-4c48-ba15-e9ebb7c18b3b |
| Modern Marvels | 123433 | a6c3900f-1c46-a1de-8a73-d7f0156dc1d7 |
| Movie Favorites by Lifetime | 121308 | eb4161d4-79a0-23c6-8b4a-98101491311a |
| MovieSphere | 158131 | f5f22b85-28be-1fee-3eaa-3ff3afa2bfb9 |
| MS Now | 64241 | 6ea83d29-e16f-7ab5-397e-6efb32bbcba9 |
| MTV | 60964 | 9ec54b53-8d07-7efc-99a7-349057b95eed |
| MTV2 | 75077 | 721ab65b-5333-8c23-4a03-3fff869176c9 |
| Mysterious Worlds | 138032 | a35cfee1-834d-49cb-b0be-2872430dc6b7 |
| Mythbusters | 180083 | 19b4c411-ff39-4a5d-96cd-1a131d468aad |
| Nat Geo WILD | 67331 | 219e6ef1-a7d1-b89d-fbb8-f190e7832bd2 |
| National Geographic Channel | 49438 | 2b76c29e-325d-a699-9a6c-99bbe6a7c765 |
| NBA FAST Channel | 196933 | c5ce58ef-2f58-4a51-868f-b908f9f88d9d |
| NBC News Now | 114174 | b768a920-2942-4655-b869-e5912808deaa |
| NBC Sports Now | 114140 | 677221c4-6ef5-4df9-be7a-3eae6d497307 |
| NBC-KNBC | 19568 | f5bbe264-e39e-9b2e-a490-560be72e07e4 |
| Newsmax TV | 97163 | 533f3fad-e91d-5cbf-6f80-82db799e4953 |
| Nosey | 133657 | 62e8a5e0-2c60-2c74-1856-9aa1cb32948b |
| Ovation HD | 69061 | 334adfc3-a627-41bd-7724-f313e9101697 |
| OWN | 70388 | c88d76e7-6a4c-435c-65f2-5ea6c63a3c9e |
| Oxygen True Crime | 70522 | a7ee26db-54eb-601b-b8df-1a67ad0cff4d |
| Oxygen True Crime Archives | 138585 | cb5990f8-d329-455a-8aa6-79e08501a8b6 |
| Paramount TV | 59186 | 6924fc10-8306-4009-6495-714764f0dbf6 |
| Pickleball TV | 146769 | 8b13aaf2-eddd-4a22-9b09-8a600c811ea2 |
| Players TV | 116748 | 62f051e8-c6d6-b689-e952-27644a8019af |
| PokerGo | 124268 | 915a988d-f06e-12c8-7ef3-1fa8bede454d |
| POP HD | 68796 | d7f25adf-9813-5570-bdaa-83d1aef41777 |
| Portlandia | 122435 | b9a568c2-5ec8-4250-b937-bb80c6a0400e |
| PowerNation | 123515 | 30ab6d01-34fb-e35f-48af-b36707d9cb40 |
| Pureflix TV | 149039 | b1a6d17c-8ea1-4fd9-b538-7b073f564c70 |
| Pursuit UP | 112487 | 956541c0-e5b1-4b0e-8ff1-7c33be71f191 |
| Racing America | 124630 | e9fa4976-45fa-fcea-da4c-a2becc56ea07 |
| Real Housewives Vault | 138455 | 17a13fad-b5ab-4ddb-86c9-b07afce38f65 |
| Red Bull TV | 142279 | 7553c225-8868-43d3-8874-90cafa0cc371 |
| Rig TV | 160864 | 40e4accf-9058-44fe-b9e8-52c33e067617 |
| RVTV | 164367 | 18f466e0-e3e7-4431-970f-a2bf7cc0176a |
| Ryz Sports | 173352 | 9cfc5708-8ca3-4a8f-be66-1da3642a0af8 |
| Say Yes To The Dress | 149117 | 003c9e88-d38a-4523-9f5d-e21f32d6f614 |
| Science | 57390 | c6874cea-e0ae-8bda-80b4-a347b0e09a43 |
| Scripps News | 120010 | d9afeb8d-ed9e-af47-36b0-c7f993e64a47 |
| Shorts TV HD | 67454 | 24c133b3-ae88-b1b2-efdb-357127a9d1d7 |
| Smithsonian Channel HD | 58532 | 1653bae3-dad0-8d4f-7524-8090a1a46e86 |
| SNL Vault | 113678 | 86032e2f-ed1f-4f2f-85a1-4447e5ec7878 |
| Somos Novelas | 158862 | 65f85519-70ad-12bc-85fe-17893c41ea17 |
| Sony Movies HD | 69130 | 61160753-1873-9662-f8cf-3aea8f6e4239 |
| Speedvision | 132889 | e3dba27a-cac1-4b73-b977-c6078e24a172 |
| Sports Illustrated | 132647 | 79e6dffd-ff8f-41fc-8f00-16843bc588d5 |
| SportsGrid | 120919 | 5d74452d-3569-4c5f-52a5-70aec559f007 |
| Stadium Stream | 113991 | 637fad42-44b3-4f64-b4e1-d623bf26447f |
| Stories by AMC | 130687 | 37966f8a-aba0-4bb0-88bd-bd6caa967208 |
| Sundance TV | 71280 | d94cb013-806e-43f9-c316-31ed9073b3d3 |
| Supermarket Sweep | 121598 | 1353cabb-992d-4aa6-9a0a-856c48854154 |
| Surf Cinema | 152976 | 69aadc5e-4f13-4bf1-bcfb-3a663c38f07b |
| Sweet Escapes | 138027 | a69d935f-a0b5-4d14-80f5-51574911b96e |
| Swerve Combat | 122436 | bd98ceac-7e30-44d5-8c49-cc391646408a |
| Syfy | 58623 | 148e9301-574b-e202-9f1d-5eaac40731ac |
| Tastemade | 107076 | 6a0016fd-74ec-7d3e-973f-da042697284d |
| Tastemade Home | 125187 | 900ddb32-a2e9-fa38-327f-266af6b3ca8b |
| Tastemade Travel | 121718 | 6e6081ac-415e-1e3e-5b0b-939ff4558368 |
| TCM | 64312 | cca34ba0-ffc4-bcdd-16d1-20469ae2f1c9 |
| Tennis Channel 2 | 137752 | 995a6592-b8d3-4331-aa7c-8236c5cfe7d4 |
| The Design Network | 118087 | 35703c79-93c8-a679-8282-ff6f0822d1d7 |
| The First | 114934 | 4bdf80f2-d09d-45d5-b98a-86da258f373e |
| The Jim Rome Show | 162473 | a8c44e05-c444-492d-bc15-6eb67833e4f0 |
| The Masked Singer | 191048 | ff300b51-5b71-4aa5-b48d-3b01a5166a9a |
| The Pet Collective | 121165 | 6a699b8f-3d82-d8ce-eeb4-44bf4d4e3dd5 |
| The Price is Right: Drew Carey | 163435 | 2bc76122-8ab3-46d9-9cd3-3b7688f5b67c |
| The Price is Right: The Barker Era | 175935 | faa38971-dd49-4a9d-a927-fb088d7ef42a |
| The Walking Dead Universe | 115540 | 456688d4-45d0-40cf-9763-614959b1224d |
| Three Stooges | 170345 | 4d6daef4-63f8-404f-b60a-849e4ff19a23 |
| Tiny House Nation | 118456 | 5f7a1a3f-5bf9-54b5-eda8-7d6aee1d7e5c |
| TLC | 57391 | 88bbbc54-9107-45ec-26b0-a79707a87bb2 |
| TNA | 121991 | bc4aa7db-ed8a-493b-8d28-0971951d3c3c |
| Today All Day | 114138 | b4e5ec5e-8479-4514-89c4-85fac278a1ec |
| Torque by History | 123423 | d79e6e89-1c63-43c6-a868-f1b384571bf6 |
| Total Crime | 131220 | fdf99f1f-69b4-45d3-b532-a08f38def5f5 |
| Travel Channel | 59303 | d1fd34a4-4dcc-dd0d-6310-6c25aabf20ff |
| Tribeca Festival+ | 183204 | b06de443-3a27-4d68-ae1d-3b602fef48b4 |
| True Crime Now | 135383 | a9222905-2b40-4c4c-bc5e-21e685d6ae26 |
| TV Land | 73541 | b24b7b6f-c840-e216-e73c-7d32d9eecbda |
| UnXplained Zone | 123431 | e273fbe5-4fb6-1a98-b5d2-2ff67c957f89 |
| UP | 44940 | ce75e450-1ad3-1794-1b74-351de95ea6ad |
| VH1 | 60046 | f4d9239f-9378-1beb-9ab3-23c07a0b1473 |
| VICE | 65732 | 5d43cf2a-99f7-f804-499b-4409953e578d |
| Waypoint TV | 121424 | ebd517c3-0c17-498d-a0a4-19f0ab9fba2a |
| WE TV | 59296 | af87404f-791a-a30f-c3f9-484abfce0452 |
| Willow Sports | 164602 | d6e6da4f-2239-4ebb-b120-9c1d2d37d646 |
| WIRED2fish TV | 132644 | 0b515061-de43-40f4-91eb-28d02e4a4119 |
| Women's Sports Network | 124636 | e2e20701-db3f-88af-8847-375ce73ad2b8 |
| Yahoo Finance | 113674 | adbf117c-1d63-eac6-eaf8-52ac94284631 |
| Yu-Gi-Oh! | 155772 | f0b0a1cc-5257-4401-8dcd-75f00678b420 |
---
