# 8B Geometry Dash Sponsored by RobTop, Created by Johnson Traveon and Christain Ortiz v0.9

# Kelley -- 04/25/24 -- Code Review 
# Create 'HEADERS' for each section of your code, such as 'Controls' or 'Screen Information' to keep the data organized. 
# Create a variable to track the current game level, use if and screen.blit() to display the correct level using that variable. 
# Start working on an actual playable level! 
'Import Modules'
import pygame, csv, os, random
from sys import exit
from pygame.math import Vector2
from pygame.draw import rect
'''Debugging Logs'''
logFile = "geometrydashDebugLog.txt"
logData = open(logFile, "w") 


pygame.init()


'''VARIABLESSS OF MY OWN'''
screen = True
screen2 = False
screen3 = False
particles = []
orbs = []
win_cubes = []
resolution = 1
welcome = 'geometry dash'
start = False
zodiac_Dis = 'top 1 hardest demon from 2018 - 2023'
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAVITY = Vector2(0, 0.86)
'Game Active/ Levels'
level1 = 'Zodiac'
level2 = 'digital descent'
game_active =  False
level1_active = False
level2_active = False
'''Resolution'''
if resolution == 1:
    x = 1152
    y = 648
elif resolution == 0:
    x = 800
    y = 600
else:
    print('This game only runs on Resolution 0 or 1.')
    
    


# BINTRICALIZATIONALISM



def resize(img, size=(32, 32)):
    """resize images
    :param img: image to resize
    :type img: im not sure, probably an object
    :param size: default is 32 because that is the tile size
    :type size: tuple
    :return: resized img

    :rtype:object?
    """
    resized = pygame.transform.smoothscale(img, size)
    return resized


# SENSAGREGORY INSTINCTUAL HOLOSCHLATERIAL
'''SURFACES'''
screen = pygame.display.set_mode((x,y))
screen2 = pygame.display.set_mode((x,y))
screen3 = pygame.display.set_mode((x,y))
alpha_surf = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    
pygame.display.set_caption('Geometry Dash')
clock = pygame.time.Clock()


geometry_bg = pygame.image.load('img/Gd background.jpg').convert_alpha()
cEdit = pygame.image.load('img/GD CEdit.jpg').convert_alpha()
font = pygame.font.Font('img/Seagram.ttf', 60)
font2 = pygame.font.Font('img/Seagram.ttf', 40)
tip = font.render("tip: tap and hold for the first few seconds of the level", True, BLUE)
geometry_surface = font.render('geometry dash', True, 'Green', None)
geometry_editor = pygame.image.load('img/editor button.png').convert_alpha()
playership = pygame.image.load('img/bird_108.png').convert_alpha()
# geometry_rect = geometry_surface.get_rect(center = (400,150))
geometry_pb = pygame.image.load('img/Gd play.jpg').convert_alpha()
gdpb_rect = geometry_pb.get_rect(center = (550,330))
gd_editor_rect = geometry_editor.get_rect(center = (775, 300))
cedit_rect = cEdit.get_rect(center = (225,290))
demonface = pygame.image.load('img/sed.png')
font = pygame.font.SysFont("lucidaconsole", 20)


start_screen = [geometry_bg, gdpb_rect, geometry_pb, geometry_editor, gd_editor_rect, cEdit, cedit_rect]
if not start:
    start_screen[0]
# square block face is main character the icon of the window is the block face
avatar = pygame.image.load("img/avatar.jpg", "avatar.png")  # load the main character
pygame.display.set_icon(avatar)
#  this surface has an alpha value with the colors, so the player trail will fade away using opacity
alpha_surf = pygame.Surface(screen.get_size(), pygame.SRCALPHA)

# sprite groups
player_sprite = pygame.sprite.Group()
elements = pygame.sprite.Group()

# images
spike = pygame.image.load("img/images/obj-spike.png")
spike = resize(spike)
coin = pygame.image.load("img/images/coin.png")
coin = pygame.transform.smoothscale(coin, (32, 32))
block = pygame.image.load("img/images/block_1.png")
block = pygame.transform.smoothscale(block, (32, 32))
orb = pygame.image.load("img/images/orb-yellow.png")
orb = pygame.transform.smoothscale(orb, (32, 32))
trick = pygame.image.load("img/images/obj-breakable.png")
trick = pygame.transform.smoothscale(trick, (32, 32))

#  ints
fill = 0
num = 0
CameraX = 0
attempts = 0
coins = 0
angle = 0
level = 0

# list
particles = []
orbs = []
win_cubes = []

# initialize level with

# set window title suitable for game
pygame.display.set_caption('Pydash: Geometry Dash in Python')

# initialize the font variable to draw text later
text = font.render('image', False, (255, 255, 0))

# music
music = pygame.mixer_music.load("img/music/Corrison.mp3")
pygame.mixer_music.play()


# show tip on start and on death
tip = font.render("tip: tap and hold for the first few seconds of the level", True, BLUE)


