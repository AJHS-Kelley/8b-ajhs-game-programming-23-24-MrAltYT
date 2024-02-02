# Projekt M by Johnson Traevon 2.53pm 2/1/24 v0.2.5
import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('A.R.G.U.S')
clock = pygame.time.Clock()

sky_surface = pygame.image.load('img/blossom.jpg')
ground_surface = pygame.image.load('img/ground.jpg')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,225))
    # Draw all our elements
    # Update everything
    pygame.display.update()
    clock.tick(60)
























