#Constants Module: Simply creates a list of buttons that all have
# constant values 


SIZE = [800,600]


def getButtons():
    buttons = []
    buttons.append((0,"standardButton",510,100,275,69))
    buttons.append((0,"customButton",510,250,275,69))
    buttons.append((1,"white",510,100,42,42))
    buttons.append((1,"black",510,300,42,42))
    buttons.append((1,"kingwhite",510,200,42,42))
    buttons.append((1,"kingblack",510,400,42,42))
    buttons.append((1,"blank", 510, 10, 42, 42))
    buttons.append((1,"finish", 510, 500, 275, 69))
    buttons.append((2,"saveButton", 510, 100, 275, 69))
    buttons.append((0,"loadButton", 510, 400, 275, 69))
    buttons.append((2,"menuButton",510,250,275,69))
    return buttons
    
