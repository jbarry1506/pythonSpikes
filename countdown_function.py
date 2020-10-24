import sys
import pyglet


COUNTDOWN = 5


def reset(w, c):
    w.time = c # * 60
    w.running = False
    w.label.text = "Trick or Treat!"
    w.label.color = (255, 255, 255, 255)


def update(w, dt):
    if w.running:
        time -= dt
        m, s = divmod(time, 60)
        label.text = '%02d:%02d' % (m, s)
        if m < 5:
            label.color = (180, 0, 0, 255)
        if m < 0:
            running = False
            label.text = 'Trick or Treat!'


if __name__ == "__main__":

    window = pyglet.window.Window(fullscreen=True)
    pyglet.clock.schedule_interval(update(window, 1), 1)
    window.start = ':0%s' % str(COUNTDOWN-2)
    label = pyglet.text.Label(window.start, font_size=160,
                                       x=window.width//2, y=window.height//2,
                                       anchor_x='center', anchor_y='center')
    
    @window.event
    def on_draw():
        window.clear()
        label.draw()

    pyglet.app.run()

    reset(window, COUNTDOWN)