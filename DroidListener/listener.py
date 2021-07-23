#!/usr/bin/python3

import subprocess
from xml.dom import minidom
from xmlCords import *
from tap import * 

def start_listener():
	subprocess.Popen("adb shell am start -n com.emanuelef.remote_capture/.activities.MainActivity", stdout=subprocess.PIPE,stderr=subprocess.STDOUT, shell=True)
	get_coordinates_to_start()

def get_coordinates_to_start():
	nodes = getCords()
	# for node in nodes:
	# 	print(node.getAttribute("content-desc"))
	#executeCords("com.emanuelef.remote_capture:id/action_start")
	#executeCords("com.emanuelef.remote_capture:id/pager")
	#content-desc="Connections"
	executeCords_content("Start")
	get_coordinates_to_save()
		
def get_coordinates_to_save():
	executeCords_id("android:id/button1")

def to_connections():
	executeCords_content("Connections")
	nodes = getCords()
	to_save_csv()
	# for node in nodes:
	# 	print(node.getAttribute("resource-id"))
	# 	print(node.getAttribute("content-desc"))

def to_save_csv():
	executeCords_id("com.emanuelef.remote_capture:id/save")
	get_coordinates_to_save()
	to_status_to_stop()

def to_status_to_stop():
	executeCords_content("Status")
	executeCords_content("Stop")
	executeCords_id("android:id/button3")
	


start_listener()
to_connections()