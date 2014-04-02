import Constants


class State():

    gameState = 0 #0 = preSetup,CustomSetup,PlayState
    
    selectedCustomTile = "W"
    pickedUpPiece = "BLANK"
    currentPlayer = "WHITE"
    selectedTile = ()
    legalMoves = []
    currentWin = ""

    def getGameState(self):
        return self.gameState
    def setGameState(self,x):
        if (type(x) is  int) and (0<= x <= 3):
            self.gameState = x

    def getSelectedCustomPiece(self):
        return self.selectedCustomTile


    def setSelectedCustomPiece(self,x):
        self.selectedCustomTile = x

    #New and shiny stuff goes here
    def setPickedUpPiece(self,x):
        self.pickedUpPiece = x

    def getPickedUpPiece(self):
        return self.pickedUpPiece

    def setCurrentPlayer(self,x):
        self.currentPlayer = x

    def getCurrentPlayer(self):
        return self.currentPlayer
    
    def getSelectedTile(self):
        return self.selectedTile
    
    def setSelectedTile(self,x):
        self.selectedTile = x

    def clearSelectedTile(self):
        self.selectedTile = ()

    def setLegalMoves(self,x):
        self.legalMoves = x

    def getLegalMoves(self):
        return self.legalMoves

    def clearPiece(self):
        self.legalMoves = []
        self.selectedTile = ()
        self.pickedUpPiece = "BLANK"

    def playerSwitch(self):
        if self.currentPlayer == "WHITE":
            self.currentPlayer = "BLACK"
        else:
            self.currentPlayer = "WHITE"

    def currentWinner(self, winner):
        self.currentWin = winner

    def getcurrentWinner(self):
        return self.currentWin
        

     
        
    
    
s = State()
