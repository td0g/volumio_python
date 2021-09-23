#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Written by Tyler Gerritsen
#td0g.ca

#apt-get install python3-pip
#pip3 install rpi.gpio

#https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/
#https://volumio.github.io/docs/API/REST_API.html

import time
import RPi.GPIO as GPIO
import requests

#################### Setup ##################

  #Set the GPIO Pins
buttonA_GPIO = 4


#################### Script ##################


print("Script started")
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonA_GPIO, GPIO.IN)

def sendCommand(c):
    url = "http://127.0.0.1:3000/api/v1/commands/?cmd=" + c
    print (url)
    res = requests.get(url)
    print(res.text)
    print()
    return res.text

def setVolume(v):
    if v < 0:
        v = 0
    if v > 100:
        v = 100
    print("Setting Volume to " + str(int(v)))
    sendCommand("volume&volume=" + str(int(v)))

def playPlaylist(p):
    print("Beginning playlist " + p)
    sendCommand("playplaylist&name=" + p)

def setRandom(r):
    if r:
        print("Randomizing ON")
        sendCommand("random&value=true")
    else:
        print("Randomizing OFF")
        sendCommand("random&value=false")

def playNext():
    print("Next")
    sendCommand("next")
    
def pause():
    print("Pausing playback")
    sendCommand("pause")
    
def isPlaying():
    url = "http://127.0.0.1:3000/api/v1/getstate"
    print (url)
    res = requests.get(url)
    print(str(res.text))
    if str(res.text).replace('"status":"play"',"") == str(res.text):
        print ("NOT PLAYING\n")
        return False
    else:
        print ("PLAYING\n")
        return True
    
def onButton():
    if isPlaying():
        sendCommand("pause")
    else:
        setVolume(0)
        playPlaylist("Kiera")
        setRandom(True)
        playNext()
        setVolume(50)
        

try:
  while True:
    time.sleep(0.05)
    r = GPIO.input(buttonA_GPIO)
    if r == 0:
      onButton()
      while GPIO.input(buttonA_GPIO) == 0:
        pass
      time.sleep(0.2)


except KeyboardInterrupt: 
  GPIO.cleanup()
  try:
    pass
  except:
    pass
