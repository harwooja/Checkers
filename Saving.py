import pickle 
def saveState(state):
    file_name = "Savefile"
    fileObject = open(file_name,'wb')
    pickle.dump(state,fileObject)
    fileObject.close()

def loadState():
    try:
        file_name = "Savefile"
        fileObject = open(file_name,'r')
        loadedList = pickle.load(fileObject)
        fileObject.close()
        return loadedList
    except ValueError:
        print("No save file detected")

    
    
    

