import pygame,sys,Constants
from pygame.locals import *






#drawSetup function
def drawSetup(window):
    size = Constants.SIZE
    button1 = pygame.image.load("standardButton.png").convert_alpha()
    button2 = pygame.image.load("customButton.png").convert_alpha()

    window.blit(button1,(510,100))
    window.blit(button2,(510,350))

def drawCustomSetup(window):
    size = Constants.SIZE
    piece_W = pygame.image.load("white.png").convert_alpha()
    piece_B = pygame.image.load("black.png").convert_alpha()
    piece_WK = pygame.image.load("kingwhite.png").convert_alpha()
    piece_BK = pygame.image.load("kingblack.png").convert_alpha()

    window.blit(piece_W, (510,100))
    window.blit(piece_WK, (510,200))
    window.blit(piece_B, (510,300))
    window.blit(piece_BK, (510,400))


def getButton():

    return buttons    
