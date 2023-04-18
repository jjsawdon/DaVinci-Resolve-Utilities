#!/bin/env python
## IMPORTS ##
import os
import DaVinciResolveScript as bmd
from pathlib import Path

# Set Basic Resolve Settings
dvr = bmd.scriptapp("Resolve")
fusion = dvr.Fusion()
projectManager = dvr.GetProjectManager()
project = projectManager.GetCurrentProject()
timeline = project.GetCurrentTimeline()

# Get Info From Resolve
framerate = timeline.GetSetting('timelineFrameRate')
markers = timeline.GetMarkers()
timelineName = timeline.GetName()

# Set File Path
chapterList = (timelineName + '.txt')
desktopPath = os.path.join(str(Path.home()), 'Desktop')
writePath = os.path.join(desktopPath, chapterList)

# Make sure 0 is a marker; if not, add it
if 0 not in markers:
	markers[0] = {'color': 'Blue', 'duration': 1, 'note': '', 'name': 'Start', 'customData': ''}
# Check Marker Count
if len(markers.keys()) < 3:
	with open(writePath, 'w') as f:
		f.write('Not enough chapters! Minimum of 3 chapters required!\nAdd an additional marker and try again.\n')
else:
	# Sort, Filter and Format Markers
	sorted_markers = {k: markers[k] for k in sorted(markers)}
	filtered_dict = {k:v for k,v in sorted_markers.items() if v['color'] == 'Blue'}
	formatted_dict = {}
	for k, v in filtered_dict.items():
	    seconds = int(k / framerate)
	    minutes = int(seconds / 60)
	    seconds = seconds % 60
	    formatted_time = f'{minutes:02d}:{seconds:02d}'
	    formatted_dict[formatted_time] = v
	# Write to the file
	with open(writePath, 'w') as f:
		for k,v in formatted_dict.items():
			f.write(f'{k} {v["name"]}\n')