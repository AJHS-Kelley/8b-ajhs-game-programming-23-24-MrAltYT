# 8B Geometry Dash Sponsored by RobTop, Created by Johnson Traveon and Christain Ortiz v0.8.2
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
# BINTRICALIZATIONALISM

def player_controls(event1, event2, keys):
    event1 = pygame.MOUSEBUTTONDOWN
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        print('jump')
    event2 = keys
    





pygame.init()
# SENSAGREGORY INSTINCTUAL HOLOSCHLATERIAL

screen = pygame.display.set_mode((1152,648))

    
pygame.display.set_caption('Geometry Dash')
clock = pygame.time.Clock()



geometry_bg = pygame.image.load('img/Gd background.jpg').convert_alpha()
cEdit = pygame.image.load('img/GD CEdit.jpg').convert_alpha()
geometrydash_font = pygame.font.Font('img/Seagram.ttf', 80)
geometry_surface = geometrydash_font.render('geometry dash', True, 'Green').convert_alpha()
geometry_editor = pygame.image.load('img/editor button.jpg').convert_alpha()

# geometry_rect = geometry_surface.get_rect(center = (400,150))

geometry_pb = pygame.image.load('img/Gd play.jpg').convert_alpha()
gdpb_rect = geometry_pb.get_rect(center = (520,260))

def start_screen():
    """main menu. option to switch level, and controls guide, and game overview."""
    global level
    if not start:
        screen.fill('BLACK')
        if pygame.key.get_pressed()[pygame.K_1]:
            level = 0
        if pygame.key.get_pressed()[pygame.K_2]:
            level = 1

        welcome = geometrydash_font.render(f"Welcome to Pydash. choose level({level + 1}) by keypad", True, 'WHITE')

        controls = player_controls.font.render("Controls: jump: Space/Up exit: Esc", True, 'GREEN')

        screen.blit(welcome, (100, 100))
        screen.blit(controls, (100, 400))
        screen.blit(tip, (100, 500))

        level_memo = zodiac_Dis.render(f"Level {level + 1}.", True, (255, 255, 0)).convert_alpha()
        screen.blit(level_memo, (100, 200))





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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
        if g.collidepoint(event.pos):
            print('player touched the pb')
        # if mouse_pos.collidepoint(geometry_pb):
        #     print('Player mouse is on Play button')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    pygame.display.update()
    clock.tick(60)
    

    
    
    
    
    
def Zodiac():
    pass
def digitalDescent():
    pass