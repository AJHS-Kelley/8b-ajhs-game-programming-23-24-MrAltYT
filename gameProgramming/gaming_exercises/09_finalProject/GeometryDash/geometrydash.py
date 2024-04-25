# 8B Geometry Dash Sponsored by RobTop, Created by Johnson Traveon and Christain Ortiz v0.8.4.7

# Kelley -- 04/25/24 -- Code Review 
# Create 'HEADERS' for each section of your code, such as 'Controls' or 'Screen Information' to keep the data organized. 
# Create a variable to track the current game level, use if and screen.blit() to display the correct level using that variable. 

import pygame, csv, os, random
from sys import exit
from pygame.math import Vector2
from pygame.draw import rect

'''VARIABLESSS'''
screen1 = True
screen2 = False
screen3 = False
particles = []
orbs = []
win_cubes = []
resolution = 1


def eval_outcome(won: bool, died: bool):
    """simple function to run the win or die screen after checking won or died"""
    # if won:
    #     won_screen()
    # if died:
    #     death_screen()
    
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
screen2 = '' #LEVEL PICKER
screen3 = "" #LEVEL
GRAVITY = Vector2(0, 0.86)

# BINTRICALIZATIONALISM

def player_controls(event1, event2, keys):
    event1 = pygame.MOUSEBUTTONDOWN
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        print('jump')
    event2 = keys
    if keys[pygame.K_UP]:
        print('jump')
    return player_controls, keys

class Draw(pygame.sprite.Sprite):
    """parent class to all obstacle classes; Sprite class"""

    def __init__(self, image, pos, *groups):
        super().__init__(*groups)
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)



pygame.init()
# SENSAGREGORY INSTINCTUAL HOLOSCHLATERIAL

screen = pygame.display.set_mode((x,y))
alpha_surf = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    
pygame.display.set_caption('Geometry Dash')
clock = pygame.time.Clock()

game_active = True

geometry_bg = pygame.image.load('img/Gd background.jpg').convert_alpha()
cEdit = pygame.image.load('img/GD CEdit.jpg').convert_alpha()
font = pygame.font.Font('img/Seagram.ttf', 80)
tip = font.render("tip: tap and hold for the first few seconds of the level", True, BLUE)
geometry_surface = font.render('geometry dash', True, 'Green').convert_alpha()
geometry_editor = pygame.image.load('img/editor button.png').convert_alpha()
playership = pygame.image.load('img/bird_108.png').convert_alpha()

# geometry_rect = geometry_surface.get_rect(center = (400,150))

geometry_pb = pygame.image.load('img/Gd play.jpg').convert_alpha()
gdpb_rect = geometry_pb.get_rect(center = (550,300))
gd_editor_rect = geometry_editor.get_rect(center = (775, 300))
cedit_rect = cEdit.get_rect(center = (225,290))


class Player(pygame.sprite.Sprite):
    """Class for player. Holds update method, win and die variables, collisions and more."""
    win: bool
    died: bool

    def __init__(self, image, platforms, pos, *groups):
        """
        :param image: block face avatar
        :param platforms: obstacles such as coins, blocks, spikes, and orbs
        :param pos: starting position
        :param groups: takes any number of sprite groups.
        """
        super().__init__(*groups)
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

    def draw_particle_trail(self, x, y, color=(255, 255, 255)):
        """draws a trail of particle-rects in a line at random positions behind the player"""

        self.particles.append(
                [[x - 5, y - 8], [random.randint(0, 25) / 10 - 1, random.choice([0, 0])],
                 random.randint(5, 8)])

        for particle in self.particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.5
            particle[1][0] -= 0.4
            rect(alpha_surf, color,
                 ([int(particle[0][0]), int(particle[0][1])], [int(particle[2]) for i in range(2)]))
            if particle[2] <= 0:
                self.particles.remove(particle)

    def collide(self, yvel, platforms):
        global coins

        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                """pygame sprite builtin collision method,
                sees if player is colliding with any obstacles"""
                if isinstance(p, Orb) and ([pygame.K_UP] or [pygame.K_SPACE]):
                    pygame.draw.circle(alpha_surf, (255, 255, 0), p.rect.center, 18)
                    screen.blit(pygame.image.load("images/editor-0.9s-47px.gif"), p.rect.center)
                    self.jump_amount = 12  # gives a little boost when hit orb
                    self.jump()
                    self.jump_amount = 10  # return jump_amount to normal

                if isinstance(p, End):
                    self.win = True

                if isinstance(p, Spike):
                    self.died = True  # die on spike

                if isinstance(p, Coin):
                    # keeps track of all coins throughout the whole game(total of 6 is possible)
                    coins += 1

                    # erases a coin
                    p.rect.x = 0
                    p.rect.y = 0

                if isinstance(p, Platform):  # these are the blocks (may be confusing due to self.platforms)

                    if yvel > 0:
                        """if player is going down(yvel is +)"""
                        self.rect.bottom = p.rect.top  # dont let the player go through the ground
                        self.vel.y = 0  # rest y velocity because player is on ground

                        # set self.onGround to true because player collided with the ground
                        self.onGround = True

                        # reset jump
                        self.isjump = False
                    elif yvel < 0:
                        """if yvel is (-),player collided while jumping"""
                        self.rect.top = p.rect.bottom  # player top is set the bottom of block like it hits it head
                    else:
                        """otherwise, if player collides with a block, he/she dies."""
                        self.vel.x = 0
                        self.rect.right = p.rect.left  # dont let player go through walls
                        self.died = True

    def jump(self):
        self.vel.y = -self.jump_amount  # players vertical velocity is negative so ^

    def update(self):
        """update player"""
        if self.isjump:
            if self.onGround:
                """if player wants to jump and player is on the ground: only then is jump allowed"""
                self.jump()

        if not self.onGround:  # only accelerate with gravity if in the air
            self.vel += GRAVITY  # Gravity falls

            # max falling speed
            if self.vel.y > 100: self.vel.y = 100

        # do x-axis collisions
        self.collide(0, self.platforms)

        # increment in y direction
        

        # assuming player in the air, and if not it will be set to inversed after collide
        self.onGround = False

        # do y-axis collisions
        self.collide(self.vel.y, self.platforms)

        # check if we won or if player won
        eval_outcome(self.win, self.died)
