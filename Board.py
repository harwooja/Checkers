import pygame, sys, Constants, GameState
from pygame.locals import *

TOPLEFT = 10
WIDTH = 480






boardState = []

for m in range (8):
    boardState.append([])
    for z in range(8):
        boardState[m].append("BLANK")

def convStateToFile(a):
    if a == "B":
        return "black"
    elif a == "W":
        return "white"
    elif a == "KB":
        return "kingblack"
    elif a == "KW":
        return "kingwhite"

def convFileToState(a):
    if a == "black":
        return "B"
    elif a == "white":
        return "W"
    elif a == "kingblack":
        return "KB"
    elif a == "kingwhite":
        return "KW"

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
                pygame.draw.rect(window,yellow,Rect((xcord,ycord),(60,60)))
def cEmpty(r,c):
    if boardState == "BLANK":
        return True
    else:
        return False

def checkLegalMoves(coord,localBState = None, localCurrentPlayer = None):
    if not localBState:
        localBState = boardState
    if not localCurrentPlayer:
        localCurrentPlayer = GameState.s.getCurrentPlayer()
        
    
    locs = []
    row = coord[0]
    column = coord[1]
    t = localBState[row][column]
    color = "None"
    if t == "W" or t == "KW":
        color = "WHITE"
    elif t == "B" or t == "KB":
        color = "BLACK"
    if color == localCurrentPlayer:
        if t == "B":
            if row != 7:
                if column == 0:
                    if localBState[row+1][column+1] == "BLANK":
                        locs.append((row+1,column+1,None))
                        return locs
                    elif localBState[row+1][column+1] == "W" or localBState[row+1][column+1] == "KW":
                        return checkAttackMoves((row,column))
                    else:
                        return locs
                elif column == 7:
                    if localBState[row+1][column-1] == "BLANK":
                        locs.append((row+1,column-1,None))
                        return locs
                    elif localBState[row+1][column-1] == "W" or localBState[row+1][column-1] == "KW":
                        return checkAttackMoves((row,column))
                    else:
                        return locs
                else:
                    if localBState[row+1][column+1] == "BLANK":
                        locs.append((row+1,column+1,None))
                    if localBState[row+1][column-1] == "BLANK":
                        locs.append((row+1,column-1,None))
                    at = checkAttackMoves((row,column))
                    if at:
                        for moves in at:
                            locs.append(moves)
                    return locs
        if t == "W":
            if row != 0:
                if column == 0:
                    if localBState[row-1][column+1] == "BLANK":
                        locs.append((row-1,column+1,None))
                        return locs
                    elif localBState[row-1][column+1] == "B" or localBState[row-1][column+1] == "KB":
                        return checkAttackMoves((row,column))
                    else:
                        return locs
                elif column == 7:
                    if localBState[row-1][column-1] == "BLANK":
                        locs.append((row-1,column-1,None))
                        return locs
                    elif localBState[row-1][column-1] == "B" or localBState[row-1][column-1] == "KB":
                        return checkAttackMoves((row,column))
                    else:
                        return locs
                else:
                    
                    if localBState[row-1][column+1] == "BLANK":
                        
                        locs.append((row-1,column+1,None))
                    if localBState[row-1][column-1] == "BLANK":
                        locs.append((row-1,column-1,None))
                    at = checkAttackMoves((row,column))
                    if at:
                        for moves in at:
                            locs.append(moves)
                    return locs
        if t == "KB":
            if row == 0:
                if column == 0:
                    if localBState[row+1][column+1] == "BLANK":
                        locs.append((row+1,column+1,None))
                        return locs
                    elif localBState[row+1][column+1] == "W" or localBState[row+1][column+1] == "KW":
                        return checkAttackMoves((row,column))
                    else:
                        return locs
                elif column == 7:
                    if localBState[row+1][column-1] == "BLANK":
                        locs.append((row+1,column-1,None))
                        return locs
                    elif localBState[row+1][column-1] == "W" or localBState[row+1][column-1] == "KW":
                        return checkAttackMoves((row,column))
                    else:
                        return locs
                else:
                    if localBState[row+1][column+1] == "BLANK":
                        locs.append((row+1,column+1,None))
                    if localBState[row+1][column-1] == "BLANK":
                        locs.append((row+1,column-1,None))
                    at = checkAttackMoves((row,column))
                    if at:
                        for moves in at:
                            locs.append(moves)
                    return locs
            elif row == 7:
                if column == 0:
                    if localBState[row-1][column+1] == "BLANK":
                        locs.append((row+1,column+1,None))
                        return locs
                    elif localBState[row-1][column+1] == "W" or localBState[row+1][column+1] == "KW":
                        return checkAttackMoves((row,column))
                    else:
                        return locs
                elif column == 7:
                    if localBState[row-1][column-1] == "BLANK":
                        locs.append((row-1,column-1,None))
                        return locs
                    elif localBState[row-1][column-1] == "W" or localBState[row+1][column-1] == "KW":
                        return checkAttackMoves((row,column))
                    else:
                        return locs
                else:
                    if localBState[row-1][column+1] == "BLANK":
                        locs.append((row-1,column+1,None))
                    if localBState[row-1][column-1] == "BLANK":
                        locs.append((row-1,column-1,None))
                    at = checkAttackMoves((row,column))
                    if at:
                        for moves in at:
                            locs.append(moves)
                    return locs
            else:
                if column == 0:
                    if localBState[row+1][column+1] == "BLANK":
                        locs.append((row+1,column+1,None))
                    if localBState[row-1][column+1] == "BLANK":
                        locs.append((row-1,column+1,None))
                    at = checkAttackMoves((row,column))
                    if at:
                        for moves in at:
                            locs.append(moves)
                    return locs
                elif column == 7:
                    if localBState[row+1][column-1] == "BLANK":
                        locs.append((row+1,column-1,None))
                    if localBState[row-1][column-1] == "BLANK":
                        locs.append((row-1,column-1,None))
                    at = checkAttackMoves((row,column))
                    if at:
                        for moves in at:
                            locs.append(moves)
                    return locs
                else:
                    if localBState[row+1][column+1] == "BLANK":
                        locs.append((row+1,column+1,None))
                    if localBState[row+1][column-1] == "BLANK":
                        locs.append((row+1,column-1,None))
                    if localBState[row-1][column-1] == "BLANK":
                        locs.append((row-1,column-1,None))
                    if localBState[row-1][column+1] == "BLANK":
                        locs.append((row-1,column+1,None))
                    at = checkAttackMoves((row,column))
                    if at:
                        for moves in at:
                            locs.append(moves)
                    return locs
        if t == "KW":
            if row == 0:
                if column == 0:
                    if localBState[row+1][column+1] == "BLANK":
                        locs.append((row+1,column+1,None))
                        return locs
                    elif localBState[row+1][column+1] == "B" or localBState[row+1][column+1] == "KB":
                        return checkAttackMoves((row,column))
                    else:
                        return locs
                elif column == 7:
                    if localBState[row+1][column-1] == "BLANK":
                        locs.append((row+1,column-1,None))
                        return locs
                    elif localBState[row+1][column-1] == "B" or localBState[row+1][column-1] == "KB":
                        return checkAttackMoves((row,column))
                    else:
                        return locs
                else:
                    if localBState[row+1][column+1] == "BLANK":
                        locs.append((row+1,column+1,None))
                    if localBState[row+1][column-1] == "BLANK":
                        locs.append((row+1,column-1,None))
                    at = checkAttackMoves((row,column))
                    if at:
                        for moves in at:
                            locs.append(moves)
                    return locs
            elif row == 7:
                if column == 0:
                    if localBState[row-1][column+1] == "BLANK":
                        locs.append((row-1,column+1,None))
                        return locs
                    elif localBState[row-1][column+1] == "B" or localBState[row+1][column+1] == "KB":
                        return checkAttackMoves((row,column))
                    else:
                        return locs
                elif column == 7:
                    if localBState[row-1][column-1] == "BLANK":
                        locs.append((row-1,column-1,None))
                        return locs
                    elif localBState[row-1][column-1] == "B" or localBState[row-1][column-1] == "KB":
                        return checkAttackMoves((row,column))
                    else:
                        return locs
                else:
                    if localBState[row-1][column+1] == "BLANK":
                        locs.append((row-1,column+1,None))
                    if localBState[row-1][column-1] == "BLANK":
                        locs.append((row-1,column-1,None))
                    at = checkAttackMoves((row,column))
                    if at:
                        for moves in at:
                            locs.append(moves)
                    return locs
            else:
                if column == 0:
                    
                    if localBState[row+1][column+1] == "BLANK":
                        locs.append((row+1,column+1,None))
                    if localBState[row-1][column+1] == "BLANK":
                        locs.append((row-1,column+1,None))
                    at = checkAttackMoves((row,column))
                    if at:
                        for moves in at:
                            locs.append(moves)
                    return locs
                elif column == 7:
                    if localBState[row+1][column-1] == "BLANK":
                        locs.append((row+1,column-1,None))
                    if localBState[row-1][column-1] == "BLANK":
                        locs.append((row-1,column-1,None))
                    at = checkAttackMoves((row,column))
                    if at:
                        for moves in at:
                            locs.append(moves)
                    return locs
                else:
                    if localBState[row+1][column+1] == "BLANK":
                        locs.append((row+1,column+1,None))
                    if localBState[row+1][column-1] == "BLANK":
                        locs.append((row+1,column-1,None))
                    if localBState[row-1][column-1] == "BLANK":
                        locs.append((row-1,column-1,None))
                    if localBState[row-1][column+1] == "BLANK":
                        locs.append((row-1,column+1,None))
                    at = checkAttackMoves((row,column))
                    if at:
                        for moves in at:
                            locs.append(moves)
                    return locs

