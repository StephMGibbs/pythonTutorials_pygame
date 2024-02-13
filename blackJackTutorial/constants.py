'''
Created on Feb 12, 2024

@author: StephMGibbs

#Tutorial: https://medium.com/nerd-for-tech/creating-blackjack-game-with-python-80a3b87b1995
#Constants - script file w/ logic part of the game, pygame GUI, etc.
'''
import pygame as pygame 
#install pygame with pip in terminal
#pydev recognize pygame: Window -> Preferences -> PyDev -> Interpreter -> Python Interpreter (Packages tab look for Pygame library)
    #add manually if not there.



display_width = 900
display_height = 700

background_color = (34, 139, 34)
grey = (220, 220, 220)
black = (0, 0, 0)
green = (0, 200, 0)
red = (255, 0, 0)
light_slat = (119, 136, 153)
dark_slat = (47, 79, 79)
dark_red = (255, 0, 0)

pygame.init()
font = pygame.font.SysFont("Arial", 20)
textfont = pygame.font.SysFont('Comic Sans MS', 35)
game_end = pygame.font.SysFont('dejavusans', 100)
blackjack = pygame.font.SysFont('roboto', 70)

SUITS = ['C', 'S', 'H', 'D']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
