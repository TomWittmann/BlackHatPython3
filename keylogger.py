'''
Allows us to monitor and control mouse and keyboard.
'''
import pynput.keyboard

log = ""

'''
A callback function. A callback function is a function passed to a method so that the method
can call the function when the method has completed its work. 
'''
def process_key_press(key):
    global log  #Using global variable so it is not created every time.
    log += str(key)
    print(log)


keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)    #Everytime a key is pressed print it.

with keyboard_listener:
    keyboard_listener.join()






