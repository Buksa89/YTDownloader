class Front():
    """Program frontend"""
    def __init__(self):
        None

    def display_screen(self, screen, variables):
        content = ''
        if screen == "main_menu":
            content = """Press number, to choose:\n
            1: Choose download path
            2: Download single clip
            3: Download single clip as mp3
            4: Download channel
            ESC: Exit"""

        elif screen == "download_settings":
            content = f"""Current download path: {variables['path']}
            Wanna change it?\n
            1: Yes
            0: No, back to main menu
            ESC: Exit"""
        elif screen == "download_settings_input":
            content = "New download path (leave empty, if you don't want to change path): \n"
        elif screen == "download_settings_correct":
            content = """Path changed
            0: Back to main menu
            ESC: Exit"""
        elif screen == "download_settings_incorrect":
            content = "Path doesn't exist. Try again"

        elif screen == "force_download_path_input":
            content = "New download path: \n"
        elif screen == "force_download_path_correct":
            content = """Path changed
            0: Back to main menu
            ESC: Exit"""
        elif screen == "force_download_path_incorrect":
            content = "Path doesn't exist. Try again"

        elif screen == "clip_menu":
            # TODO: Create clip menu
            content = """Clip menu - NOT READY YET\n
            0: back to main menu
            ESC: Exit"""
        elif screen == "mp3_menu":
            # TODO: Create mp3 menu
            content = """MP# MENU - NOT READY YET\n
            0: back to main menu
            ESC: Exit"""
        elif screen == "channel_menu":
            # TODO: Create clip menu
            content = """Channel menu - NOT READY YET\n
            0: back to main menu
            ESC: Exit"""
        return content