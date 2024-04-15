# 8B Geometry Dash Sponsored by RobTop, Created by Johnson Traveon and Christain Ortiz v0.8.4
import pygame
from sys import exit
import random
from pygame.math import Vector2
from pygame.draw import rect
import csv
import os


resolution = 1
if resolution == 1:
    x = 1152
    y = 648
elif resolution == 0:
    x = 800
    y = 600
else:
    print('This game only runs on Resolution 0 or 1.')
gameplay = 2
if gameplay == 2:
    pass
welcome = 'geometry dash'
start = False
zodiac_Dis = 'top 1 hardest demon from 2018 - 2023'
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# BINTRICALIZATIONALISM

def player_controls(event1, event2, keys):
    event1 = pygame.MOUSEBUTTONDOWN
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        print('jump')
    event2 = keys
    if keys[pygame.K_UP]:
        print('jump')
    return player_controls





pygame.init()
# SENSAGREGORY INSTINCTUAL HOLOSCHLATERIAL

screen = pygame.display.set_mode((x,y))

    
pygame.display.set_caption('Geometry Dash')
clock = pygame.time.Clock()



geometry_bg = pygame.image.load('img/Gd background.jpg').convert_alpha()
cEdit = pygame.image.load('img/GD CEdit.jpg').convert_alpha()
font = pygame.font.Font('img/Seagram.ttf', 80)
tip = font.render("tip: tap and hold for the first few seconds of the level", True, BLUE)
geometry_surface = font.render('geometry dash', True, 'Green').convert_alpha()
geometry_editor = pygame.image.load('img/editor button.png').convert_alpha()

# geometry_rect = geometry_surface.get_rect(center = (400,150))

geometry_pb = pygame.image.load('img/Gd play.jpg').convert_alpha()
gdpb_rect = geometry_pb.get_rect(center = (520,260))
gd_editor_rect = geometry_editor.get_rect(center = (750, 260))
cedit_rect = cEdit.get_rect(center = (200,260))

def start_screen():
    """main menu. option to switch level, and controls guide, and game overview."""
    global level
    if not start:
        screen.fill('BLACK')
        if pygame.key.get_pressed()[pygame.K_1]:
            level = 0
        if pygame.key.get_pressed()[pygame.K_2]:
            level = 1

        welcome = font.render(f"Welcome to Pydash. choose level({level + 1}) by keypad", True, 'WHITE')

        controls = player_controls.font.render("Controls: jump: Space/Up exit: Esc", True, 'GREEN')

        screen.blit(welcome, (100, 100))
        screen.blit(controls, (100, 400))
        screen.blit(tip, (100, 500))

        level_memo = font.render(f"Level {level + 1}.", True, (255, 255, 0)).convert_alpha()
        screen.blit(level_memo, (100, 200))

def __init__(self, image, platforms, pos, *groups):
    """
        :param image: block face avatar
        :param platforms: obstacles such as coins, blocks, spikes, and orbs
        :param pos: starting position
        :param groups: takes any number of sprite groups.
    """
    class super():__init__(*groups)
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

















while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.K_ESCAPE:
            print(input('Are you sure you want to leave?'))
            if event.type == pygame.K_KP_ENTER:
                pygame.quit()
                exit()
            
            
    screen.blit(geometry_bg,(0,0))
    screen.blit(geometry_surface,(325,65))
    screen.blit(geometry_pb, (480,260))
    screen.blit(cEdit, (200, 260))
    screen.blit(geometry_editor, (750, 260))
    # pygame.draw.rect(geometry_surface,'Black',geometry_rect, 700)
    
    mouse_pos = pygame.mouse.get_pos()
    # if gdpb_rect.collidepoint((mouse_pos)):
    #     print(pygame.mouse.get_pressed())
    # if event.type == pygame.MOUSEBUTTONDOWN:
    #     print('player is choosing a level')
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        if gdpb_rect.collidepoint(event.pos):
            print('player touched the pb')
    if event.type == pygame.MOUSEBUTTONDOWN:
        if gd_editor_rect.collidepoint(event.pos):
            print('Player Touched the editor button')
    if event.type == pygame.MOUSEBUTTONDOWN:
        if cedit_rect.collidepoint(event.pos):
            print('Player Touched the Character Editor button')
           


 

        # if mouse_pos.collidepoint(geometry_pb):
        #     print('Player mouse is on Play button')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    pygame.display.update()
    clock.tick(60)
    

    
    
    
    
    
def Zodiac():
    pass
def digitalDescent():
    pass