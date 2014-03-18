import Constants


class State():

    gameState = 0 #0 = preSetup,CustomSetup,PlayState

    selectedCustomTile = "W"
    pickedUpPiece = "BLANK"

    def getGameState(self):
        return self.gameState
    def setGameState(self,x):
        if (type(x) is  int) and (0<= x <= 3):
            self.gameState = x

    def getSelectedCustomPiece(self):
        return self.selectedCustomTile


    def setSelectedCustomPiece(self,x):
        self.selectedCustomTile = x

    def setPickedUpPiece(self,x):
        self.pickedUpPiece = x

    def getPieckedUpPiece(self):
        return self.pickedUpPiece

        
s = State()
