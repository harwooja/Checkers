import pygame, sys, Constants
from pygame.locals import *


def drawBoard(window):
    size = Constants.SIZE
    black = 0,0,0
    red = 245,27,27
    redp = 252,3,3
    goldp = 209,227,43
    white = 255,255,255
    bg = pygame.image.load("back.jpg")
    bg = pygame.transform.scale(bg, size)
    window.blit(bg,(0,0))
    pygame.draw.rect(window,red,Rect((5,5), (490,490)))
    pygame.draw.rect(window,black,Rect((10,10),(480,480)))



def debug():

    pygame.init()
    
    done = False
    size = Constants.SIZE
    window = pygame.display.set_mode(size)
    pygame.display.set_caption("Checkers")
    clock = pygame.time.Clock()

    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        drawBoard(window,size)
        pygame.display.flip()
        clock.tick(60) #60 fps


#debug()
    







        

