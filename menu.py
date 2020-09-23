from key_listener import KeyListener

class Menu():
    """A class for display the menu and process user's choices"""

    def __init__(self):
        """Initialize menu and set default page as "main menu"""

        # Initialize key-listening alghorytm
        self.key_listener = KeyListener()

        # set default page of menu:
        self.page = 'main_menu'

        # Prepare map of menu with keys to change page
        self.menu_map = {'main_menu': {1: "download_settings",
                                  2: "clip_menu",
                                  3: "mp3_menu",
                                  4: "channel_menu"},
                    'download_settings': {0: "main_menu"},
                    'clip_menu': {0: "main_menu"},
                    'mp3_menu': {0: "main_menu"},
                    'channel_menu': {0: "main_menu"}
                    }

        self.show_menu()


    def show_menu(self):
        """Display menu"""

        # Displaying menu
        self.print_menu_content()

        # Create list of available keys
        available_keys = list(map(str,self.menu_map[self.page].keys()))
        # Turn on Key listener
        next_page = self.key_listener.start(available_keys)

        # switch page
        self.switch_page(next_page)

        # TODO Processing menu pages:
        # TODO 1: default download path
        # TODO 3: import yt library
        # TODO 4: download files
        # TODO 5: channel scraping


    def switch_page(self, next_page):
        """Switching page"""

        self.page = self.menu_map[self.page][int(next_page)]
        print("\n"*100)
        self.show_menu()


    def print_menu_content(self):
        """Print menu page content"""

        if self.page == "main_menu":
            print("""Press number, to choose:\n
            1: Choose download path
            2: Download single clip
            3: Download single clip as mp3
            4: Download channel
            ESC: Exit""")
        elif self.page == "download_settings":
            print("""Download setting\n
            0: back to main menu""")
        elif self.page == "clip_menu":
            # TODO: Create clip menu
            print("""NOT READY YET\n
            0: back to main menu""")
        elif self.page == "mp3_menu":
            # TODO: Create mp3 menu
            print("""NOT READY YET\n
            0: back to main menu""")
        elif self.page == "channel_menu":
            # TODO: Create clip menu
            print("""NOT READY YET\n
            0: back to main menu""")
