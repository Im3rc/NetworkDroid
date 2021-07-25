#!/usr/bin/python3

import subprocess
from xml.dom import minidom
import sys
sys.path.insert(0, '/home/m3rc/Projects/NetworkDroid/adbController')
from adbScripts import *
from xmlCords import *

layoutDict = {}
mapper = {}
mapOfStacks = {}

stackMapper = 0

def findClickableInParent(mapOfStacks,stackMapper):
	mapOfStacks[stackMapper] = []
	xml_data = ""
	processed_output = activityXmlDump()
	for i in processed_output:
		if(i[0:5] == "<?xml"):
			xml_data = i
	#print(xml_data)
# 	Get current activity name
	nodes = minidom.parseString(xml_data).getElementsByTagName("node")
	for node in nodes:
		if(node.getAttribute("clickable") == "true"):
			if(node.getAttribute("resource-id") == "" and node.getAttribute("content-desc") != ""):
				push(mapOfStacks[stackMapper], node.getAttribute("content-desc"))
			elif(node.getAttribute("content-desc") == "" and node.getAttribute("resource-id") != ""):
				push(mapOfStacks[stackMapper], node.getAttribute("resource-id"))
			elif(node.getAttribute("content-desc") != "" and node.getAttribute("resource-id") != ""):
				push(mapOfStacks[stackMapper], node.getAttribute("content-desc"))
	#updateParentLayout(stack,count)

def findClickableInChild(mapOfStacks,stackMapper):
	xml_data = ""
	processed_output = activityXmlDump()
	for i in processed_output:
		if(i[0:5] == "<?xml"):
			xml_data = i
	#print(xml_data)
# 	Get current activity name
	nodes = minidom.parseString(xml_data).getElementsByTagName("node")
	for node in nodes:
		if(node.getAttribute("clickable") == "true"):
			if(node.getAttribute("resource-id") == "" and node.getAttribute("content-desc") != ""):
				pushChild(stackMapper, node.getAttribute("content-desc"))
			elif(node.getAttribute("content-desc") == "" and node.getAttribute("resource-id") != ""):
				pushChild(stackMapper, node.getAttribute("resource-id"))
			elif(node.getAttribute("content-desc") != "" and node.getAttribute("resource-id") != ""):
				pushChild(stackMapper, node.getAttribute("content-desc"))
	#updateParentLayout(stack,count)
def clickEvent(mapOfStacks,stackMapper,count):

#['Drawer Open', 'Start', 'Settings', 'Connections', 'com.emanuelef.remote_capture:id/status_view', 'com.emanuelef.remote_capture:id/dump_mode_spinner', 'com.emanuelef.remote_capture:id/app_filter_switch']
	currentActivity = ""
	c = stackMapper
	# if(c != 0):
	# 	c = c-1
	x = pop(mapOfStacks[c])
	while(x != "-1"):
		args = " "
		if args in x:
			executeCords_content(x)
			stackMapper = stackMapper + 1 
			currentActivity = currentActivityList()
			try:
				if(count == 0):
					mapper[count] = currentActivity
				else:
					if(mapper[count] != currentActivity):
						count = count + 1 
						mapper[count] = currentActivity
			except Exception as e:
				mapper[count] = currentActivity
			#updateParentLayout(mapOfStacks,stackMapper,count)
			findClickableInChild(mapOfStacks,stackMapper) 
			print("By content-desc")
			print(mapOfStacks)
			# if(set(mapOfStacks[stackMapper]) == set(mapOfStacks[stackMapper-1])):
			# 	startActivity(mapper[count])
			# 	clickEvent(mapOfStacks,stackMapper,count)
		else:
			executeCords_id(x)
			stackMapper = stackMapper + 1 
			currentActivity = currentActivityList()
			try:
				if(count == 0):
					mapper[count] = currentActivity
				else:
					if(mapper[count] != currentActivity):
						count = count + 1 
						mapper[count] = currentActivity
			except Exception as e:
					mapper[count] = currentActivity
			#updateParentLayout(mapOfStacks,stackMapper,count)
			findClickableInChild(mapOfStacks,stackMapper)
			print("By resource-id") 
			print(mapOfStacks)
			# if(set(mapOfStacks[stackMapper])== set(mapOfStacks[stackMapper-1])):
			# 	startActivity(mapper[count])
			# 	clickEvent(mapOfStacks,stackMapper,count)
		x = pop(mapOfStacks[stackMapper-1])
		print(x)
		#if(stackMapper != 0 and x=="-1"):
		# if(mapOfStacks[stackMapper] is None):
		# 	print("%")
		# 	startActivity(mapper[count])
		# 	clickEvent(mapOfStacks,stackMapper,count)

def push(stack, data):
	stack.append(data)
	#print(stack)

def pushChild(stackMapper, data):
	mapOfStacks[stackMapper+1] = data
	print(mapOfStacks[stackMapper+1])


def pop(stack):
	if(stack):
		return stack.pop()
	return -1

def updateParentLayout(mapOfStacks, stackMapper, count):
	layoutDict[mapper[count]] = mapOfStacks[stackMapper]

def scanActivity():
	count = 0
	findClickableInParent(mapOfStacks,stackMapper)
	clickEvent(mapOfStacks,stackMapper,count)
	#print(parentStack)
	#print(mapper)
	#print(layoutDict)
	print(mapOfStacks)
	


layoutDict = {}
mapper = {}
mapOfStacks = {}
stackMapper = 0
scanActivity()

