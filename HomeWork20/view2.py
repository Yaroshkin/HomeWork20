import tkinter
import controller

def getThrow():
    return txt.get()

def viewMassage(mas):
    lb1.configure(text=mas)

def getLoop():
    return window.mainloop

window = tkinter.Tk()

lb1 = tkinter.Label(window, text='')
txt = tkinter.Entry(window, width=30)
btn = tkinter.Button(window, text="Бросок", command=controller.controllerLoop)

lb1.grid(column=0, row=0)
txt.grid(column=0, row=1)
btn.grid(column=1, row=1)


