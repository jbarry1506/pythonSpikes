import RPi.GPIO as GPIO
from time import sleep
import sys
import pyglet

# set the GPIO mapping to Broadcom GPIO
GPIO.setmode(GPIO.BCM)
# set up GPIO pin 12 as input, 
# default value down/0 with internal resistor
GPIO.setup(12, GPIO.IN, pull_up_down = GPIO.PUD_UP)
# set up GPIO pin 16 as output
GPIO.setup(16, GPIO.OUT)
# set up countdown window
window = pyglet.window.Window(fullscreen=True)
COUNTDOWN = 5


class Timer(object):
    def __init__(self):
        self.start = ':0%s' % str(COUNTDOWN-2)
        self.label = pyglet.text.Label(self.start, font_size=160,
                                       x=window.width//2, y=window.height//2,
                                       anchor_x='center', anchor_y='center')
        self.reset()

    def reset(self):
        self.time = COUNTDOWN # * 60
        self.running = False
        self.label.text = self.start
        self.label.color = (255, 255, 255, 255)

    def update(self, dt):
        if self.running:
            self.time -= dt
            m, s = divmod(self.time, 60)
            self.label.text = '%02d:%02d' % (m, s)
            if m < 5:
                self.label.color = (180, 0, 0, 255)
            if m < 0:
                self.running = False
                self.label.text = 'Trick or Treat!'

@window.event
def on_key_press(symbol, modifiers):
    timer.running = True
    window.close()
    # if symbol == pyglet.window.key.SPACE:
    #    if timer.running:
    #        timer.running = False
    #    else:
    #        timer.running = True
    # elif symbol == pyglet.window.key.ESCAPE:
    #    window.close()

@window.event
def on_draw():
    window.clear()
    timer.label.draw()


def button_press():
    print("button pressed")
    GPIO.output(16,1)
    pyglet.clock.schedule_interval(timer.update, 1)
    pyglet.app.run()



# global vars
timer = Timer()
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
            window = pyglet.window.Window(fullscreen=True)
except KeyboardInterrupt:
    # clean up settings
    GPIO.cleanup()