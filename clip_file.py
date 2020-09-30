from pytube import YouTube

class ClipFile():
    """A class managed video files"""

    def __init__(self, link):
        """Set YT link and download path"""
        self.link = ''
        self.title = ''
        self.link_is_correct = False
        try:
            self.link = YouTube(link[:-1])
            self.link_is_correct = True
        except:
            None

    def download(self, path):
        name = self.link.title()
        print(f"Downloading file {name}")
        file = self.link.streams.get_by_itag('22')
        file.download(path)