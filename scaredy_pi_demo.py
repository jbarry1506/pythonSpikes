'''
    Digi-Key Raspberry Pi Halloween candy dispenser
    October 2018
    Kyle Meier
    Digi-Key Electronics

    Credit to these sites used for code reference:
    https://www.instructables.com/id/Servo-Motor-Control-With-Raspberry-Pi/
    https://stackoverflow.com/questions/20021457/playing-mp3-song-on-python
    https://raspberrypi.stackexchange.com/questions/667/is-it-possible-to-install-vlc/46829#46829
    https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/4
    https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/
    https://makezine.com/projects/tutorial-raspberry-pi-gpio-pins-and-python/
    https://learn.sparkfun.com/tutorials/raspberry-gpio/gpio-pinout
'''

from time import sleep
from picamera import PiCamera # Enable camera in Preferences>Raspberry Pi Configuration>Interfaces
import vlc # In terminal, "sudo apt-get install vlc" and then "pip3 install python-vlc"
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) # Sets pin numbering scheme to BCM 
GPIO.setup(12, GPIO.OUT) # PWM output to servo signal pin (typically yellow or white). Remember to connect the positive and negative of the servo to 5V and GND.
GPIO.setup(16, GPIO.OUT) # Logic output pin for the power strip (positive). Other power strip wire will go to GND.
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # Input from pushbutton, using internal pulldown resistor. Other button wire will connect to 5V pin.
pwm = GPIO.PWM(12, 50) # PWM Frequency for servo set at 50Hz
pwm.start(0) # Start PWM with duty cycle of 0 (no signal being sent to servo)
camera = PiCamera() # Setup pi camera
p = vlc.MediaPlayer("/home/pi/Desktop/scream1.mp3") # The scream sound track we'll be playing. Modify to match location and name of your sound file. I used this track: https://freesound.org/people/adriancalzon/sounds/220619/

# Variables
buttonpress = 0
picnum = 0

# Function to set the servo angle
def SetAngle(angle):
    duty = angle / 18   # 2
    GPIO.output(12, 1)
    pwm.ChangeDutyCycle(duty)
    sleep (0.5)
    GPIO.output(12, 0)
    pwm.ChangeDutyCycle(0)

while (1):
    if (GPIO.input(18) == 1):
        camera.start_preview() # STart preview for the camera, it takes a little time for it to adjust to the lighting conditions.
        SetAngle(0) # Set servo's angle to 0 degrees, opening the flap.
        sleep (1)            
        GPIO.output(16, 1) # Turn the power strip (light) on
        p.play() # Play the mp3 track selected in the setup
        for i in range(5):
            #Make sure to create a new folder on the desktop named "pictures" 
            ''' 
            Capture a picture- note the "%s" in the save location, this will insert the value of the picnum variable
            in the image's title. This allows us to store multiple images instead of rewriting over the previously saved image. 
            '''
            camera.capture('/home/pi/Desktop/pictures/image%s.jpg' %picnum) 
            picnum  = 1 # Increment the picnum variable by 1
            sleep (1) # Time delay between pictures
        buttonpress = 1
    elif (buttonpress == 1):
        p.stop()
        camera.stop_preview()
        SetAngle(85)
        buttonpress = 0
        GPIO.output(16, 0)
    