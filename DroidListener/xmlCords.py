#!/usr/bin/python3	

import subprocess
from xml.dom import minidom
from tap import * 

def getCords():
	xml_data = ""
	proc = subprocess.Popen("adb exec-out uiautomator dump /dev/tty | awk '{gsub(\"UI hierchary dumped to: /dev/tty\", \"\");print}'", stdout=subprocess.PIPE,stderr=subprocess.STDOUT, shell=True)
	output_1 = proc.stdout.read().decode()
	processed_output = output_1.splitlines()
	for i in processed_output:
		if(i[0:5] == "<?xml"):
			xml_data = i
	nodes = minidom.parseString(xml_data).getElementsByTagName("node")
	return(nodes)

def processCords(c):
	c = c.replace("[","")
	c = c.replace("]",",")
	c = c[:-1]
	c = c.split(",")
	cords = []
	cords.append(int((int(c[0]) + int(c[2]))/2))
	cords.append(int((int(c[1]) + int(c[3]))/2))
	return(cords)

def executeCords_id(id):
	nodes = getCords()
	for node in nodes:
		if(node.getAttribute("resource-id") == id ):
			c = node.getAttribute("bounds")
	cords = processCords(c)
	tap(cords[0],cords[1])

def executeCords_content(id):
	nodes = getCords()
	c = ""
	for node in nodes:
		if(node.getAttribute("content-desc") == id ):
			c = node.getAttribute("bounds")
	cords = processCords(c)
	tap(cords[0],cords[1])