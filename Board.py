import pygame, sys, Constants
from pygame.locals import *

Bsprite = pygame.image.load('black.png')
Wsprite = pygame.image.load('white.png')
BKsprite = pygame.image.load('kingblack.png')
WKsprite = pygame.image.load('kingwhite.png')


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
    pygame.draw.rect(window,black,Rect((5,5), (490,490)))
    pygame.draw.rect(window,red,Rect((10,10),(480,480)))

    
    x = 10;
    for index in range (4):
        
        y = 10
        for j in range(4):
            pygame.draw.rect(window,white,Rect((x,y),(60,60)))
            y = y +120
            
                                               
        
        x = x + 120



    x = 70;
    for index in range (4):
       
        y = 70
        for j in range(4):
            
            pygame.draw.rect(window,white,Rect((x,y),(60,60)))
            y = y +120
                                               
        
        x = x + 120
    

def drawPieces(array):
    xCord = 10
    yCord = 10

    for index in range (7):
        for j in range(7):
            if x[index][j] == "B" :
                    xCord = xCord + ((index*60)+9)
                    yCord = yCord + ((j*60)
                    pygame.draw.rect(window,white,Rect((xCord,yCord),(42,42)))

            elif x[index][j] == "W" :
                    xCord = xCord + (index*60)
                    yCord = yCord + (j*60)

            elif x[index][j] == "KB" :
                    xCord = xCord + (index*60)
                    yCord = yCord + (j*60)

            elif x[index][j] == "KW" :
                    xCord = xCord + (index*60)
                    yCord = yCord + (j*60)
                
                
            
    



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
                
        drawBoard(window)
        pygame.display.flip()
        clock.tick(60) #60 fps



debug()

    







        

