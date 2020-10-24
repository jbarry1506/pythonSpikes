import RPi.GPIO as GPIO
from time import sleep

# set the GPIO mapping to Broadcom GPIO
GPIO.setmode(GPIO.BCM)
# set up GPIO pin 16 as output
GPIO.setup(16, GPIO.OUT)

# turn pin 16 on for 1 second, turn off for 1 second
i = 0
for i in range(10):
    GPIO.output(16,1)
    sleep(2)
    GPIO.output(16,0)
    sleep(2)
