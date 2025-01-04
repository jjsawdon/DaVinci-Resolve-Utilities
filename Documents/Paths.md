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

* macOS: `/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts`

* Windows: `%PROGRAMDATA%\Blackmagic Design\DaVinci Resolve\Fusion\Scripts`

* Linux: `/opt/resolve/Fusion/Scripts`  (or `/home/resolve/Fusion/Scripts/` depending on installation)

### Specific Users

* macOS: `/Users/UserName/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts`

* Windows: `%APPDATA%\Roaming\Blackmagic Design\DaVinci Resolve\Support\Fusion\Scripts`

* Linux: `$HOME/.local/share/DaVinciResolve/Fusion/Scripts`

## Macro Paths

### General Macros

#### Fusion Page in Resolve

* macOS: `Macintosh HD/Users/username/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Macros/`

* Windows: `C:\Users\username\AppData\Roaming\Blackmagic Design\DaVinci Resolve\Support\Fusion\Macros`

* Linux: `home/username/.local/share/DaVinciResolve/Fusion/Macros`

#### Fusion Studio (Standalone)

* macOS: `Macintosh HD/Users/username/Library/Application Support/Blackmagic Design/Fusion/Macros/`

* Windows: `C:\Users\username\AppData\Roaming\Blackmagic Design\Fusion\Macros`

* Linux: `home/username/.fusion/BlackmagicDesign/Fusion/Macros`

### Titles for the Edit Page

* macOS: `Macintosh HD/Users/username/Library/Application Support/Blackmagic Design/ DaVinci Resolve/Fusion/Templates/Edit/Titles`

* Windows: `C:\Users\username\AppData\Roaming\Blackmagic Design\DaVinci Resolve\Support\Fusion\Templates\Edit\Titles`

* Linux: `home/username/.local/share/DaVinciResolve/Fusion/Templates/Edit/Titles`

### Transitions for the Edit Page

* macOS: `Macintosh HD/Users/username/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Templates/Edit/Transitions`

* Windows: `C:\Users\username\AppData\Roaming\Blackmagic Design\DaVinci Resolve\Support\Fusion\Templates\Edit\Transitions`

* Linux: `home/username/.local/share/DaVinciResolve/Fusion/Templates/Edit/Transitions`

### Generators for the Edit Page

* macOS: `Macintosh HD/Users/username/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Templates/Edit/Generators`

* Windows: `C:\Users\username\AppData\Roaming\Blackmagic Design\DaVinci Resolve\Support\Fusion\Templates\Edit\Generators`

* Linux: `home/username/.local/share/DaVinciResolve/Fusion/Templates/Edit/Generators`

## System Paths

These paths are meant as reference for sysadmins or for use in shared environments. If you're not a system administrator or using Resolve on multiple systems in a shared environment, proceed with caution.

### LUTs

Note: in Resolve 17 and later, you can add custom LUT directories in System Preferences.

* macOS (from App Store): `~/Library/Containers/DaVinci Resolve/Data/Library/Application Support/LUT`

* macOS (from BMD): `/Library/Application Support/Blackmagic Design/DaVinci Resolve/LUT/`

* Windows: `C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\LUT\`

* Linux: `/opt/resolve/LUT`

### dblist.conf

dblist.conf is a config file that populates the list of databases (Project Libraries) in the Project Manager on a given system.

* macOS Free (from App Store): `~/Library/Containers/com.blackmagic-design.DaVinciResolveLite/Data/Library/Preferences/dblist.conf`

* macOS Studio (from App Store): `~/Library/Containers/com.blackmagic-design.DaVinciResolve/Data/Library/Preferences/dblist.conf`

* macOS (from Blackmagic Design): `~/Library/Preferences/Blackmagic Design/DaVinci Resolve/dblist.conf`

* Windows: `C:\Users\UserName\AppData\Roaming\Blackmagic Design\DaVinci Resolve\Preferences\dblist.conf`

* Linux: `~/.local/share/DaVinciResolve/configs/.dblist`

### Fusion Studio OFX BlockList

FusionOFX.blocklist will block OFX plugins from loading in Fusion Studio. It's just a path to the ofx.bundle, like this:

`/Library/OFX/Plugins/FilmboxLite.ofx.bundle`

* macOS (only available from Blackmagic Design): `~/Library/Application Support/Blackmagic Design/Fusion/Profiles/Default/FusionOFX.blocklist`

* Windows: `C:\Users\UserName\AppData\Roaming\Blackmagic Design\DaVinci Resolve\Support\Fusion\Profiles\Default`

* Linux: `~/.local/share/DaVinciResolve/Fusion/Profiles/Default/`
