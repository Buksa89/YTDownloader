from menu import Menu
from key_listener import KeyListener

def run_downlader():
    # Crate menu-object for display and process interactive menu
    menu = Menu()
    KeyListener(menu)

run_downlader()
