class Front():
    """Program frontend"""
    def __init__(self):
        None

    def display_screen(self, screen):
        if screen == "main_menu":
            print("""Press number, to choose:\n
            1: Choose download path
            2: Download single clip
            3: Download single clip as mp3
            4: Download channel
            ESC: Exit""")

        elif screen == "download_settings":
            print("""NOT READY YET\n
            0: back to main menu""")
        elif screen == "download_settings_input":
            print("""NOT READY YET\n
            0: back to main menu""")

        elif screen == "clip_menu":
            # TODO: Create clip menu
            print("""NOT READY YET\n
            0: back to main menu""")
        elif screen == "mp3_menu":
            # TODO: Create mp3 menu
            print("""NOT READY YET\n
            0: back to main menu""")
        elif screen == "channel_menu":
            # TODO: Create clip menu
            print("""NOT READY YET\n
            0: back to main menu""")