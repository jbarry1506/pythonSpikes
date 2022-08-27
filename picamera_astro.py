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

"""
TODO:
- accept args:
    - mount drive
    - frame length
- create logs for errors
- try/except blocks
"""

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
    # if key.char == 't':
    #     logging.info(f'[{datetime.datetime.now()}]:  Time captures')
    #     dt = str(datetime.datetime.now()).replace(' ','').replace('.','-').replace(':','-')

    if key == keyboard.Key.esc:
        # stop listener
        return False


with keyboard.Listener(
    on_press=on_press,
    on_release=on_release) as listener:
    listener.join()

