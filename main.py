# This module is where the code is originally ran. Sets up everything
# for the game.

# Imports modules that we use here
import pygame,sys,Board,Constants,InputManager,Menu,GameState
from pygame.locals import *


pygame.init()
size = Constants.SIZE
window = pygame.display.set_mode(size)
pygame.display.set_caption("Checkers 2ME3/2AA4 #CompSci4Life")
done = False
clock = pygame.time.Clock()
Menu.init_buttons()


#drawPickedUpPiece function: This function draws the piece that is placed
# on our custom board.

def drawPickedUpPiece():
    posx,posy = pygame.mouse.get_pos()
    posx = posx - 18
    posy = posy - 18
    if GameState.s.getPickedUpPiece()=="white":
        piece = pygame.image.load("white.png").convert_alpha()
        window.blit(piece,(posx,posy))

    elif GameState.s.getPickedUpPiece()=="black":
        piece = pygame.image.load("black.png").convert_alpha()
        window.blit(piece,(posx,posy))

    elif GameState.s.getPickedUpPiece()=="kingblack":
        piece = pygame.image.load("kingblack.png").convert_alpha()
        window.blit(piece,(posx,posy))

    elif GameState.s.getPickedUpPiece()=="kingwhite":
        piece = pygame.image.load("kingwhite.png").convert_alpha()
        window.blit(piece,(posx,posy))



#Event Loop
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            
            InputManager.dispatch(pos)
            
            
            

    Board.drawBoard(window)
    
# If gamestate is 0, we will call drawSetup    
    if GameState.s.getGameState() == 0:
        Menu.drawSetup(window)
# if gamestate is 1, we will call drawCustomSetup
    elif GameState.s.getGameState() == 1:
        Menu.drawCustomSetup(window)
# if gamestate is 2, we will call drawGame
    elif GameState.s.getGameState() == 2:
        Menu.drawGame(window)

#If gamestate is not blank, we will draw the winner
    if GameState.s.getcurrentWinner() != "":
        Menu.drawWinner(window)
    
    drawPickedUpPiece()
    pygame.display.flip()
    clock.tick(60) #60 fps






