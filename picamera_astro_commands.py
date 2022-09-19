"""
Script to try out astrophotography with a picam.
TODO - THIS NEEDS A GUI AND DB
"""

from ast import arg
from time import sleep
import picamera
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

# Defaults
astro_iso = None
astro_mode = None
astro_shutter = None

# take command line arguments
# TODO - VALIDATE ARGUMENTS
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--mode", required=False, default="still", 
    help="Accepted Values = 'still', 'series', 'video'")
ap.add_argument("-i", "--iso", required=False, help="Accepted Values = 200, 400, 600, 800")
ap.add_argument("-s", "--shutter", required=False, help="2000 < Shutter speed > 6000000")

# parse the arguments
args = vars(ap.parse_args())

# set the variables
astro_mode = args['mode']
astro_iso = args['iso']
astro_shutter = args['shutter']

today = datetime.datetime.today().date()

logging.basicConfig(filename=f"/home/jbarry1506/Documents/script_logs/astro/{today}_astro_error.log")


def catch_keypress(iso,shtr):
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
                cam.iso = int(iso)
                cam.shutter_speed = int(shtr)
                cam.resolution = (1920,1080)
                # sleep(3)
                cam.capture(output=f"/mnt/Astro/{dt}.jpg")

            if key == keyboard.Key.esc:
                # stop listener
                return False


        with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
            listener.join()


def cap_mode(md, iso, shtr):
    if md == None:
        md = "still"

    if md == "still":
        if iso == None:
            iso = 200
        if shtr == None:
            shtr = 10000
            
        # TODO - Create Decorator / helper function
        catch_keypress(iso,shtr)
        # END Decorator / helper function

    elif md == "series":
        pass
    elif md == "video":
        pass


if __name__ == "__main__":
    try:
        os.system("sudo mount /dev/sda1 /mnt")
    except Exception as e:
        logging.error(f"[{datetime.datetime.now()}]:  {e}")

    cam = picamera.PiCamera()
    cam.start_preview()

    cap_mode(astro_mode, astro_iso, astro_shutter)