"""WAITTTT"""
class Platform(Draw):
    """block"""

    def __init__(self, image, pos, *groups):
        super().__init__(image, pos, *groups)


class Spike(Draw):
    """spike"""

    def __init__(self, image, pos, *groups):
        super().__init__(image, pos, *groups)


class Coin(Draw):
    """coin. get 6 and you win the game"""

    def __init__(self, image, pos, *groups):
        super().__init__(image, pos, *groups)


class Orb(Draw):
    """orb. click space or up arrow while on it to jump in midair"""

    def __init__(self, image, pos, *groups):
        super().__init__(image, pos, *groups)


class Trick(Draw):
    """block, but its a trick because you can go through it"""

    def __init__(self, image, pos, *groups):
        super().__init__(image, pos, *groups)


class End(Draw):
    "place this at the end of the level"

    def __init__(self, image, pos, *groups):
        super().__init__(image, pos, *groups)


def blitRotate(surf, image, pos, originpos: tuple, angle: float):
    """
    rotate the player
    :param surf: Surface
    :param image: image to rotate
    :param pos: position of image
    :param originpos: x, y of the origin to rotate about
    :param angle: angle to rotate
    """
    # calcaulate the axis aligned bounding box of the rotated image
    w, h = image.get_size()
    box = [Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(angle) for p in box]

    # make sure the player does not overlap, uses a few lambda functions(new things that we did not learn about number1)
    min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])
    # calculate the translation of the pivot
    pivot = Vector2(originpos[0], -originpos[1])
    pivot_rotate = pivot.rotate(angle)
    pivot_move = pivot_rotate - pivot

    # calculate the upper left origin of the rotated image
    origin = (pos[0] - originpos[0] + min_box[0] - pivot_move[0], pos[1] - originpos[1] - max_box[1] + pivot_move[1])

    # get a rotated image
    rotated_image = pygame.transform.rotozoom(image, angle, 1)

    # rotate and blit the image
    surf.blit(rotated_image, origin)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.K_ESCAPE:
            print(input('Are you sure you want to leave?'))
            if event.type == pygame.K_KP_ENTER:
                pygame.quit()
                exit()
    
    if game_active:
        
        screen.blit(geometry_bg,(0,0))
        screen.blit(geometry_surface,(325,65))
        screen.blit(geometry_pb, (480,260))
        screen.blit(cEdit, (200, 260))
        screen.blit(geometry_editor, (750, 260))
        # pygame.draw.rect(geometry_surface,'Black',geometry_rect, 700)
        
        mouse_pos = pygame.mouse.get_pos()


        
        """"Game Menu Controls"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if gdpb_rect.collidepoint(event.pos):
               geometry_pb = pygame.transform.rotozoom(geometry_editor,60, 1)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if gd_editor_rect.collidepoint(event.pos):
                screen.fill((150,0,0))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if cedit_rect.collidepoint(event.pos):
                screen.fill('Purple')
                screen.blit(playership, (400,300))
            


        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    pygame.display.update()
    clock.tick(60)
    

    
    
    
    
    
def Zodiac():
    pass
def digitalDescent():
    pass