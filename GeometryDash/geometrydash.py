# 8B Geometry Dash Sponsored by RobTop, Created by Johnson Traveon v0.2
import pygame
from sys import exit
import random

pygame.init()
screen = pygame.display.set_mode((1152,648))
pygame.display.set_caption('Geometry Dash')
clock = pygame.time.Clock()
geometrydash_font = pygame.font.Font('oxygene-1/OXYGENE1.ttf', 40)
geometry_surface = geometrydash_font.render('geometry dash', False, 'Green')
geometry_rect = geometry_surface.get_rect(center = (375,150))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(geometry_surface,(375,150))
    pygame.draw.rect(geometry_surface, 'White',geometry_rect)
    
    pygame.display.update()
    clock.tick(60)