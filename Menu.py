import pygame,sys,Constants
from pygame.locals import *

#drawSetup function
def drawSetup(window):
    size = Constants.SIZE
    button1 = pygame.image.load("MenuButton.png").convert()
    button2 = pygame.image.load("MenuButton.png").convert()

    bg = pygame.transform.scale(bg, size)
    window.blit(button1,(100,100))
    window.blit(button2,(100,400))
    
