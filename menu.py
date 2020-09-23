

class Menu():
    """A class for display the menu and process user's choices"""

    def __init__(self):
        """Initialize menu and set default page as "main menu"""

        self.page="main_menu"
        self.show_menu()

    def switch_page(self, key):
        """Switching and display menu page"""

        # Map of menu
        menu_map = {'main_menu': {'1': "download_settings",
                               '2': "clip_menu",
                               '3': "mp3_menu",
                               '4': "channel_menu"},
                    'download_settings': {'1': "main_menu"},
                    'clip_menu': {'1': "main_menu"},
                    'mp3_menu': {'1': "main_menu"},
                    'channel_menu': {'1': "main_menu"}
                    }

        # Switching page of menu (depends of current page)
        try:
            self.page = menu_map[self.page][key]
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n###########################################\n")
            self.show_menu()
        except:
            None


    def show_menu(self):
        """Display menu"""
        # TODO Processing menu pages:
        # TODO 1: default download path
        # TODO 2: stop listening, when user input data
        # TODO 3: import yt library
        # TODO 4: download files
        # TODO 5: channel scraping
        self.print_menu_content()


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
            # TODO: Create download settings page
            print("""NOT READY YET\n
            1: back to main menu""")
        elif self.page == "clip_menu":
            # TODO: Create clip menu
            print("""NOT READY YET\n
            1: back to main menu""")
        elif self.page == "mp3_menu":
            # TODO: Create mp3 menu
            print("""NOT READY YET\n
            1: back to main menu""")
        elif self.page == "channel_menu":
            # TODO: Create clip menu
            print("""NOT READY YET\n
            1: back to main menu""")
