import RPi.GPIO as GPIO
from time import sleep

# set the GPIO mapping to Broadcom GPIO
GPIO.setmode(GPIO.BCM)
# set up GPIO pin 12 as input, 
# default value down/0 with internal resistor
GPIO.setup(12, GPIO.IN, pull_up_down = GPIO.PUD_UP)
# set up GPIO pin 16 as output
GPIO.setup(16, GPIO.OUT)

try:
    while True:
        if GPIO.input(12) == 0:
            print("button pressed")
            GPIO.output(16,1)
        else:
            GPIO.output(16,0)
            # print("Button released")
except KeyboardInterrupt:
    # clean up settings
    GPIO.cleanup()