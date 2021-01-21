from tkinter import *
from .addThing import *

global initiatives

def initiativeTracker():
    #Declaring the window
    window = Tk()
    window.title('Initiative Tracker')
    window.geometry('300x300')

    #declaring buttons
    addThing = Button(window, text='Add a thing', command=add)

    #placing buttons
    addThing.place(x=60, y=250)

    window.mainloop()

def addToOrder(creature):
    print(creature)
