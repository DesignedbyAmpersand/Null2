#!/bin/python
#shutdown with a button

import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def Shutdown(channel):
	os.system("sudo shutdown -h now")

GPIO.add_event_detect(5, GPIO.FALLING, callback = Shutdown, bouncetime = 2000)

while 1:
	time.sleep(1)
