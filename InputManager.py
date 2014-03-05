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
        x = Constants.getButtons()
        for i in range x:
            if i[0] == GameState.s.getGameState():
                xmin = i[3]
                ymin = i[4]
                xmax = xmin + i[5]
                ymax = ymin + i[6]
                if xmin<=pos[0]<=xmax and ymin<=pos[1] <=ymax:
                    callFunction(i[0])


def callFunction(s):

    if (s = "standardButton"):
        Menu.buttonStandard()
    elif (s = "customButton"):
        Menu.buttonCustom()
    elif (s = "white"):
        Menu.CustomPiece("W")
    elif (s = "black"):
        Menu.CustomPiece("B")
    elif (s = "kingwhite"):
        Menu.CustomPiece("KW")
    elif (s = "kingblack"):
        Menu.CustomPiece("KB")
