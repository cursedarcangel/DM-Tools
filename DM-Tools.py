from tkinter import *

#Defining the functions for the individual tools
def magicItem():
    from magicItemTracker import magicItemTracker as mIT
    mIT.magicItemTracker()

def initiative():
    from initiativeTracker import initiativeTracker as iT
    iT.initiativeTracker()

def dice():
    from diceRoller import diceRoller as dR
    dR.diceRoller()

def monster():
    from monsterTracker import monsterTracker as mT
    mT.monsterTracker()

def character():
    from characterTracker import characterTracker as cT
    cT.characterTracker()

#The window variable
window = Tk()
window.title('DM Tools')
window.geometry('200x150')

#The title
title = Label(window, text="The DM's toolbox", relief=RAISED)

#Declaring the buttons for each of the tools
magicItemTracker = Button(window, text='Magic Item Tracker', command=magicItem)
initiativeTracker = Button(window, text='Initiative Tracker', command=initiative)
diceRoller = Button(window, text='Roll the dice...', command=dice)
monsterTracker = Button(window, text='Monster Tracker', command=monster)
characterTracker = Button(window, text='Character Tracker', command=character)

#Packing stuff
title.pack()
magicItemTracker.pack()
initiativeTracker.pack()
diceRoller.pack()
monsterTracker.pack()

#Showing the window
window.mainloop()
