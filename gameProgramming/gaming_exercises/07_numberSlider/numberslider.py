# Sliding your numbers game, by Johnson Traevon, v0.0

import sys, random, pygame
# sys module provides access to system resources such as operating system

from pygame.locals import *
# Allows us to call features from pygame using just the function name instead of module.function()
# Example: We can use draw() instead of pygame.draw()

# Constants for game board
BOARDWIDTH = 4 # COLUMNS
BOARDHEIGT = 4 # ROWS
TILESIZE = 80 # MEASURED IN PIXELS
WINDOWWIDTH = 640 # MEASURED IN PIXELS
WINDOWHEIGHT = 480 # MEASURED IN PIXELS
FPS = 5 # This is a maximum value! Won't make a slow computer run faster
BLANK = None
