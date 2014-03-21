import pickle 
def saveState(state):
    file_name = "Savefile"#name of the savefile
    fileObject = open(file_name,'wb')#creates the savefile
    pickle.dump(state,fileObject)#saves the gameState into the savefile
    fileObject.close()#closes savefile

def loadState():
    try:
        file_name = "Savefile"#name of file to load
        fileObject = open(file_name,'r')#opens file in read mode
        loadedList = pickle.load(fileObject)#loadedList is assigned to whatever was saved
        fileObject.close()#closes the file
        return loadedList#returns the gameState
    except ValueError:#checks to see if there is a savefile to begin with, via try and catch
        print("No save file detected")

    
    
    

