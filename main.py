import pygame,sys,Board,Constants,InputManager,Menu,GameState
from pygame.locals import *
pygame.init()
size = Constants.SIZE
window = pygame.display.set_mode(size)
pygame.display.set_caption("Checkers 2ME3/2AA4 #CompSci4Life")
done = False
clock = pygame.time.Clock()
Menu.init_buttons()


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
    
    
    if GameState.s.getGameState() == 0:
        Menu.drawSetup(window)
    elif GameState.s.getGameState() == 1:
        Menu.drawCustomSetup(window)
    elif GameState.s.getGameState() == 2:
        Menu.drawGame(window)

    if GameState.s.getcurrentWinner() != "":
        Menu.drawWinner(window)
    
    drawPickedUpPiece()
    pygame.display.flip()
    clock.tick(60) #60 fps






