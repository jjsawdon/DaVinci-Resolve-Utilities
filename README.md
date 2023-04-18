# DaVinci Resolve Utilities
 Utilities for DaVinci Resolve

 A collection of Python scripts for DaVinci Resolve

## Scripts

### YouTube Chapter Markers

***Install Instructions***

Make sure you have the Python API set up properly before use. See the included [Python API Setup File](Documents/Python_API_Setup.md) for more information.

**macOS**

Copy `Edit/YouTube Chapters.py` to `~/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts/Edit/`

**Windows**

Copy `Edit\YouTube Chapters.py` to `%APPDATA%\Roaming\Blackmagic Design\DaVinci Resolve\Support\Fusion\Scripts\Edit`

**Linux**

Copy `Edit/YouTube Chapters.py` to `$HOME/.local/share/DaVinciResolve/Fusion/Scripts/Edit`

***Usage***

From Workspace>Scripts (or Workspace>Scripts>Edit), select "YouTube Chapters" to generate a .txt file with YouTube chapter markers to your desktop.

To run this externally, make sure Resolve is running, and run `python3 yt_chapters_external.py` in a terminal/command prompt.

***Known Issues***

* Currently only pulls blue markers
* Does not filter for duration between markers to meet minimum of 10 seconds.

## Documents

A set of documents detailing paths, settings, and advanced workflows

### [Advanced Options](Documents/Advanced_Options.md)

This document lists settings for Advanced Options in System Preferences.

### [Paths](Documents/Paths.md)

This document lists paths for scripts, macros, and system files.

### [Python API Setup](Documents/Python_API_Setup.md)

This document lists setup instructions for using Resolve's Python API