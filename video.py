from pytube import YouTube
import shutil, os, re

class Video():
    """A class managed video files"""

    def __init__(self, link):
        """Set YT link and download path"""
        self.link_is_correct = False
        try:
            self.video = YouTube(link.strip())
            self.link_is_correct = True
        except:
            None

    def download(self, path, as_mp3=False):
        """Download file from link"""

        name = self.video.title
        name = re.sub('\W+', ' ', name).strip()
        print(f"Downloading file \"{name}\"")
        if as_mp3:
            file = self.video.streams.get_audio_only()
            file.download(output_path=path, filename=name)
            mp4_path = os.path.join(path, name + '.mp4')
            print(mp4_path)
            mp3_path = os.path.join(path, name + '.mp3')
            shutil.move(mp4_path, mp3_path)
        else:
            file = self.video.streams.get_highest_resolution()
            file.download(output_path=path, filename=name)

