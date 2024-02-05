# Projekt M by Johnson Traevon 2.53pm 2/1/24 v0.3.5
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('A.R.G.U.S')
clock = pygame.time.Clock()
test_font = pygame.font.Font('img/Seagram_tfb 2.ttf', 33)

sky_surface = pygame.image.load('img/blossom.jpg')
ground_surface = pygame.image.load('img/ground.jpg')
test_surface = test_font.render('Welcome to Oshi No Ko!!', True, 'cyan')

ai_surface = pygame.image.load('img/AI.gif')
ai_x_pos = 400
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,225))
    screen.blit(test_surface,(200,50))
    ai_x_pos -= 3
    if ai_x_pos <= -100:
        ai_x_pos = 400
    screen.blit(ai_surface,(ai_x_pos,75))

    # Draw all our elements
    # Update everything
    pygame.display.update()
    clock.tick(60)
























