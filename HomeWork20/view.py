import controller

def getThrow():
    return input('для продалжения s: ')

def viewMassage(mas):
    print(mas)

def getLoop():
    return mainloop

def mainloop():
    while True:
        controller.controllerLoop()
