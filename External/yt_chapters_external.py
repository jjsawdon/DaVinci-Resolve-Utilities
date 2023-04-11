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

# Filter Markers
filtered_dict = {k:v for k,v in markers.items() if v['color'] == 'Blue'}
formatted_dict = {f'{int(k//(framerate*3600)):02d}:{int(((k//framerate)%60))%60:02d}:{int((k//framerate)//60):02d}:{str(int(k%60)).zfill(2)}.{int((k%1)*framerate):02d}' if isinstance(framerate, float) else f'{int(k//(framerate*3600)):02d}:{int(((k//framerate)%60))%60:02d}:{int((k//framerate)//60):02d}:{str(int(k%60)).zfill(2)}.{int(framerate):02d}':v for k,v in filtered_dict.items()}


with open(writePath, 'w') as f:
	for k,v in formatted_dict.items():
		f.write(f'Chapter: {v["name"]}, Start Time: {k}\n')