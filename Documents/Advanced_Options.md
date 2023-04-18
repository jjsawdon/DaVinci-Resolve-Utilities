# Advanced Options

These are settings for Advanced Options in System Preferences

## Remote Panels

From `DaVinci Remote Panel.txt`:

On the server system, make sure the panels are correct, then add this line to Advanced Preferences, where IP = IP of the user system.

`Local.Panel.Remote.Address = IP:20323`

On the client system with the panels connected, run these scripts before launching Resolve on the server system:

***Linux:***
* For DaVinci Resolve Advanced Panel - `/opt/resolve/bin/DaVinciRemoteAdvPanel.sh`
* For DaVinci Resolve Micro/Mini Panel - `/opt/resolve/bin/DaVinciRemotePanel.sh`

***Mac:***
* For any DaVinci Resolve Panel - `/Library/Application Support/Blackmagic Design/DaVinci Resolve/DaVinciRemotePanel.app`

***Windows:***
* For DaVinci Resolve Advanced Panel - `%ProgramFiles%\Blackmagic Design\DaVinci Resolve\DaVinciRemoteAdvPanel.bat`
* For DaVinci Resolve Micro/Mini Panel - `%ProgramFiles%\Blackmagic Design\DaVinci Resolve\DaVinciRemotePanel.bat`