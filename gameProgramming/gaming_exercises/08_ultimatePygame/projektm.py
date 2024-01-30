# Projekt M by Johnson Traevon 1:49pm 1/30/24 v0.1.5
import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption('A.R.G.U.S')
clock = pygame.time.Clock()

test_surface = pygame.Surface((600,400))
test_surface.fill('purple')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_surface,(0,0))
    # Draw all our elements
    # Update everything
    pygame.display.update()
    clock.tick(60)























