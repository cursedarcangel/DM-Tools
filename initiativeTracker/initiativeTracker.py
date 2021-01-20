from tkinter import *

def add():
    print('Thing added')

window = Tk()
window.title('Initiative Tracker')
window.geometry('300x300')

addThing = Button(window, text='Add a thing to initiative', command=add)

addThing.place(x=60, y=250)

window.mainloop()
