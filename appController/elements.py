#!/usr/bin/python3

import subprocess
from xml.dom import minidom
import sys
sys.path.insert(0, '/home/m3rc/Projects/NetworkDroid/adbController')
from adbScripts import *

count = 1 
def findClickable():
	xml_data = ""
	processed_output = activityXmlDump()
	for i in processed_output:
		if(i[0:5] == "<?xml"):
			xml_data = i
# 	Get current activity name
	processed_output = currentActivityList()
	s = processed_output[0].split(' ')
	currentActivity = s[-2]
	nodes = minidom.parseString(xml_data).getElementsByTagName("node")
	for node in nodes:
		if(node.getAttribute("clickable") == "true"):
			if(node.getAttribute("resource-id") == "" and node.getAttribute("content-desc") != ""):
				push(node.getAttribute("content-desc"))
			elif(node.getAttribute("content-desc") == "" and node.getAttribute("resource-id") != ""):
				push(node.getAttribute("resource-id"))
			elif(node.getAttribute("content-desc") != "" and node.getAttribute("resource-id") != ""):
				push(node.getAttribute("content-desc"))
			else:
				push("Error")
	mapper[count] = currentActivity 
	updateParentLayout(count)

def push(data):
	parentStack.append(data)

def pop(data):
	if(parentStack):
		return parentStack.pop()
	return -1
def updateParentLayout(count):
	layoutDict[mapper[count]] = parentStack
def scanActivity():
	findClickable()
	print(parentStack)
	print(mapper)
	print(layoutDict)


parentStack = []
layoutDict = {}
mapper = {}
scanActivity()

