# Projekt M by Johnson Traevon 2.53pm 2/1/24 v0.5.5
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('A.R.G.U.S')
clock = pygame.time.Clock()
test_font = pygame.font.Font('img/Seagram_tfb 2.ttf', 33)

sky_surface = pygame.image.load('img/blossom.jpg').convert_alpha()
ground_surface = pygame.image.load('img/ground.jpg').convert_alpha()

score_surf = test_font.render('Welcome to Oshi No Ko!!', True, 'cyan')
score_rect = score_surf.get_rect(center = (400,50))

Stars_surf = pygame.image.load('img/Star_Twins.gif').convert_alpha()
Stars_rect = Stars_surf.get_rect(bottomright = (600,300))

player_surf = pygame.image.load('img/AI.gif').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):                                                                                                                        
        #         print('collision')

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,225))
    screen.blit(score_surf,score_rect)
    Stars_rect.x -= 3
    if Stars_rect.right <= -300:
        Stars_rect.left = 800
    screen.blit(Stars_surf, Stars_rect)
    screen.blit(player_surf,player_rect)
    
    # if player_rect.colliderect(Stars_rect):
    #     print('collision')
    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint((mouse_pos)):
    #     print(pygame.mouse.get_pressed())

    # Draw all our elements
    # Update everything
    pygame.display.update()
    clock.tick(60)
























