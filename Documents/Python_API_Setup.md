# Python API Setup

This is a shortened summary of the setup required for the Python API, documented in the API README.txt found by going to Help>Developer>Documentation.

## Environment Variables

***Mac OS X***
* RESOLVE_SCRIPT_API="/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting"
* RESOLVE_SCRIPT_LIB="/Applications/DaVinci Resolve/DaVinci Resolve.app/Contents/Libraries/Fusion/fusionscript.so"
* PYTHONPATH="$PYTHONPATH:$RESOLVE_SCRIPT_API/Modules/"

***Windows***
* RESOLVE_SCRIPT_API="%PROGRAMDATA%\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting"
* RESOLVE_SCRIPT_LIB="C:\Program Files\Blackmagic Design\DaVinci Resolve\fusionscript.dll"
* PYTHONPATH="%PYTHONPATH%;%RESOLVE_SCRIPT_API%\Modules\"

***Linux***
* RESOLVE_SCRIPT_API="/opt/resolve/Developer/Scripting"
* RESOLVE_SCRIPT_LIB="/opt/resolve/libs/Fusion/fusionscript.so"
* PYTHONPATH="$PYTHONPATH:$RESOLVE_SCRIPT_API/Modules/"
(Note: For standard ISO Linux installations, the path above may need to be modified to refer to /home/resolve instead of /opt/resolve)

### Setting Environment Variables

***macOS/Linux***

In a Terminal window, run `export NAME=VALUE`.

For example, on macOS:

`export RESOLVE_SCRIPT_API="/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting"`

And on Linux:

`export RESOLVE_SCRIPT_API="/opt/resolve/Developer/Scripting`

***Windows***

