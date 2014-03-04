import pygame,sys,Constants
from pygame.locals import *

#drawSetup function
def drawSetup(window):
    size = Constants.SIZE
    button1 = pygame.image.load("standardButton.png").convert_alpha()
    button2 = pygame.image.load("customButton.png").convert_alpha()

    #bg = pygame.transform.scale(bg, size)
    window.blit(button1,(510,100))
    window.blit(button2,(510,350))
    
