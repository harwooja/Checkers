import pygame, Board



# Reads the entire board, stores a list of each pieces possibilities
def choosePiece(board):


    attackmoves = [] # [coordinate, value at coordinate, list of attack moves]
    normalmoves = [] # [coordinate, value at coordinate, list of normal moves]

    for i in range(len(board)):
        m = board[i]
        for j in range(len(m)):
            piece = (i,j) #coordinate of piece on board
            col = boardState[i][j] #value at coordinate
            if (Board.checkLegalMoves(piece):
                normalmoves.append(piece, col, Board.checkLegalMoves(piece))
            if (Board.checkAttackMoves(piece)):
                attackmoves.append(piece, col, Board.checkAttackMoves(piece))

    ranking(normalmoves, attackmoves)


    
def ranking(normalmoves, attackmoves):

    for i in normalmoves:
        nindex = i[0]
        nval = i[1]
        nlst = i[2]

    for i in attackmoves:
        aindex = i[0]
        aval = i[1]
        alst = i[2]
            

