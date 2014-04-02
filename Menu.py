import pygame,sys,Constants,GameState,Board,Saving
from pygame.locals import *

#only load images once
size = Constants.SIZE
def init_buttons():
    #buttons
    global buttonStandard,buttonCustom,buttonLoad,buttonSave,buttonMenu,indicatorWhite,indicatorBlack
    global font,turnLabel,piece_W,piece_B,piece_WK,piece_BK,piece_BLANK,piece_FINISH,piece_Selected
    buttonStandard = pygame.image.load("standardButton.png").convert_alpha()
    buttonCustom = pygame.image.load("customButton.png").convert_alpha()
    buttonLoad = pygame.image.load("loadGameButton.png").convert_alpha()
    buttonSave = pygame.image.load("saveGameButton.png").convert_alpha()
    buttonMenu = pygame.image.load("menuButton.png").convert_alpha()
    #indicator pieces
    indicatorWhite = pygame.image.load("white.png").convert_alpha()
    indicatorBlack = pygame.image.load("black.png").convert_alpha()
    #font/text
    font = pygame.font.SysFont("monospace", 40)
    turnLabel = font.render("Turn:", 3, (255,255,255))
    #pieces
    piece_W = pygame.image.load("white.png").convert_alpha()
    piece_B = pygame.image.load("black.png").convert_alpha()
    piece_WK = pygame.image.load("kingwhite.png").convert_alpha()
    piece_BK = pygame.image.load("kingblack.png").convert_alpha()
    piece_BLANK = pygame.image.load("redx.png").convert_alpha()
    piece_FINISH = pygame.image.load("finishButton.png").convert_alpha()
    piece_Selected = pygame.image.load("highlight.png").convert_alpha()

    
#drawSetup function
def drawSetup(window):
    window.blit(buttonStandard,(510,100))
    window.blit(buttonCustom,(510,250))
    window.blit(buttonLoad,(510,400))

def drawGame(window):
    currentTurn = GameState.s.getCurrentPlayer() #WHITE or BLACK
    
    window.blit(buttonSave,(510,100))
    window.blit(buttonMenu,(510,250))
    window.blit(turnLabel,(510,363))
    if(currentTurn == "WHITE"):
        window.blit(indicatorWhite,(625,360))
    else:
        window.blit(indicatorBlack,(625,360))
    
def drawCustomSetup(window):
    window.blit(piece_W, (510,100))
    window.blit(piece_WK, (510,200))
    window.blit(piece_B, (510,300))
    window.blit(piece_BK, (510,400))
    window.blit(piece_BLANK, (510, 10))
    window.blit(piece_FINISH, (510, 500))
    s = GameState.s.getSelectedCustomPiece()
    if s == "W":
        window.blit(piece_Selected, (510,100))
    elif s == "B":
        window.blit(piece_Selected, (510,300))
    elif s == "KW":
        window.blit(piece_Selected, (510,200))
    elif s == "KB":
        window.blit(piece_Selected, (510,400))
    elif s == "BLANK":
        window.blit(piece_Selected, (510,10))

def buttonCustomFinish():
    GameState.s.setGameState(2)

def buttonCustomBoard():
    GameState.s.setGameState(1)

def buttonMenu():
    GameState.s.setGameState(0)

def buttonCustomPiece(pieceType):
    GameState.s.setSelectedCustomPiece(pieceType)

def buttonStandardBoard():
    GameState.s.setGameState(2)
    for row in range(8):
        for column in range(8):
            if (0<= row <= 2) and (((row+column) %2) == 1):
                Board.insertPiece(row,column,"B")
            if (5<=row<=8) and (((row+column) %2) == 1):
                Board.insertPiece(row,column,"W")
                
def saveButton():
    board = Board.boardState
    cPlayer = GameState.s.getCurrentPlayer()
    state = (board,cPlayer)
    Saving.saveState(state)

def loadButton():
    state = Saving.loadState()
    if state:
        Board.boardState = state[0]
        GameState.s.setCurrentPlayer(state[1])
        GameState.s.setGameState(2)
