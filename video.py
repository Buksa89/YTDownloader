from pytube import YouTube
import shutil, os, re

class Video():
    """A class managed video files"""

    def __init__(self, link):
        """Set YT link and download path"""
        self.link = ''
        self.title = ''
        self.link_is_correct = False
        try:
            self.video = YouTube(link.strip())
            self.link_is_correct = True
        except:
            None

    def download(self, path):
        name = self.video.title
        print(f"Downloading file \"{name}\"")
        file = self.video.streams.get_highest_resolution()
        file.download(path)

    def download_as_mp3(self, path):
        name = self.video.title
        print(f"Downloading file \"{name}\"")
        file = self.video.streams.get_audio_only()
        file.download(path)
        name = re.sub('\W+', ' ', name).strip()
        mp4_path = os.path.join(path,name+'.mp4')
        print(mp4_path)
        mp3_path = os.path.join(path,name+'.mp3')
        shutil.move(mp4_path,mp3_path)