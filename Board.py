import pygame, sys, Constants, GameState
from pygame.locals import *

TOPLEFT = 10
WIDTH = 480






boardState = []

for m in range (8):
    boardState.append([])
    for z in range(8):
        boardState[m].append("Blank")

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
                pygame.draw.rect(window,red,Rect((xcord,ycord),(60,60)))
                
def checkLegalMoves(coord):
    return []

def checkAttackMoves(coord):
    return []

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
        if not GameState.s.getSelectedTile(): #A tile has not currently been picked up
            moves = checkLegalMoves((a,b)) #checking if the piece can be picked up
            st = GameState.s
            if moves:
                st.setSelectedTile((a,b))
                st.setLegalMoves(m)
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
                    boardState[m[0]][m[1]] = "legal"
        
                
                    
        else:
            state = GameState.s
            moves = state.getLegalMoves()
            if boardState[a][b] == "selected": #case 1 they clicked on the selected tile
                    boardState[a][b] = convFileToState(state.getPickedUpPiece())
                    for m in moves:
                        boardState[m[0]][m[1]] = "BLANK"
                    state.setLegalMoves([])
                    state.setSelectedTile(())
                    state.setPickedUpTile("BLANK")
            else:
                for m in moves:
                    if a == m[0] and b == m[1]: #case 2 a legal move is taken
                        if not m[2]: #no piece taken
                            if not checkKing(coord):
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
                            state.clearPiece()
                            return
                        else: #a piece is overtaken
                            if not checkKing(coord):
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
                                state.clearPiece()
                                return
                            else: #there are attack moves to be taken
                                state.setPickedUpPiece(convStateToFile(boardState[a][b]))
                                boardState[a][b] = "selected"
                                state.setSelectedTile((a,b))
                                state.setLegalMoves(secMoves)
                                return
                            
                

        
            


def insertPiece(a, b, piece):
    boardState[a][b] = piece

def deletePiece(a, b):
    boardState[a][b] = "BLANK"


    







        

