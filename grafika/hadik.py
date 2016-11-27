import pyglet
import math
window = pyglet.window.Window()

obrazek=pyglet.image.load('had.png')
obrazek2=pyglet.image.load('had2.png')
had=pyglet.sprite.Sprite(obrazek)

def vykresli():
    #premaluje okno cernou barvou
    window.clear()
    #vykresli hada
    had.draw()
    if had.x>=window.width:
        had.x=0

def zpracuj_text(text):
    had.x=150
def tik(t):
    had.x=had.x+t*20
    #had.y=20+20*math.sin(had.x/5)
    #had.rotation=had.rotation+200*t
def zmen(t):
    had.image=obrazek2
    pyglet.clock.schedule_once(zmen_zpatky, 0.1)
def zmen_zpatky(t):
    had.image=obrazek
    pyglet.clock.schedule_once(zmen, 0.1)
def klik(x, y, tlacitko, mod):
    had.x = x
    had.y = y
    if tlacitko==4:
        had.rotation+=90

#spousti se 30x ya vterinu,
pyglet.clock.schedule_interval(tik, 1/30)
pyglet.clock.schedule_once(zmen, 1)


window.push_handlers(on_draw=vykresli,
                     on_text = zpracuj_text,
                     on_mouse_press=klik)



pyglet.app.run()
print('Hotovo!')