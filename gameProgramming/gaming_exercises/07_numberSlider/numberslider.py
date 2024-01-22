# Sliding your numbers game, by Johnson Traevon, v0.1

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
FPS = 30 # This is a maximum value! Won't make a slow computer run faster
BLANK = None

# Color values in (R, G, B) format.
# 0 = No Value, 255 = Max Value
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BRIGHTBLUE = (0, 50, 255)
DARKTURQUOISE = (3, 54, 73)
GREEN =  (0, 204, 0)

# BOARD DESIGN SETUP 
BGCOLOR = DARKTURQUOISE
TILECOLOR = GREEN
TEXTCOLOR = WHITE
BORDERCOLOR = BRIGHTBLUE
BASICFONTSIZE = 20
