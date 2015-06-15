#!/usr/bin/env python
 
background_image_filename = '/Users/mayaoyu/Dropbox/Python/pygame/pokemon.jpg'
mouse_image_filename = '/Users/mayaoyu/Dropbox/Python/pygame/fugu.png'
 
import pygame
from pygame.locals import *
#import several basic functions and parameters
from sys import exit
#borrow exit function from sys to exit
 
pygame.init()
#initiate pygame
 
screen = pygame.display.set_mode((640, 480), 0, 32)
# set up a screen for game
pygame.display.set_caption("Hello, World!")
# set up name
 
background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
# load images
 
while True:
# game loop
 
    for event in pygame.event.get():
        if event.type == QUIT:
            # if recieve quit then exit
            exit()
 
    screen.blit(background, (0,0))
    #draw background
 
    x, y = pygame.mouse.get_pos()
    # get mouse position
    #  x-= mouse_cursor.get_width() / 2
    #  y-= mouse_cursor.get_height() / 2
    #  
    screen.blit(mouse_cursor, (x, y))
    # draw mouse cursor
 
    pygame.display.update()
    # update display
