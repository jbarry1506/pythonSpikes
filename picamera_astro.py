"""
Script to try out astrophotography with a picam.
TODO - THIS NEEDS A GUI AND DB
"""

import picamera
# import keyboard
from pynput import keyboard
import datetime
import os
import logging
import argparse

"""
TODO:
- accept args:
    - mount drive
    - shutter speed
    - ISO
    - add validation, error messages, logs for all arguments
- create logs for errors
- try/except blocks
- create app
"""

# take command line arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-m", "--mode", required=False, default="still", help="Accepted Values = 'still', 'series', 'video'")
# ap.add_argument("-i", "--iso", required=False, help="Accepted Values = 200, 400, 600, 800")
# ap.add_argument("-s", "--shutter", required=False, help="2000 < Shutter speed > 6000000")

# parse the arguments



today = datetime.datetime.today().date()

logging.basicConfig(filename=f"/home/jbarry1506/Documents/script_logs/astro/{today}_astro_error.log")

try:
    os.system("sudo mount /dev/sda1 /mnt")
except Exception as e:
    logging.error(f"[{datetime.datetime.now()}]:  {e}")

cam = picamera.PiCamera()
cam.start_preview()

# MUST RUN AS ROOT!!!
# while True:
#     if keyboard.read_key() == "p":
#         dt = datetime.datetime.now()
#         print(f"You pressed p at {dt}")
#         # cam.capture(f"{dt}.jpg")

#     if keyboard.read_key() == "q":
#         dt = datetime.datetime.now()
#         print(f"keyboard capture q at {dt}")
#         # cam.stop_preview()
#         exit(0)

# Need to run this from the command line
def on_press(key):
    try:
        print(f'Alphanumeric key pressed: {key}')
        print(f"key == {key}")
        # if key == 'p':
        #     print('Taking a picture')
    except AttributeError:
        print(f"Special key pressed: {key}")

    
def on_release(key):
    print(f'Key released: {key}')
    if key.char == 'p':
        logging.info(f"[{datetime.datetime.now()}]:  taking a still shot")
        dt = str(datetime.datetime.now()).replace(' ','').replace('.','-').replace(':','-')
        cam.capture(output=f"/mnt/Astro/{dt}.jpg")

    # This loop does not work
    # if key.char == 't':
    #     while key.char != 's':
    #         logging.info(f'[{datetime.datetime.now()}]:  Time captures')
    #         dt = str(datetime.datetime.now()).replace(' ','').replace('.','-').replace(':','-')
    #         cam.capture(output=f"/mnt/Astro/{dt}.jpg")

    if key == keyboard.Key.esc:
        # stop listener
        return False


with keyboard.Listener(
    on_press=on_press,
    on_release=on_release) as listener:
    listener.join()

