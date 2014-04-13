#This class deals with setting the states of our program depending on a current
# situation. An example may be when the user in the setup phase, then our game
# state would be set to 0.

#Imports our constants module
import Constants


class State():

#Sets our global variables
    gameState = 0 #0 = preSetup,CustomSetup,PlayState
    selectedCustomTile = "W"
    pickedUpPiece = "BLANK"
    currentPlayer = "WHITE"
    selectedTile = ()
    legalMoves = []
    currentWin = ""

#getGameState function: This function returns the current gamestate value
    def getGameState(self):
        return self.gameState
    
#setGameState function: This function sets the current gamestate value
    def setGameState(self,x):
        if (type(x) is  int) and (0<= x <= 3):
            self.gameState = x
            
#getSelectedCustomPIece: This function will return the value of the selected
#piece chosen on the board.
    def getSelectedCustomPiece(self):
        return self.selectedCustomTile

#setSelectedCustomPiece: This function will set the value of the selected
#piece chosen on the board.
    def setSelectedCustomPiece(self,x):
        self.selectedCustomTile = x

#setPickedUpPiece: Sets the value of the picked up piece on the board.
    def setPickedUpPiece(self,x):
        self.pickedUpPiece = x

#getPickedUpPiece: Returns the value of the current picked up piece
    def getPickedUpPiece(self):
        return self.pickedUpPiece

#setCurrentPlayer: Sets the value of the current player (black or white)
    def setCurrentPlayer(self,x):
        self.currentPlayer = x

#getCurrentPlayer: Returns the value of the current player (black or white)
    def getCurrentPlayer(self):
        return self.currentPlayer
    
#getSelectedTile: Returns the coordinates of the current clicked tile.
    def getSelectedTile(self):
        return self.selectedTile

#setSelectedTile: Sets the coordinates of the selected tile    
    def setSelectedTile(self,x):
        self.selectedTile = x

#clearSelectedTile: Clears the coordinate value of the selected tile
    def clearSelectedTile(self):
        self.selectedTile = ()

#setLegalMoves: Sets our array (list) of legal moves depending on the argument
    def setLegalMoves(self,x):
        self.legalMoves = x

#getLegalMoves: Returns our array (list) of legal moves 
    def getLegalMoves(self):
        return self.legalMoves

#clearPiece: Clears the piece entirely from the board. Coordinate, moves, and
# values all wiped

    def clearPiece(self):
        self.legalMoves = []
        self.selectedTile = ()
        self.pickedUpPiece = "BLANK"

#playerSwitch: This function simply switches the value of our currentplayer.
# Handles with turn switching.

    def playerSwitch(self):
        if self.currentPlayer == "WHITE":
            self.currentPlayer = "BLACK"
        else:
            self.currentPlayer = "WHITE"

#currentWinner: This function sets the winner of the game (at the end of the game)
    def currentWinner(self, winner):
        self.currentWin = winner

#getCurrentWinner: This function returns the winner of the game (at the end of the game)
    def getcurrentWinner(self):
        return self.currentWin
        

     
        
    
# Calls state
s = State()
