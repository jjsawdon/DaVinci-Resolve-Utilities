#!/bin/env python
## IMPORTS ##
import DaVinciResolveScript as dvr
from datetime import datetime

# Set Basic Resolve Settings
dvr = bmd.scriptapp("Resolve")
fusion = dvr.Fusion()
projectManager = dvr.GetProjectManager()
projects = projectManager.GetProjectListInCurrentFolder()

#Loop through projects
for p in projects:
	# Load Project
	project = projectManager.LoadProject(p)
	# Log to Console
	print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' - disabling auto cache settings for project: ' + project.GetName())
	# Set Settings
	project.SetSetting('perfAutoRenderCacheEnable', '0')
	project.SetSetting('perfAutoRenderCacheComposite', '0')
	project.SetSetting('perfAutoRenderCacheFuEffect', '0')
	project.SetSetting('perfAutoRenderCacheTransition', '0')
	# Save Project
	projectManager.SaveProject()
	# Log to Console
	print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' - done with ' + project.GetName())
	# Close Project and continue
	projectManager.CloseProject(project)