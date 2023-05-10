#!/bin/env python
## IMPORTS ##
import os
#import DaVinciResolveScript as bmd

def GetAllFolders(folderList):
	for f in folderList:
		folderList.extend(f.GetSubFolderList())
	return list(set(folderList))

def GetAllMediaItems(folderList):
	for f in folderList:
		mediaList.extend(f.GetClipList())
	return list(set(mediaList))

# Set Basic Resolve Settings
dvr = bmd.scriptapp("Resolve")
fusion = dvr.Fusion()
projectManager = dvr.GetProjectManager()
project = projectManager.GetCurrentProject()
mediaPool = project.GetMediaPool()
rootFolder = mediaPool.GetRootFolder()
folderList = rootFolder.GetSubFolderList()

folderList = GetAllFolders(folderList)

if folderList:
	folderList.insert(0, rootFolder)
else:
	folderList.insert(0, rootFolder)
print("Gathered "+str(len(folderList))+" bin(s)")
mediaList = []
mediaList = GetAllMediaItems(folderList)
for m in mediaList[:]:
	if m.GetClipProperty('Type') not in ['Video + Audio', 'Video']:
		mediaList.remove(m)
print("Gathered "+str(len(mediaList))+" media item(s)")
for m in mediaList:
	m.UnlinkProxyMedia()
print("Done!")