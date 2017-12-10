import RPi.GPIO as GPIO
import os
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN)
GPIO.setup(13, GPIO.IN) #pull_up_down = GPIO.PUD_UP
GPIO.setup(19, GPIO.IN)

try:
    while True:
        if(GPIO.input(5) == True):
            os.system('omxplayer /home/pi/Music/OhHiMark.mp3')
        elif(GPIO.input(13) == True):
            os.system('omxplayer /home/pi/Music/TearingMeApartLisa.mp3')
        elif(GPIO.input(19) == True):
            os.system('omxplayer /home/pi/Music/JustAChickenCheep.mp3')
        time.sleep(.1);

finally:
    GPIO.cleanup()
