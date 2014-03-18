import pygame,sys,Board,Constants,InputManager,Menu,GameState
from pygame.locals import *
pygame.init()
size = Constants.SIZE
window = pygame.display.set_mode(size)
pygame.display.set_caption("Checkers 2ME3/2AA4 #CompSci4Life")
done = False
clock = pygame.time.Clock()


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
    
    pygame.display.flip()
    clock.tick(60) #60 fps



