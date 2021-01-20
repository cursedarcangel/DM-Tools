from tkinter import *

#Defining the functions for the individual tools
def magicItem():
    print('Tracking magic items')

def initiative():
    print('Initiating tracker')

def dice():
    print('Hey a 20!')

def monster():
    print('Rawr a monster is coming')

#The window variable
window = Tk()

#The title
name = StringVar()
title = Label(window, textvariable=name, relief=RAISED)
name.set("The DM's toolbox")

#Declaring the buttons for each of the tools
magicItemTracker = Button(window, text='Magic Item Tracker', command=magicItem)
initiativeTracker = Button(window, text='Initiative Tracker', command=initiative)
diceRoller = Button(window, text='Roll the dice...', command=dice)
monsterTracker = Button(window, text='Monster Tracker', command=monster)

#Packing stuff
title.pack()
magicItemTracker.pack()
initiativeTracker.pack()
diceRoller.pack()
monsterTracker.pack()

#Showing the window
window.mainloop()