def checkAttackMoves(coord,localBState = None, localCurrentPlayer = None):
    if not localBState:
        localBState = boardState
    if not localCurrentPlayer:
        localCurrentPlayer = GameState.s.getCurrentPlayer()
        
    locs = []
    row = coord[0]
    column = coord[1]
    t = localBState[row][column]
    s = GameState.s
    color = "None"
    if t == "W" or t == "KW":
        color = "WHITE"
    elif t == "B" or t == "KB":
        color = "BLACK"
    if color == localCurrentPlayer:
        if t == "B":
            if row < 6:
                if column <2:
                    
                    if localBState[row+1][column+1] == "W" or localBState[row+1][column+1] == "KW":
                        if localBState[row+2][column+2] == "BLANK":
                            locs.append((row+2,column+2,(row+1,column+1)))
                            return locs
                    else:
                        return locs
                elif column > 5:
                    if localBState[row+1][column-1] == "W" or localBState[row+1][column-1] == "KW":
                        if localBState[row+2][column-2] == "BLANK":
                            locs.append((row+2,column-2,(row+1,column-1)))
                            return locs
                    else:
                        return locs
                else:
                    if localBState[row+1][column+1] == "W" or localBState[row+1][column+1] == "KW":
                        if localBState[row+2][column+2] == "BLANK":
                            locs.append((row+2,column+2,(row+1,column+1)))
                    if localBState[row+1][column-1] == "W" or localBState[row+1][column-1] == "KW":
                        if localBState[row+2][column-2] == "BLANK":
                            locs.append((row+2,column-2,(row+1,column-1)))
                    return locs
        if t == "W":
            
            if row > 1:
                if column < 2:
                    if localBState[row-1][column+1] == "B" or localBState[row-1][column+1] == "KB":
                        if localBState[row-2][column+2] == "BLANK":
                            locs.append((row-2,column+2,(row-1,column+1)))
                            return locs
                    else:
                        return locs
                elif column > 5:
                    if localBState[row-1][column-1] == "B" or localBState[row-1][column-1] == "KB":
                        if localBState[row-2][column-2] == "BLANK":
                            locs.append((row-2,column-2,(row-1,column-1)))
                            return locs
                    else:
                        return locs
                else:
                    if localBState[row-1][column+1] == "B" or localBState[row-1][column+1] == "KB":
                        if localBState[row-2][column+2] == "BLANK":
                            locs.append((row-2,column+2,(row-1,column+1)))
                    if localBState[row-1][column-1] == "B" or localBState[row-1][column-1] == "KB":
                        if localBState[row-2][column-2] == "BLANK":
                            locs.append((row-2,column-2,(row-1,column-1)))
                    
                    return locs
        if t == "KB":
            if row < 2:
                if column <2:
                    
                    if localBState[row+1][column+1] == "W" or localBState[row+1][column+1] == "KW":
                        if localBState[row+2][column+2] == "BLANK":
                            locs.append((row+2,column+2,(row+1,column+1)))
                            return locs
                    else:
                        return locs
                elif column > 5:
                    if localBState[row+1][column-1] == "W" or localBState[row+1][column-1] == "KW":
                        if localBState[row+2][column-2] == "BLANK":
                            locs.append((row+2,column-2,(row+1,column-1)))
                            return locs
                    else:
                        return locs
                else:
                    if localBState[row+1][column+1] == "W" or localBState[row+1][column+1] == "KW":
                        if localBState[row+2][column+2] == "BLANK":
                            locs.append((row+2,column+2,(row+1,column+1)))
                    if localBState[row+1][column-1] == "W" or localBState[row+1][column-1] == "KW":
                        if localBState[row+2][column-2] == "BLANK":
                            locs.append((row+2,column-2,(row+1,column-1)))
                    return locs
            elif row > 5:
                if column <2:
                    if localBState[row-1][column+1] == "W" or localBState[row-1][column+1] == "KW":
                        if localBState[row-2][column+2] == "BLANK":
                            locs.append((row-2,column+2,(row-1,column+1)))
                            return locs
                    else:
                        return locs
                elif column > 5:
                    if localBState[row-1][column-1] == "W" or localBState[row-1][column-1] == "KW":
                        if localBState[row-2][column-2] == "BLANK":
                            locs.append((row-2,column-2,(row-1,column-1)))
                            return locs
                    else:
                        return locs
                else:
                    if localBState[row-1][column+1] == "W" or localBState[row-1][column+1] == "KW":
                        if localBState[row-2][column+2] == "BLANK":
                            locs.append((row-2,column+2,(row-1,column+1)))
                    if localBState[row-1][column-1] == "W" or localBState[row-1][column-1] == "KW":
                        if localBState[row-2][column-2] == "BLANK":
                            locs.append((row-2,column-2,(row-1,column-1)))
                    return locs
            else:
                if column <2:
                    
                    if localBState[row+1][column+1] == "W" or localBState[row+1][column+1] == "KW":
                        if localBState[row+2][column+2] == "BLANK":
                            locs.append((row+2,column+2,(row+1,column+1)))
                    if localBState[row-1][column+1] == "W" or localBState[row-1][column+1] == "KW":
                        if localBState[row-2][column+2] == "BLANK":
                            locs.append((row-2,column+2,(row-1,column+1)))
                    else:
                        return locs
                elif column > 5:
                    if localBState[row+1][column-1] == "W" or localBState[row+1][column-1] == "KW":
                        if localBState[row+2][column-2] == "BLANK":
                            locs.append((row+2,column-2,(row+1,column-1)))
                    if localBState[row-1][column-1] == "W" or localBState[row-1][column-1] == "KW":
                        if localBState[row-2][column-2] == "BLANK":
                            locs.append((row-2,column-2,(row-1,column-1)))
                    else:
                        return locs
                else:
                    if localBState[row+1][column+1] == "W" or localBState[row+1][column+1] == "KW":
                        if localBState[row+2][column+2] == "BLANK":
                            locs.append((row+2,column+2,(row+1,column+1)))
                    if localBState[row-1][column+1] == "W" or localBState[row-1][column+1] == "KW":
                        if localBState[row-2][column+2] == "BLANK":
                            locs.append((row-2,column+2,(row-1,column+1)))
                    if localBState[row+1][column-1] == "W" or localBState[row+1][column-1] == "KW":
                        if localBState[row+2][column-2] == "BLANK":
                            locs.append((row+2,column-2,(row+1,column-1)))
                    if localBState[row-1][column-1] == "W" or localBState[row-1][column-1] == "KW":
                        if localBState[row-2][column-2] == "BLANK":
                            locs.append((row-2,column-2,(row-1,column-1)))
                    return locs
        if t == "KW":
            if row < 2:
                if column <2:
                    
                    if localBState[row+1][column+1] == "B" or localBState[row+1][column+1] == "KB":
                        if localBState[row+2][column+2] == "BLANK":
                            locs.append((row+2,column+2,(row+1,column+1)))
                            return locs
                    else:
                        return locs
                elif column > 5:
                    if localBState[row+1][column-1] == "B" or localBState[row+1][column-1] == "KB":
                        if localBState[row+2][column-2] == "BLANK":
                            locs.append((row+2,column-2,(row+1,column-1)))
                            return locs
                    else:
                        return locs
                else:
                    if localBState[row+1][column+1] == "B" or localBState[row+1][column+1] == "KB":
                        if localBState[row+2][column+2] == "BLANK":
                            locs.append((row+2,column+2,(row+1,column+1)))
                    if localBState[row+1][column-1] == "B" or localBState[row+1][column-1] == "KB":
                        if localBState[row+2][column-2] == "BLANK":
                            locs.append((row+2,column-2,(row+1,column-1)))
                    return locs
            elif row > 5:
                if column <2:
                    if localBState[row-1][column+1] == "B" or localBState[row-1][column+1] == "KB":
                        if localBState[row-2][column+2] == "BLANK":
                            locs.append((row-2,column+2,(row-1,column+1)))
                            return locs
                    else:
                        return locs
                elif column > 5:
                    if localBState[row-1][column-1] == "B" or localBState[row-1][column-1] == "KB":
                        if localBState[row-2][column-2] == "BLANK":
                            locs.append((row-2,column-2,(row-1,column-1)))
                            return locs
                    else:
                        return locs
                else:
                    if localBState[row-1][column+1] == "B" or localBState[row-1][column+1] == "KB":
                        if localBState[row-2][column+2] == "BLANK":
                            locs.append((row-2,column+2,(row-1,column+1)))
                    if localBState[row-1][column-1] == "B" or localBState[row-1][column-1] == "KB":
                        if localBState[row-2][column-2] == "BLANK":
                            locs.append((row-2,column-2,(row-1,column-1)))
                    return locs
            else:
                if column <2:
                    
                    if localBState[row+1][column+1] == "B" or localBState[row+1][column+1] == "KB":
                        if localBState[row+2][column+2] == "BLANK":
                            locs.append((row+2,column+2,(row+1,column+1)))
                    if localBState[row-1][column+1] == "B" or localBState[row-1][column+1] == "KB":
                        if localBState[row-2][column+2] == "BLANK":
                            locs.append((row-2,column+2,(row-1,column+1)))
                    else:
                        return locs
                elif column > 5:
                    if localBState[row+1][column-1] == "B" or localBState[row+1][column-1] == "KB":
                        if localBState[row+2][column-2] == "BLANK":
                            locs.append((row+2,column-2,(row+1,column-1)))
                    if localBState[row-1][column-1] == "B" or localBState[row-1][column-1] == "KB":
                        if localBState[row-2][column-2] == "BLANK":
                            locs.append((row-2,column-2,(row-1,column-1)))
                    else:
                        return locs
                else:
                    if localBState[row+1][column+1] == "B" or localBState[row+1][column+1] == "KB":
                        if localBState[row+2][column+2] == "BLANK":
                            locs.append((row+2,column+2,(row+1,column+1)))
                    if localBState[row-1][column+1] == "B" or localBState[row-1][column+1] == "KB":
                        if localBState[row-2][column+2] == "BLANK":
                            locs.append((row-2,column+2,(row-1,column+1)))
                    if localBState[row+1][column-1] == "B" or localBState[row+1][column-1] == "KB":
                        if localBState[row+2][column-2] == "BLANK":
                            locs.append((row+2,column-2,(row+1,column-1)))
                    if localBState[row-1][column-1] == "B" or localBState[row-1][column-1] == "KB":
                        if localBState[row-2][column-2] == "BLANK":
                            locs.append((row-2,column-2,(row-1,column-1)))
                    return locs

