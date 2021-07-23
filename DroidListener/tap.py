#!/usr/bin/python3

import os
import subprocess

def tap(x,y):
	args = "adb shell input tap " + str(x) + " " + str(y)
	subprocess.Popen(args, stderr=subprocess.STDOUT, shell=True)