import pygame
import os

width = 810
height = 810
rows = 9
cols = 9
square_size = width//cols

# rgb colors used
global red
red = (255, 0, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
grey = (128,128,128)

CROWN = pygame.transform.scale(pygame.image.load(os.path.join('pics/crown.png')), (44, 25))

