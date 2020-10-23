import random
import time

from pynput.keyboard import Key, Controller

keyboard = Controller()

while True:
    keyboard.press(Key.space)
    delay = random.uniform(0, 2)  # Generate a random number between 0 and 10
    time.sleep(delay)
