# 8B Geometry Dash Sponsored by RobTop, Created by Johnson Traveon and Christain Ortiz v0.5S
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
pygame.init()
# SENSAGREGORY INSTINCTUAL HOLOSCHLATERIAL

screen = pygame.display.set_mode((1152,648))

    
pygame.display.set_caption('Geometry Dash')
clock = pygame.time.Clock()

geometry_bg = pygame.image.load('img/Gd background.jpg').convert_alpha()

geometrydash_font = pygame.font.Font('img/Seagram.ttf', 80)
geometry_surface = geometrydash_font.render('geometry dash', True, 'Green').convert_alpha()
# geometry_rect = geometry_surface.get_rect(center = (400,150))

geometry_pb = pygame.image.load('img/Gd play.jpg').convert_alpha()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(geometry_bg,(0,0))
    screen.blit(geometry_surface,(325,65))
    screen.blit(geometry_pb, (480,260))
    # pygame.draw.rect(geometry_surface,'Black',geometry_rect, 700)
    
    
    pygame.display.update()
    clock.tick(60)
    

    
    
    
    
    
def Zodiac():
    pass
def Deadlocked():
    pass