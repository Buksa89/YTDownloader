from key_listener import KeyListener
from video import Video
import time

class Screen():

    """Menu and screens"""

    def __init__(self, name, path):
        self.path = path
        self.name = name
        self.next = ''
        self.menu_map = {'main_menu': {1: "set_download_path",  # Map of menu with keys to switch screen
                                  2: "video_menu",
                                  3: "mp3_menu",
                                  4: "channel_menu"},

                    'set_download_path': {1: "set_download_path_input",
                                          0: "main_menu"},
                    'video_valid': {1: "video_menu",
                                    0: "main_menu"},
                    'mp3_valid': {1: "mp3_menu",
                                    0: "main_menu"},

                    }
        self.display_screen()
        self.process_screen()

    def process_screen(self):

        if self.name in self.menu_map.keys(): self.set_next_screen()

        elif self.name == 'force_download_path' or self.name == 'force_download_path_invalid':
            path = input()
            if self.path.is_valid(path):
                self.path.write(path)
                self.next = 'force_download_path_valid'
            else:
                self.next = 'force_download_path_invalid'

        elif self.name == 'set_download_path_input' or self.name == 'set_download_path_invalid':
            path = input()
            if path == '':
                self.next = 'main_menu'
            else:
                if self.path.is_valid(path):
                    self.path.write(path)
                    self.next = 'set_download_path_valid'
                else:
                    self.next = 'set_download_path_invalid'

        elif self.name == 'set_download_path_valid':
            time.sleep(2)
            self.next = 'main_menu'

        elif self.name == 'video_menu' or self.name == 'video_invalid':
            link = input()
            if link == '': self.next = 'main_menu'
            else:
                video = Video(link)
                if video.link_is_correct:
                    video.download(self.path.read())
                    self.next = 'video_valid'
                else:
                    self.next = 'video_invalid'


        elif self.name == 'mp3_menu' or self.name == 'mp3_invalid':
            link = input()
            if link == '': self.next = 'main_menu'
            else:
                video = Video(link)
                if video.link_is_correct:
                    video.download_as_mp3(self.path.read())
                    self.next = 'mp3_valid'
                else:
                    self.next = 'mp3_invalid'



    def display_screen(self):
        content = '\n'*100+'-'*100+'\n'
        if self.name == "main_menu":
            content += """Press number, to choose:\n
            1: Choose download path
            2: Download single clip
            3: Download single clip as mp3
            4: Download channel
            ESC: Exit"""


        elif self.name == "set_download_path":
            content += f"""Current download path: {self.path.read()}
            Wanna change it?\n
            1: Yes
            0: No, back to main menu
            ESC: Exit"""
        elif self.name == "set_download_path_input":
            content += "New download path (leave empty, if you don't want to change path): \n"
        elif self.name == "set_download_path_valid": content += """Path changed. Redirecting to main menu"""
        elif self.name == "set_download_path_invalid": content += "Path doesn't exist. Try again"


        elif self.name == "force_download_path": content += "New download path: \n"
        elif self.name == "force_download_path_valid": content += """Path changed. Redirecting to main menu"""
        elif self.name == "force_download_path_invalid": content += "Path doesn't exist. Try again"


        elif self.name == "video_menu":
            content += """Youtube link (leave empty, if you want to back to main menu): \n"""
        elif self.name == "video_valid": content += """File downloaded
            1: Download another video
            0: Back to main menu
            ESC: Exit"""
        elif self.name == "video_invalid": content += "Link incorrect Try again"



        elif self.name == "mp3_menu":
            content += """Youtube download as mp3:\nYoutube link (leave empty, if you want to back to main menu): \n"""
        elif self.name == "mp3_valid": content += """File downloaded
            1: Download another mp3
            0: Back to main menu
            ESC: Exit"""
        elif self.name == "mp3_invalid": content += "Link incorrect Try again"



        elif self.name == "channel_menu":
            # TODO: Create clip menu
            content += """Channel menu - NOT READY YET\n
            0: back to main menu
            ESC: Exit"""
        print(content)

    def set_next_screen(self):
        key_listener = KeyListener()
        available_keys = list(map(str, self.menu_map[self.name].keys()))  # Create list of available keys to press
        key_number = key_listener.start(available_keys)  # Turn on Key listener
        self.next = self.menu_map[self.name][int(key_number)]  # Select screen to switch