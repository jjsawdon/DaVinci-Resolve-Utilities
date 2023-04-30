#!/bin/env python3
## IMPORTS ##
import re
import os
import DaVinciResolveScript as bmd
from datetime import datetime

# Settings Dict for Resolve
settings = {
	'perfOptimisedCodec': 'dnxhd_444_12b',
	'perfRenderCacheCodec': 'dnxhd_444_12b',
	'videoCaptureCodec': 'dnxhd_444_12b',
	'perfAutoRenderCacheEnable':'1',
	'perfAutoRenderCacheComposite': '1',
	'perfAutoRenderCacheFuEffect': '1',
	'perfAutoRenderCacheTransition': '1',
	'perfAutoRenderCacheAfterTime': '1',
	'colorLuminanceMixerDefaultZero': '1',
	'timelineOutputResMatchTimelineRes': '0',
	'timelineOutputResolutionHeight': '1080',
	'timelineOutputResolutionWidth': '1920',
	'colorScienceMode': 'davinciYRGBColorManagedv2',
	'timelineInputResMismatchBehavior': 'scaleToCrop',
}

# Define Folder & SubFolder Dict

masterFolders = {
	'timelines': None,
	'utility': None,
	'source': None,
	'ref': None,
	'renders': None
}

tlSubFolders = {
	'submasters': None,
	'fusion': None,
	'compound': None
}

sourceSubFolders = {
	'co': None,
	'audio': None,
	'gfx': None,
	'stock': None,
	'internal_fx': None,
	'vfx': None
}

gfxSubFolders = {
	'ot': None,
	'mt': None,
	'et': None,
	'logos': None
}

# Functions

def add_subfolders(subfolders: dict, masterKey: str) -> dict:
	for k in subfolders:
		subfolder = masterFolders.get(masterKey, mPMaster)
		if subfolder is not None:
			subfolders[k] = mPool.AddSubFolder(subfolder, k)
	return subfolders

# Set Basic Resolve Settings
dvr = bmd.scriptapp("Resolve")
fusion = dvr.Fusion()
projectManager = dvr.GetProjectManager()

# Get database name
database = projectManager.GetCurrentDatabase()
dName = database['DbName']

# Determine from Database Name if it's episodic or feature and set frame rates and template project name accordingly
if re.search(r'_s\d+', dName):
	templateName = dName.rsplit('_', 1)[0] + "_ep_xxx"
	settings['timelineFrameRate'] = '23.976'
	settings['timelinePlaybackFrameRate'] = '23.976'
else:
	templateName = dName + "_rxx"
	settings['timelineFrameRate'] = '24.0'
	settings['timelinePlaybackFrameRate'] = '24.0'

# Create project, open it, and set it as the current object
projectManager.CreateProject(templateName)
projectManager.LoadProject(templateName)
project = projectManager.GetCurrentProject()

# Set project settings as defined in settings dict
for k, v in settings.items():
	project.SetSetting(k, v)

# Get media pool items (can only be done after a project has been created)
mPool = project.GetMediaPool()
mPMaster = mPool.GetRootFolder()

for k in masterFolders:
	masterFolders[k] = mPool.AddSubFolder(mPMaster, k)
tlSubFolders = add_subfolders(tlSubFolders, 'timelines')
sourceSubFolders = add_subfolders(sourceSubFolders, 'source')
for k in gfxSubFolders:
	gfxSubFolder = sourceSubFolders.get('gfx', None)
	if gfxSubFolder is not None:
		gfxSubFolders[k] = mPool.AddSubFolder(gfxSubFolder, k)

# Save and Close the Resolve Project
projectManager.SaveProject()
projectManager.CloseProject(project)
