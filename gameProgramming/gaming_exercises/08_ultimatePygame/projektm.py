# Projekt M by Johnson Traevon 1:49pm 1/30/24 v0.1
import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800,400))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # Draw all our elements
    # Update everything
    pygame.display.update()
























