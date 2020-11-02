import RPi.GPIO as GPIO
from time import sleep
import sys
import os

# set the GPIO mapping to Broadcom GPIO
GPIO.setmode(GPIO.BCM)
# set up GPIO pin 12 as input, 
# default value up/1 with internal resistor
GPIO.setup(12, GPIO.IN, pull_up_down = GPIO.PUD_UP)
# set up GPIO pin 16 as output
GPIO.setup(16, GPIO.OUT)


def button_press():
    print("button pressed")
    GPIO.output(16,1)
    sleep(.5)
    os.system("aplay ./sounds/scream.wav")
    sleep(3)


# global vars
# no buttons have been pressed, yet
pressed = 0

try:
    while True:
        if GPIO.input(12) == 0:
            button_press()
            pressed = 1
        elif pressed == 1:
            GPIO.output(16,0)
            print("Button released")
            pressed = 0
except KeyboardInterrupt:
    # clean up settings
    GPIO.cleanup()
