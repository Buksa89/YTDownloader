from download_path import DownloadPath
from screen import Screen

path = DownloadPath()  # initialize download path managing object

# set default screen to display:
if path.read() == '':
    screen_name = 'force_download_path'
else:
    screen_name = 'main_menu'

# Main loop
while True:
    screen = Screen(screen_name, path)      # Start screen by name
    screen_name = screen.next               # Change name for next screen