def player_controls(event1, event2):
    event1 = pygame.MOUSEBUTTONDOWN
    if keys[pygame.K_SPACE]:
        print('jump')
    event2 = keys
    if keys[pygame.K_UP]:
        print('jump')
    return player_controls

class Draw(pygame.sprite.Sprite):
    """parent class to all obstacle classes; Sprite class"""

    def __init__(self, image, pos, *groups):
        super().__init__(*groups)
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)

def eval_outcome(won: bool, died: bool):
    """simple function to run the win or die screen after checking won or died"""
    # if won:
    #     won_screen()
    # if died:
    #     death_screen()
    
'''PLAYER/SELF'''
class Player(pygame.sprite.Sprite):
    """Class for player. Holds update method, win and die variables, collisions and more."""
    win: bool
    died: bool

    def __init__(self, image, platforms, pos, *groups):
        """
        :param image: block face avatar
        :param platforms: obstacles such as coins, blocks, spikes, and orbs
        :param pos: starting position
        :param groups: takes any number of sprite groups.
        """
        super().__init__(*groups)
        self.onGround = False  # player on ground?
        self.platforms = platforms  # obstacles but create a class variable for it
        self.died = False  # player died?
        self.win = False  # player beat level?

        self.image = pygame.transform.smoothscale(image, (32, 32))
        self.rect = self.image.get_rect(center=pos)  # get rect gets a Rect object from the image
        self.jump_amount = 10  # jump strength
        self.particles = []  # player trail
        self.isjump = False  # is the player jumping?
        self.vel = Vector2(0, 0)  # velocity starts at zero

 
    '''Player movement'''

"""WAITTTT"""
class Platform(Draw):
    """block"""

    def __init__(self, image, pos, *groups):
        super().__init__(image, pos, *groups)


class Spike(Draw):
    """spike"""

    def __init__(self, image, pos, *groups):
        super().__init__(image, pos, *groups)


class Coin(Draw):
    """coin. get 6 and you win the game"""

    def __init__(self, image, pos, *groups):
        super().__init__(image, pos, *groups)


class Orb(Draw):
    """orb. click space or up arrow while on it to jump in midair"""

    def __init__(self, image, pos, *groups):
        super().__init__(image, pos, *groups)


class Trick(Draw):
    """block, but its a trick because you can go through it"""

    def __init__(self, image, pos, *groups):
        super().__init__(image, pos, *groups)


class End(Draw):
    "place this at the end of the level"

    def __init__(self, image, pos, *groups):
        super().__init__(image, pos, *groups)






while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.K_ESCAPE:
            print(input('Are you sure you want to leave?'))
            if event.type == pygame.K_KP_ENTER:
                pygame.quit()
                exit()
    keys = pygame.key.get_pressed()
    if game_active == False:    
        screen.blit(geometry_bg,(0,0))
        screen.blit(geometry_surface,(325,65))
        screen.blit(geometry_pb, gdpb_rect)
        screen.blit(cEdit, (200, 260))
        screen.blit(geometry_editor, (750, 260))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if gd_editor_rect.collidepoint(event.pos):
                screen.fill((150,0,0))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if cedit_rect.collidepoint(event.pos):
                screen.fill('Purple')
                screen.blit(playership, (400,300))
        # pygame.draw.rect(geometry_surface,'Black',geometry_rect, 700)
        

        """Game Menu Contront"""
    if event.type == pygame.MOUSEBUTTONDOWN:
            if gdpb_rect.collidepoint(event.pos):
                game_active = True
    if game_active == True:
        screen = screen2
        level_bg = pygame.image.load('img/ha.png')
        level1_rect = level_bg.get_rect(center = (500,275))
        screen.blit(level_bg, level1_rect)
        screen.blit(geometry_bg, (0,0))
        screen.blit(demonface, (300,130))
        geometry_surface2 = font2.render('Zodiac', False, WHITE)
        dificulty = font.render('Escapulator', False, WHITE, BLACK)
        screen.blit(geometry_surface2, (500,275))
        screen.blit(dificulty, (300,250))
        if keys[pygame.K_BACKSPACE]:
            game_active = False
        tips = font.render('Please press SPACE to play.', False, WHITE)
        screen.blit(tips, (500,200))
        '''Start of LEVEL Zodiac'''
        if keys[pygame.K_SPACE]:
            level1_active = True
    if level1_active == True:
        screen3 = True 
        zodiac_bg = pygame.image.load('img/GD background.jpg')
        screen.blit(zodiac_bg, (0,0))
        ALL_LEVELS_GROUND = pygame.image.load('img/Level_ground.png').convert_alpha()
        level1_ground_rect = ALL_LEVELS_GROUND.get_rect(bottomleft = (50,750))
        level1_ground_rect.x -= 50
        if level1_ground_rect.right <= -300:
            level1_ground_rect.left = 800
            print('yes')
        screen.blit(ALL_LEVELS_GROUND, level1_ground_rect)
        ZODIAC = [screen3, zodiac_bg, ALL_LEVELS_GROUND]
        

        
        



            


        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
    pygame.display.update()
    clock.tick(60)
    

    
    
    
    
    
def Zodiac():
    pass
def digitalDescent():
    pass