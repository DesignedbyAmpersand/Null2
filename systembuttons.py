#!/bin/python
# Shutdown and volume control

import keyboard
import time
import os
 
BOUNCE_TIME = 100
INITIAL_VOLUME = 50
 
volume = INITIAL_VOLUME
 
def shutdown():
    os.system("sudo shutdown -h now")
 
def volumeUp():
    global volume
    volume = min(65, volume + 5)
    os.system("amixer sset -q 'PCM' " + str(volume) + "%")
 
def volumeDown():
    global volume
    volume = max(0, volume - 5)
    os.system("amixer sset -q 'PCM' " + str(volume) + "%")

keyboard.add_hotkey('y+s', callback=volumeUp)
keyboard.add_hotkey('y+a', callback=volumeDown)
keyboard.add_hotkey('y+left alt', callback=shutdown)
 
keyboard.wait()