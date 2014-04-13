#This class deals with all of our input. Will call functions depending
# on what the user clicks on the board.

#Imports all the modules used here
import pygame, sys, Constants,Board,GameState,Menu
from pygame.locals import *

#dispatch function:
def dispatch(pos):
    bTopLeft = Board.TOPLEFT
    bWidth = Board.WIDTH
    bBottom = bTopLeft + bWidth
    if (bTopLeft <= pos[0] < bBottom) and (bTopLeft <= pos[1] < bBottom):
        column = (pos[0]-bTopLeft)/60
        row = (pos[1]-bTopLeft)/60
        Board.selectTile(row,column)
    else:
        x = Constants.getButtons()
        for i in x:
            if i[0] == GameState.s.getGameState():
                xmin = i[2]
                ymin = i[3]
                xmax = xmin + i[4]
                ymax = ymin + i[5]
                if (xmin<=pos[0]<=xmax) and (ymin<=pos[1] <=ymax):
                    callFunction(i[1])

#callFunction function: Depending on what our input value from the user is, we will
# confirm whatever the user wanted to do by calling the function in Menu.

def callFunction(s):
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
    elif (s == "blank"):
        Menu.buttonCustomPiece("BLANK")
    elif (s == "finish"):
        Menu.buttonCustomFinish()
    elif (s == "saveButton"):
        Menu.saveButton()
    elif (s == "loadButton"):
        Menu.loadButton()
    elif (s == "menuButton"):
        Menu.buttonMainMenu()

    
