# Import libraries
from tkinter import *
from tkinter import ttk


window = Tk()
window.geometry('500x700')


# Creating a variables for prices
sctk = 40
mvtk = 75
thtk = 100

# Creating Tkinter widgets
tkvar = StringVar()
cellno = Entry(window, width=20)
tkcat = ttk.Combobox(window, textvariable=tkvar, width=20, value=["Soccer", "Movie", "Theater"])
nrtk = ttk.Spinbox(window, from_=0, to=20, state="readonly")
celllb = Label(window, text="Cellphone number:")
catlb = Label(window, text="Ticket Category:")
nrlb = Label(window, text="Number of tickets:")
anslb = Label(window)


#Creating class
class clsTiketSales:
  def __init__(self, celno, nrtkts, price):
        self.celno = celno
        self.nrtkts = nrtkts
        self.price = price
        return

 # Creates function for button
def calc():
    # Passes through class
    tksale = clsTiketSales(cellno.get(), float(nrtk.get()), tkcat.get())

    # Desicion tree
    if tkcat.get() == "Soccer":
        scprice = sctk * int(nrtk.get()) + (14/100)
        anslb.config(text="Price:"+ str(scprice) + "\n" + "tickets:"+str(nrtk.get()) + "\n" +"Number:"+ str(cellno.get()))
    if tkcat.get() == "Movie":
        mvprice = mvtk * int(nrtk.get()) + (14/100)
        anslb.config(text="Price:"+ str(mvprice) + "\n" + "tickets:"+str(nrtk.get()) + "\n" +"Number:"+ str(cellno.get()))
    if tkcat.get() == "Theater":
        thprice = thtk * int(nrtk.get()) + (14/100)
        anslb.config(text="Price:"+ str(scprice) + "\n" + "tickets:"+str(nrtk.get()) + "\n" +"Number:"+ str(cellno.get()))



def clear_all():
    cellno.delete(0,END)
    tkvar = StringVar()
    tkvar.set(0)
    tkcat.config(textvariable=tkvar)


# function

#Creating button
tkbtn = Button(window, text="calculate", command=calc, width=20, height=1)

# Adds widgets
celllb.grid(row=0, column=0, sticky=W)
catlb.grid(row=2, column=0, sticky=W)
nrlb.grid(row=5, column=0, sticky=W)
cellno.grid(row=0, column=1)
tkcat.grid(row=2, column=1)
nrtk.grid(row=5, column=1)
anslb.grid(row=6, column=0)
tkbtn.grid(row=8, column=0)


clear_entry= Button(window, text= "Clear", command = clear_all)
clear_entry.grid(row = 8, column = 1)
window.mainloop()
