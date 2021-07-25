#!/usr/bin/python3

import os
import subprocess

def tap(x,y):
	args = "adb shell input tap " + str(x) + " " + str(y)
	subprocess.Popen(args, stderr=subprocess.STDOUT, shell=True)

def runADB(args):
	proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
	output_1 = proc.stdout.read().decode()
	processed_output = output_1.splitlines()
	return(processed_output)

def processADBcurrentActivity(args):
	s = args[0].split(' ')
	return(s[-2])

def activityXmlDump():
	args = "adb exec-out uiautomator dump /dev/tty | awk '{gsub(\"UI hierchary dumped to: /dev/tty\", \"\");print}'"
	return(runADB(args))

def currentActivityIdentifier():
	args = 'adb shell "dumpsys activity activities | grep mResumedActivity"'
	#print(processADBcurrentActivity(runADB(args)))
	return(processADBcurrentActivity(runADB(args)))
	
def startActivity(var):
	args = "adb shell am start -n " + var
	subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

def goBack():
	#print("yyyyy")
	args = "adb shell input keyevent 4"
	subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)