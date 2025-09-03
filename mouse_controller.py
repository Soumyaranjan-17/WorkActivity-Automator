from pynput.mouse import Controller as MouseController
import time
import random

mouse = MouseController()

def scroll_mouse(steps=1):
    mouse.scroll(0, steps)  # negative = scroll down, positive = scroll up
    print(f"🖱️  Mouse scrolled {steps} step(s) down")

while True:
    scroll_mouse(random.randint(-3, 3))
    time.sleep(random.randint(5, 10))