import pygame, sys, Constants
from pygame.locals import *

TOPLEFT = 10
WIDTH = 480






boardState = []

for m in range (8):
    boardState.append([])
    for z in range(8):
        boardState[m].append("W")  

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


    drawPieces(window)


    
    
    
    
    

def drawPieces(window):

    Bsprite = pygame.image.load('black.png').convert_alpha()
    Wsprite = pygame.image.load('white.png').convert_alpha()
    BKsprite = pygame.image.load('kingblack.png').convert_alpha()
    WKsprite = pygame.image.load('kingwhite.png').convert_alpha()
    xCord = 10
    yCord = 10

    for index in range (8):
        for j in range(8):
            
            if boardState[index][j] == "B" :
                    
                    xCord = 10 + ((index*60)+9)
                    yCord = 20 + ((j*60))
                    window.blit(Bsprite,(xCord,yCord))

            elif boardState[index][j] == "W" :
                    xCord = 10 + ((index*60)+9)
                    yCord = 20 + (j*60)
                    window.blit(Wsprite,(xCord,yCord))

            elif boardState[index][j] == "KB" :
                    xCord = 10 + ((index*60)+9)
                    yCord = 20 + (j*60)
                    window.blit(BKsprite,(xCord,yCord))

            elif boardState[index][j] == "KW" :
                    xCord = 10 + ((index*60)+9)
                    yCord = 20 + (j*60)
                    window.blit(WKsprite,(xCord,yCord))
                
                
            
    



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



#debug()

    







        

