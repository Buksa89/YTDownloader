import keyboard
import sys

class KeyListener():
    """A class for listening keyboard and manage events"""

    def __init__(self):
        None

    def start(self, available_keys):
        while True:
            key = keyboard.read_key()
            if key == 'esc':
                sys.exit()
            elif key in (available_keys):
                return key