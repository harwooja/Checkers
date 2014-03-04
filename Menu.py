import pygame,sys,Constants
from pygame.locals import *

buttons = []
buttons.append((0,"standardButton",510,100,275,69))
buttons.append((0,"customButton",510,350,275,69))
buttons.append((1,"white",510,100,42,42))
buttons.append((1,"black",510,200,42,42))
buttons.append((1,"kingwhite",510,300,42,42))
buttons.append((1,"kingblack",510,400,42,42))



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