def checkKing(coord):
    pl = GameState.s.getCurrentPlayer()
    if (coord[0] == 0 and pl == "WHITE") or (coord[0] == 7 and pl == "BLACK"):
        return True
    else:
        return False

def selectTile(a, b):

    s = GameState.s

    if (s.getGameState() == 1): #Setup phase
        
        checkC = a + b

        if (checkC % 2 != 0):  #they clicked a white tile
            boardState[a][b] = s.getSelectedCustomPiece()
            
    elif (s.getGameState() == 2): #Game phase
        #print(places((2,1)))
        if not GameState.s.getSelectedTile(): #A tile has not currently been picked up
            moves = checkLegalMoves((a,b)) #checking if the piece can be picked up
            print moves
            st = GameState.s
            if moves:
                st.setSelectedTile((a,b))
                st.setLegalMoves(moves)
                pType = boardState[a][b]
                if pType == "B":
                    st.setPickedUpPiece("black")
                elif pType == "W":
                    st.setPickedUpPiece("white")
                elif pType == "KW":
                    st.setPickedUpPiece("kingwhite")
                elif pType == "KB":
                    st.setPickedUpPiece("kingblack")
                boardState[a][b] = "selected"
                
                for m in moves:
                    print m
                    boardState[m[0]][m[1]] = "legal"
        
                
                    
        else:
            state = GameState.s
            moves = state.getLegalMoves()
            if boardState[a][b] == "selected": #case 1 they clicked on the selected tile
                    boardState[a][b] = convFileToState(state.getPickedUpPiece())
                    for m in moves:
                        boardState[m[0]][m[1]] = "BLANK"
                    state.clearPiece()
            else:
                for m in moves:
                    if a == m[0] and b == m[1]: #case 2 a legal move is taken
                        if not m[2]: #no piece taken
                            if not checkKing((a,b)):
                                boardState[a][b] = convFileToState(state.getPickedUpPiece())
                            else:
                                if state.getCurrentPlayer() == "BLACK":
                                    boardState[a][b] = "KB"
                                else:
                                    boardState[a][b] = "KW"
                            select = state.getSelectedTile()
                            boardState[select[0]][select[1]] = "BLANK"
                            for m in moves:
                                if (m[0],m[1]) != (a,b):
                                    boardState[m[0]][m[1]] = "BLANK"
                            
                            state.playerSwitch()
                            gameEnd() 
                            state.clearPiece()
                             
                            return
                        else: #a piece is overtaken
                            if not checkKing((a,b)):
                                boardState[a][b] = convFileToState(state.getPickedUpPiece())
                            else:
                                if state.getCurrentPlayer() == "BLACK":
                                    boardState[a][b] = "KB"
                                else:
                                    boardState[a][b] = "KW"
                            select = state.getSelectedTile()
                            boardState[select[0]][select[1]] = "BLANK"
                            boardState[m[2][0]][m[2][1]] = "BLANK"
                            for m in moves:
                                if (m[0],m[1]) != (a,b):
                                    boardState[m[0]][m[1]] = "BLANK"
                            secMoves = checkAttackMoves((a,b))
                            if not secMoves: #there are no other attack moves to be taken
                                state.playerSwitch()
                                gameEnd()  
                                state.clearPiece()
                                 
                                return
                            else: #there are attack moves to be taken
                                state.setPickedUpPiece(convStateToFile(boardState[a][b]))
                                boardState[a][b] = "selected"
                                state.setSelectedTile((a,b))
                                for m in secMoves:
                                    boardState[m[0]][m[1]] = "legal"
                                state.setLegalMoves(secMoves)
                                return
                            
                
