import pyglet
window = pyglet.window.Window()

def zpracuj_text(text):
    print(text)
def tik(t):
    print(t)
#spousti se 30x ya vterinu,
pyglet.clock.schedule_interval(tik, 1/30)

window.push_handlers(on_text=zpracuj_text)
pyglet.app.run()
print('Hotovo!')