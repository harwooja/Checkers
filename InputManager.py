import pygame, sys, Constants,Board
from pygame.locals import *

def dispatch(pos):
    bTopLeft = Board.TOPLEFT
    bWidth = Board.WIDTH
    bBottom = bTopLeft + bWidth
    if (bTopLeft <= pos[0] < bBottom) and (bTopLeft <= pos[1] < bBottom):
        column = (pos[0]-bTopLeft)/60
        row = (pos[1]-bTopLeft)/60
        print (row,column)
        Board.selectTile(row,column)
    else:
        print pos
