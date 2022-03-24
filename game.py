import pygame
import time
import random

pygame.init()

#make the colors needed for the game
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#screen size
display_width = 800
display_height = 800

#initializes screen
display = pygame.display.set_mode((display_width, display_height))
display.fill(black)
pygame.display.set_caption('Game')

#game clock
clock = pygame.time.Clock()

#game contents
def gameLoop():
    game_over = False
    game_close = False

    while not game_over:
    
        pygame.quit()
        quit()

gameLoop()
