import os

class DownloadPath():
    """A class managed path for download files"""

    def __init__(self):
        """Create file 'path' if not exist"""
        if not os.path.isfile('path'):
            with open('path', 'w'): None

    def read_path(self):
        """Open path-file and read path from there"""
        with open('path') as file_object:
            return file_object.read()

    def path_valid(self, path):
        """Is path correct?"""
        return os.path.isdir(path)

    def write_path(self):
        """Write new path to file"""

    def set_path(self):
        """set path to read and write files"""

