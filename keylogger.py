
'''
Allows us to monitor and control mouse and keyboard.
'''
import pynput.keyboard

def process_key_press(key):
    print(key)

keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)    #Everytime a key is pressed print it.

with keyboard_listener:
    keyboard_listener.join()






