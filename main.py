import pygame,sys,Board#,InputManager,Setup
from pygame.locals import *
pygame.init()
size = [800,600]
window = pygame.display.set_mode(size)
pygame.display.set_caption("Checkers 2ME3/2AA4 #CompSci4Life")
done = False
#bg = pygame.image.load("back.jpg") #board
#bg = pygame.transform.scale(bg,size) #board
clock = pygame.time.Clock()

#black = 0,0,0 #board
#red = 245,27,27 #board
#redp = 252,3,3 #board
#goldp = 209,227,43 #board
#white = 255,255,255 #board


#Event Loop
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            #print pos
            #InputManager.dispatch(pos)
            
            
    Board.drawBoard(window, size) #TODO Write this
    #Setup.drawSetup()
    #window.blit(bg,(0,0)) #board
    #pygame.draw.rect (window, red, Rect((5,5), (490,490))) #board
    #pygame.draw.rect (window, black, Rect((10,10), (480,480))) #board
    

    
    pygame.display.flip()
#each box 5 long
#board 
    clock.tick(60) #60 fps
#black every 85 from x and 80 y


