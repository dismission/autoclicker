from pynput import keyboard
from pynput.mouse import Button, Controller
import threading
import time
import random
from pynput.keyboard import KeyCode
import shutil
from os import system
import subprocess

mouse = Controller()
delay = 0.05
jitterkeycode = KeyCode(char='p')



def mattclicker(cmd):
    subprocess.call(cmd, shell=True)

def clicker():
    global niggerclicker
    while 1:
        time.sleep(random.uniform(1, 1.6) * random.uniform(0.1, 0.001))
        if niggerclicker:
            mouse.press(Button.left)
            mouse.release(Button.left)


class Jitter(threading.Thread):
    def __init__(self, jitter):
        super(Jitter, self).__init__()
        self.jitter = jitter
        self.delay = delay
        self.running = False
        self.program_running = True

    def startjitter(self):
        self.running = True

    def stopjitter(self):
        self.running = False

    def quit(self):
        self.running = False
        self.program_running = False

    def stopprogram(self):
        self.program_running = False
    def startprogram(self):
        self.program_running = True

    def run(self):
        while self.program_running:
            while self.running:
                mouse.position = (random.randrange(950, 970), random.randrange(538, 542))
                time.sleep(self.delay)
            time.sleep(0.003)

jitter_thread = Jitter(delay)
jitter_thread.start()

def display_controls():
    width = shutil.get_terminal_size().columns
    print("// Jewclicker".center(width))
    print("// - Settings:".center(width))
    print("// <!> Create a macro on mouse button one to prsss do F12 <!>".center(width))
    print("// - Click - F12".center(width))
    print("// - Jitter - P".center(width))
    print("// - Self Destruct - PAGE_UP".center(width))
    print("// --------------------------------------------------".center(width))
    display_controls()





niggerclicker = False
Listener = threading.Thread(target=clicker, daemon=True)
Listener.start()
jitter = -5



def on_press(key):
    global niggerclicker
    global jitter
    if key == keyboard.Key.f12:
        niggerclicker = True
    if key == jitterkeycode:
        if jitter == -5:
            jitter = 5
        else:
            jitter = -5
    if key == keyboard.Key.f12:
        if jitter == 5:
            jitter_thread.startjitter()
        if jitter == -5:
            jitter_thread.stopjitter()


    elif key == keyboard.Key.page_up:
        jitter_thread.quit()

def on_release(key):
    global niggerclicker
    if key == keyboard.Key.f12:
        niggerclicker = False
    if key == keyboard.Key.f12:
        jitter_thread.stopjitter()
    if key == keyboard.Key.page_up:
        return False





with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

