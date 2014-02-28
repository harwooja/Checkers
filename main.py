import pygame,sys
from pygame.locals import *
pygame.init()
size = [800,600]
window = pygame.display.set_mode(size)
pygame.display.set_caption("Checkers 2ME3/2AA4 #CompSci4Life")
done = False
bg = pygame.image.load("back.jpg")
bg = pygame.transform.scale(bg,size)
clock = pygame.time.Clock()

black = 0,0,0
red = 245,27,27
redp = 252,3,3
goldp = 209,227,43
white = 255,255,255


#Event Loop
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    window.blit(bg,(0,0))
    pygame.draw.rect (window, red, Rect((5,5), (490,490)))
    pygame.draw.rect (window, black, Rect((10,10), (480,480)))
    

    
    pygame.display.flip()
#each box 5 long
#board 
    clock.tick(60) #60 fps
#black every 85 from x and 80 y


