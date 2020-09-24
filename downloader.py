from front import Front
from back import Back

# Crate Frontend and Backend objects
front = Front()
back = Back(front)

# Start program
back.create_screen()
