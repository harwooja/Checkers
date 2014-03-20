import itertools

def saveState(state):
    oneList = list(itertools.chain.from_iterable(state))
    myfile = open("savingTest.txt","w")
    for item in oneList:
          myfile.write("%s\n" % item)
    myfile.close()

def loadState():
    lastList = []
    with open("savingTest.txt", "r") as myfile:
        for line in myfile:
            lastList.append(line)
    finalList = []
    counter1 = 0
    counter2 = 8
    while(len(finalList) != 8):
        finalList.append(make1DAndAppend(lastList,counter1,counter2))
    return finalList    
    myfile.close()

def make1DArray(state):
    newList = []
    for i in range (len(state)):
        if(state[i] != "]"):
            newList.append(state[i])
        elif(state[i]=="]"):
            newList.append(state[i])
            break
    return newList

def getCounter1(counter):
    return counter

def getCounter2(counter):
    return counter

def make1DAndAppend(state,counter1,counter2):
    listToAdd = []
    counter = counter1
    for counter in range(counter2):
        toAppend = state[counter]
        toAppend = toAppend[:-1]
        listToAdd.append(toAppend)
    counter1 += 8
    counter2 += 8
    getCounter1(counter1)
    getCounter2(counter2)
    return listToAdd

    
    
    

