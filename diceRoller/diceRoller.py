from tkinter import *
from random import randint

def diceRoller():
    window = Tk()
    window.title('Dice Roller')

    reslt = StringVar()

    dNum = Entry(window)
    numD = Entry(window)

    result = Label(window, textvariable=reslt, relief=RAISED)

    def Roll():
        total = 0
        dNumVal = int(dNum.get())
        numDVal = int(numD.get())
        
        for i in range(numDVal):
            total += randint(1, dNumVal)
        
        print(total)

    roll = Button(window, text='Roll', command=Roll)
    
    dNum.pack()
    numD.pack()
    roll.pack()
    result.pack()

    window.mainloop()
