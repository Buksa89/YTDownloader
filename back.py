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
                         'download_settings_correct': {0: "main_menu"},
                         'force_download_path_correct': {0: "main_menu"},

                         'clip_menu': {0: "main_menu"},
                         'mp3_menu': {0: "main_menu"},
                         'channel_menu': {0: "main_menu"}
                         }

        # set default screen to display:
        if self.path.read() == '':
            self.screen = 'force_download_path_input'
        else:
            self.screen = 'main_menu'


    def create_screen(self):
        """Create screen to display"""
        print(self.screen)
        variables = self.prepare_screen()                                   # prepare variables do display for user

        print("\n"*100)

        # Display screen from frontend
        screen = self.front.display_screen(self.screen,variables)
        print(screen)
        self.process_screen()                                              # Process special screens


        # If user can press any button, program will be ready to switch screen
        try:
            available_keys = list(map(str,self.menu_map[self.screen].keys()))   # Create list of available keys to press
            key_number = self.key_listener.start(available_keys)                # Turn on Key listener
            self.screen = self.menu_map[self.screen][int(key_number)]           # Select screen to switch
            self.create_screen()                                                # Switch screen
        except:
            print("nigdzie dalej nie przekierowuje")

    def prepare_screen(self):
        """This method prepare necessary variables for screens"""
        variables={}

        # Place for variables, if screen need them
        if self.screen == 'download_settings':
            variables['path'] = self.path.read()
        return variables

    def process_screen(self):
        """This method process special screens"""

        # Place for variables, if screen need them
        if self.screen == 'download_settings_input':
            path = input()
            if path == '': self.screen = 'main_menu'
            else:
                if self.path.is_valid(path):
                    self.path.write(path)
                    self.screen = 'download_settings_correct'
                else:
                    self.screen = 'download_settings_incorrect'
            self.create_screen()

        if self.screen == 'download_settings_incorrect':
            path = input()
            if path == '':
                self.screen = 'main_menu'
            else:
                if self.path.is_valid(path):
                    self.path.write(path)
                    self.screen = 'download_settings_correct'
                else:
                    self.screen = 'download_settings_incorrect'
            self.create_screen()

        if self.screen == 'force_download_path_input':
            path = input()
            if self.path.is_valid(path):
                self.path.write(path)
                self.screen = 'force_download_path_correct'
            else:
                self.screen = 'force_download_path_incorrect'
            self.create_screen()

        if self.screen == 'force_download_path_incorrect':
            path = input()
            if self.path.is_valid(path):
                self.path.write(path)
                self.screen = 'force_download_path_correct'
            else:
                self.screen = 'force_download_path_incorrect'
            self.create_screen()