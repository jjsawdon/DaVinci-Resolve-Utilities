# Resolve Paths

This document contains paths for macros, scripts, and some system-level files in DaVinci Resolve.

## Script Paths

Scripts can go into two main directories: one for all users, and one for specific users.

Within those directories, you can put scripts into different directories that correspond to different pages. All scripts will appear under `Workspace>Scripts` regardless of which page you're on; however, if you're not on a specific page, they'll appear under the corresponding folder title; i.e. on the Color page, scripts in the Edit folder will appear in the Edit submenu.

* `Comp` will appear in the Fusion page
* `Edit` will appear in the Edit page
* `Color` will appear in the Color page
* `Deliver` will appear in the script menu under Advanced Settings and will not appear under `Workspace>Scripts`
* `Utility` will appear on all pages

Scripts will not work in the Mac App Store version of Resolve.

### All Users

macOS:

`/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts`

Windows:

`%PROGRAMDATA%\Blackmagic Design\DaVinci Resolve\Fusion\Scripts`

Linux:
`/opt/resolve/Fusion/Scripts`  (or `/home/resolve/Fusion/Scripts/` depending on installation)

### Specific Users

macOS:

`/Users/UserName/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts`

Windows:

`%APPDATA%\Roaming\Blackmagic Design\DaVinci Resolve\Support\Fusion\Scripts`

Linux:
`$HOME/.local/share/DaVinciResolve/Fusion/Scripts`

## Macro Paths

## System Paths

These paths are meant as reference for sysadmins or for use in shared environments. If you're not a system administrator or using Resolve on multiple systems in a shared environment, proceed with caution.

### dblist.conf

dblist.conf is a config file that populates the list of databases (Project Libraries) in the Project Manager on a given system.

***macOS***

**App Store**

`~/Library/Containers/com.blackmagic-design.DaVinciResolveLite/Data/Library/Preferences/dblist.conf`

`~/Library/Containers/com.blackmagic-design.DaVinciResolve/Data/Library/Preferences/dblist.conf`

**From BMD**

`~/Library/Preferences/Blackmagic Design/DaVinci Resolve/dblist.conf`

***Windows***

`C:\Users\UserName\AppData\Roaming\Blackmagic Design\DaVinci Resolve\Preferences\dblist.conf`

***Linux***

`~/.local/share/DaVinciResolve/configs/.dblist`