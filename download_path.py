import os

class DownloadPath():
    """A class managed path for download files"""

    def __init__(self):
        """Create file 'path' if not exist"""
        if not os.path.isfile('path'):
            with open('path', 'w'): None

    def read(self):
        """Open path-file and read path from there"""
        with open('path') as file_object:
            return file_object.read()

    def is_valid(self, path):
        """Is path correct?"""
        return os.path.isdir(path)

    def write(self, path):
        """Write new path to file"""
        with open('path','w') as file_object:
            file_object.write(path)

