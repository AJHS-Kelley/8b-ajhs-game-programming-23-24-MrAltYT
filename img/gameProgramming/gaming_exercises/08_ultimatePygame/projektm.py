# Projekt M by Johnson Traevon 2.53pm 2/1/24 v0.4
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('A.R.G.U.S')
clock = pygame.time.Clock()
test_font = pygame.font.Font('img/Seagram_tfb 2.ttf', 33)

sky_surface = pygame.image.load('img/blossom.jpg').convert_alpha()
ground_surface = pygame.image.load('img/ground.jpg').convert_alpha()
test_surface = test_font.render('Welcome to Oshi No Ko!!', True, 'cyan')

Stars = pygame.image.load('img/Star_Twins.gif').convert_alpha()
Stars_x_pos = 800

player_surf = pygame.image.load('img/AI.gif').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,250))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,225))
    screen.blit(test_surface,(200,50))
    Stars_x_pos -= 3
    if Stars_x_pos <= -300:
        Stars_x_pos = 800
    screen.blit(Stars,(Stars_x_pos,200))
    screen.blit(player_surf,player_rect)
    

    # Draw all our elements
    # Update everything
    pygame.display.update()
    clock.tick(60)
























