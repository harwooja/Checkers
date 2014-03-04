import Constants

gameState = 0 #0 = preSetup,CustomSetup,PlayState

def getGameState():
    return gameState
def setGameState(x):
    if (type(x) is  int) and (0<= x <= 3):
        gameState = x
