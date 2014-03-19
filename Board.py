import pygame, sys, Constants, GameState
from pygame.locals import *

TOPLEFT = 10
WIDTH = 480






boardState = []

for m in range (8):
    boardState.append([])
    for z in range(8):
        boardState[m].append("Blank")  

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
    green = 27,245,27
    yellow = 245,245,27

    for index in range (8):
        for j in range(8):
            
            if boardState[index][j] == "B" :
                    
                    yCord = 10 + ((index*60)+9)
                    xCord = 20 + ((j*60))
                    window.blit(Bsprite,(xCord,yCord))

            elif boardState[index][j] == "W" :
                    yCord = 10 + ((index*60)+9)
                    xCord = 20 + (j*60)
                    window.blit(Wsprite,(xCord,yCord))

            elif boardState[index][j] == "KB" :
                    yCord = 10 + ((index*60)+9)
                    xCord = 20 + (j*60)
                    window.blit(BKsprite,(xCord,yCord))

            elif boardState[index][j] == "KW" :
                    yCord = 10 + ((index*60)+9)
                    xCord = 20 + (j*60)
                    window.blit(WKsprite,(xCord,yCord))
                    
            elif boardState[index][j] == "selected":
                ycord = 10 + (index*60)
                xcord = 10 + (j*60)
                pygame.draw.rect(window,green,Rect((xcord,ycord),(60,60)))

            elif boardState[index][j] == "legal":
                ycord = 10 + (index*60)
                xcord = 10 + (j*60)
                pygame.draw.rect(window,red,Rect((xcord,ycord),(60,60)))
                
def checkLegalMoves(coord):
    return []

def checkAttackMoves(coord):
    return []
    
def selectTile(x, y):

    s = GameState.s

    if (s.getGameState() == 1): #Setup phase
        
        checkC = x + y

        if (checkC % 2 != 0):  #they clicked a white tile
            boardState[x][y] = s.getSelectedCustomPiece()
            
    elif (s.getGameState() == 2): #Game phase
        if not GameState.s.getSelectedTile(): #A tile has not currently been picked up
            moves = checkLegalMoves((x,y)) #checking if the piece can be picked up
            st = GameState.s
            if moves:
                st.setSelectedTile((x,y))
                st.setLegalMoves(m)
                pType = boardState[x][y]
                if pType == "B":
                    st.setPickedUpPiece("black")
                elif pType == "W":
                    st.setPickedUpPiece("white")
                elif pType == "KW":
                    st.setPickedUpPiece("kingwhite")
                elif pType == "KB":
                    st.setPickedUpPiece("kingblack")
                boardState[x][y] = "selected"
                for m in moves:
                    boardState[m[0]][m[1]] = "legal"
        
                
                    
        else:
            state = GameState.s
            moves = state.getLegalMoves()
            for m in moves:
                if (x,y) == (m[0],m[1]):
                    print "To do later"
                

        
            


def insertPiece(a, b, piece):
    boardState[a][b] = piece

def deletePiece(a, b):
    boardState[a][b] = "BLANK"


    







        

