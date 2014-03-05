import pygame, sys, Constants,Board,GameState,Menu
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
        for i in x:
            if i[0] == GameState.s.getGameState():
                xmin = i[2]
                ymin = i[3]
                xmax = xmin + i[4]
                ymax = ymin + i[5]
                print pos
                print (xmin,xmax,ymin,ymax,i[1])
                if (xmin<=pos[0]<=xmax) and (ymin<=pos[1] <=ymax):
                    callFunction(i[1])


def callFunction(s):
    print s
    if (s == "standardButton"):
        Menu.buttonStandardBoard()
    elif (s == "customButton"):
        Menu.buttonCustomBoard()
    elif (s == "white"):
        Menu.buttonCustomPiece("W")
    elif (s == "black"):
        Menu.buttonCustomPiece("B")
    elif (s == "kingwhite"):
        Menu.buttonCustomPiece("KW")
    elif (s == "kingblack"):
        Menu.buttonCustomPiece("KB")
