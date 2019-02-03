import time
from pynput.keyboard import Key,Controller,Listener

time.sleep(2)

Keyboard = Controller()

def on_press(key):
    print('{0} pressed'.format(key))

def on_release(key):
    print('{0} release'.format(key))
    if key == Key.esc:
        return False

with Listener(on_press=on_press,on_release=on_release)as listener:
    listener.join()


