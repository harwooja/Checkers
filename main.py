import pygame,sys,Board,Constants,InputManager,Menu
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
            #print pos
            InputManager.dispatch(pos)
            
            
    Board.drawBoard(window)
    Menu.drawSetup() #TODO
    pygame.display.flip()
    clock.tick(60) #60 fps



