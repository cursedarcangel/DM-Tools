from tkinter import *

global nameval
global initval
global acval
global hpval


#all the parameters to add a creature to initiative
def add():

    addthing = Tk()
    addthing.title('Add a creature')

    #name
    name = Label(addthing, text='Name')
    nameval = Entry(addthing)
    
    #initiative
    init = Label(addthing, text='Initiative')
    initval = Entry(addthing)

    #ac
    ac = Label(addthing, text='AC')
    acval = Entry(addthing)

    #hp
    hp = Label(addthing, text='HP')
    hpval = Entry(addthing)

    def submit():
        from .initiativeTracker import addToOrder
        stats = []
        stats.append(nameval.get())
        stats.append(initval.get())
        stats.append(acval.get())
        stats.append(hpval.get())
        addToOrder(stats)
        
    #submit button
    summit = Button(addthing, text='Submit', command=submit)
    
    #placing
    name.place(x=5, y=5)
    nameval.place(x=50, y=5)
    init.place(x=5, y=50)
    initval.place(x=65, y=50)
    ac.place(x=5, y=95)
    acval.place(x=30,y=95)
    hp.place(x=5, y=140)
    hpval.place(x=30, y=140)
    summit.place(x=60, y=165)

    addthing.mainloop()
