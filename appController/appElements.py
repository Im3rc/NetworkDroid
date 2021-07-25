#!/usr/bin/python3

import sys
import subprocess
sys.path.insert(0, '/home/m3rc/Projects/NetworkDroid/adbController')
from adbScripts import *
from xmlCords import *

parent = []
child = []
sub = []
activity = ""
count = 0
currentActivity = ""

def push(stack,data):
	stack.append(data)

def pop(stack):
	if(stack):
		return stack.pop()
	return -1

def parentStackClickable():
	nodes = getCords()
	for node in nodes:
		if(node.getAttribute("clickable") == "true"):
			if(node.getAttribute("resource-id") == "" and node.getAttribute("content-desc") != ""):
				push(parent, node.getAttribute("content-desc"))
			elif(node.getAttribute("content-desc") == "" and node.getAttribute("resource-id") != ""):
				push(parent, node.getAttribute("resource-id"))
			elif(node.getAttribute("content-desc") != "" and node.getAttribute("resource-id") != ""):
				push(parent, node.getAttribute("content-desc"))
	activity = currentActivityIdentifier()
	return(activity)


def processParentClickable(activity):
	print(parent)
	print(packageName not in currentActivityIdentifier())
	while(parent):
		x = pop(parent)
		args = ":id/"
		if args in x:
			executeCords_id(x)
			if(currentActivityIdentifier() == activity):
				goBack()
			elif(packageName not in currentActivityIdentifier()):
				subprocess.Popen("adb shell am start -n com.emanuelef.remote_capture/.activities.MainActivity", stdout=subprocess.PIPE,stderr=subprocess.STDOUT, shell=True)
			else:
				activity = parentStackClickable()
		else:
			executeCords_content(x)
			if(currentActivityIdentifier() == activity):
				goBack()
			elif(packageName not in currentActivityIdentifier()):
				subprocess.Popen("adb shell am start -n com.emanuelef.remote_capture/.activities.MainActivity", stdout=subprocess.PIPE,stderr=subprocess.STDOUT, shell=True)
			else:
				activity = parentStackClickable()


activity  = parentStackClickable()

#TODO
splits = activity.split('/')
packageName = splits[0]
print(packageName)

processParentClickable(activity)