def gameEnd():
    bmoves  = 0
    wmoves = 0
    wpiece = 0
    bpiece = 0
    player = GameState.s.getCurrentPlayer()

    
#CHECK 1: Are there any pieces left on the board of one colour?

    for i in range(len(boardState)):
        m = boardState[i]
        for j in range(len(m)):
            col = boardState[i][j]

            if (col == "W" or col == "KW"):
                wpiece = wpiece + 1

            if (col == "B" or col == "KB"):
                bpiece = bpiece + 1

            
    if (wpiece == 0):
        GameState.s.currentWinner("BLACK")
    if (bpiece == 0):
        GameState.s.currentWinner("WHITE")
        
            
   
#CHECK 2: Are there any possible moves left for a certain player?   

        for i in range(len(boardState)):
            m = boardState[i]
            for j in range(len(m)):
                piece = (i,j) #coordinate of piece on board
                col = boardState[i][j]
            if (checkLegalMoves(piece) != None or checkAttackMoves(piece) != None):
                if (col == "B" or col == "KB"):
                    bmoves += 1
                    print("Avail black moves: ")
                    print(bmoves)
                if (col == "W" or col == "KW"):
                    wmoves += 1
                    print ("Avil white moves: ")
                    print(wmoves)
            

    if (bmoves == 0 and player == "BLACK"):
        GameState.s.currentWinner("WHITE")
        print("bmoves == 0 end")
    elif (wmoves == 0 and player == "WHITE"):
        GameState.s.currentWinner("BLACK")
        print("wmoves == 0 end")
        
   
            
            

def getBoardState():
    return boardState
      


def insertPiece(a, b, piece):
    boardState[a][b] = piece

def deletePiece(a, b):
    boardState[a][b] = "BLANK"


    






        



    







        

