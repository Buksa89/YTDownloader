from download_path import DownloadPath
from key_listener import KeyListener

class Back():
    """Program backend"""
    def __init__(self, front):
        """Initialize necessary objects and variables"""
        self.front = front
        self.path = DownloadPath()                                    # initialize download path managing object
        self.key_listener = KeyListener()                             # Initialize key-listening object
        self.menu_map = {'main_menu': {1: "download_settings",        # Map of menu with keys to switch screen
                                       2: "clip_menu",
                                       3: "mp3_menu",
                                       4: "channel_menu"},

                         'download_settings': {1: "download_settings_input",
                                               0: "main_menu"},

                         'clip_menu': {0: "main_menu"},
                         'mp3_menu': {0: "main_menu"},
                         'channel_menu': {0: "main_menu"}
                         }

        # set default screen to display:
        if self.path.read_path() == '':
            self.screen = 'force_download_path_input'
        else:
            self.screen = 'main_menu'


    def create_screen(self):
        """Create screen to display"""

        self.front.display_screen(self.screen)                                  # Display screen from frontend

        # If user can press any button, program will be ready to switch screen
        try:
            available_keys = list(map(str,self.menu_map[self.screen].keys()))   # Create list of available keys to press
            key_number = self.key_listener.start(available_keys)                # Turn on Key listener
            self.screen = self.menu_map[self.screen][int(key_number)]           # Select screen to switch
            self.create_screen()                                                # Switch screen
        except: None


