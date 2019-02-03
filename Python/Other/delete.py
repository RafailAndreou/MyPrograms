import keyboard
import time

while True:
    x = input('What to type: ')
    time.sleep(3)
    for word in x:
        if word == " ":
            keyboard.press_and_release('space')
        else:
            keyboard.write(word)
