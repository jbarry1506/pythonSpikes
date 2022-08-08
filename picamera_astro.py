"""
Script to try out astrophotography with a legacy picam.
"""

import picamera
# import keyboard
from pynput import keyboard
import datetime

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
        print('Taking a picture')
        dt = datetime.datetime.now()
        cam.capture(output=f"{dt}.jpg")
    if key == keyboard.Key.esc:
        # stop listener
        return False


with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    listener.join()

