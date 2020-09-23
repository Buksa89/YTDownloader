from pynput.keyboard import Key, Listener
import sys

class KeyListener():
    """A class for listening keyboard and manage events"""

    def __init__(self, menu):
        """Initialize listening"""
        self.menu = menu
        with Listener(on_release=self.on_release) as listener:
            listener.join()

    def on_release(self, key):
        """Manage events"""
        if key == Key.esc:
            # Exit program
            sys.exit()
        else:
            # Clean key names
            key = str(key)
            if key.startswith("'") and key.endswith("'"):
                key=key[1:-1]

            # Sending feedback to menu for switch page
            self.menu.switch_page(key)