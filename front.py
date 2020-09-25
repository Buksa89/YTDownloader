class Front():
    """Program frontend"""
    def __init__(self):
        None

    def display_screen(self, screen, variables):
        content = ''
        user_response = ''
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
            content = """NOT READY YET\n
            0: back to main 
            ESC: Exit"""

        elif screen == "clip_menu":
            # TODO: Create clip menu
            content = """NOT READY YET\n
            0: back to main menu
            ESC: Exit"""
        elif screen == "mp3_menu":
            # TODO: Create mp3 menu
            content = """NOT READY YET\n
            0: back to main menu
            ESC: Exit"""
        elif screen == "channel_menu":
            # TODO: Create clip menu
            content = """NOT READY YET\n
            0: back to main menu
            ESC: Exit"""
        return content, user_response