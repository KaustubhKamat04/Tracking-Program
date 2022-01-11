import threading, time
from pynput.mouse import Button, Controller
from pynput.keyboard import KeyCode, Listener

button = Button.left
delay = 1.00
exit_key = KeyCode(char='END')
class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)

mouse = Controller()
click_thread = ClickMouse(delay, button)

def set_parameters(button, delay):
    button = button
    delay = delay  

def start_clicks():
    click_thread.start()
    click_thread.start_clicking()
    return ("Program Started..")

def stop_clicks():
    click_thread.stop_clicking()
    return ("Program Stoped..")

def exit_program():
    click_thread.exit()
    Listener.stop()
    return ("Exit Program Successful..")
    
with Listener(on_press=exit_key) as listener:
    listener.join()