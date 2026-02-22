[Setup]
; Basic App Info
AppName=Roku Bridge
AppVersion=5.0.1
AppPublisher=nuken
DefaultDirName={autopf}\RokuBridge
DisableProgramGroupPage=yes
; The icon for the installer itself
SetupIconFile=icon.ico
; Where the final setup.exe will be saved
OutputDir=Output
OutputBaseFilename=RokuBridge_Setup_v5.0.1
Compression=lzma
SolidCompression=yes
; Require admin rights to add firewall rules
PrivilegesRequired=admin

[Files]
; Grab the compiled app and the icon
Source: "dist\RokuBridge.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "icon.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
; Create Desktop and Start Menu shortcuts
Name: "{autodesktop}\Roku Bridge"; Filename: "{app}\RokuBridge.exe"; IconFilename: "{app}\icon.ico"
Name: "{autoprograms}\Roku Bridge"; Filename: "{app}\RokuBridge.exe"; IconFilename: "{app}\icon.ico"
; Auto-start the app silently in the background when Windows boots
Name: "{commonstartup}\Roku Bridge"; Filename: "{app}\RokuBridge.exe"; IconFilename: "{app}\icon.ico"

[Run]
; 1. Add Windows Defender Firewall exception silently so the M3U works immediately
Filename: "{sys}\netsh.exe"; Parameters: "advfirewall firewall add rule name=""Roku Bridge"" dir=in action=allow program=""{app}\RokuBridge.exe"" enable=yes"; Flags: runhidden
; 2. Launch the app immediately after installation finishes
Filename: "{app}\RokuBridge.exe"; Description: "Launch Roku Bridge Now"; Flags: nowait postinstall skipifsilent

[UninstallRun]
; Clean up the firewall rule if the user uninstalls the app
Filename: "{sys}\netsh.exe"; Parameters: "advfirewall firewall delete rule name=""Roku Bridge"" program=""{app}\RokuBridge.exe"""; Flags: runhidden; RunOnceId: "RemoveFirewallRule"