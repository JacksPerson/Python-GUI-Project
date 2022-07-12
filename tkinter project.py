from tkinter import *
from tkinter import ttk
from datetime import *

##Modules
def startClick():
    startTime = Label(root, text=comm1)
    startTime.pack()
    return


##Variables
root = Tk()
now = datetime.now()
analysts = ['K. Barthauer', 'J. Zwarycz']
nowString = now.strftime("%d/%m/%Y %H:%M:%S")
startButton = Button(root, text = 'Begin Investigation', padx = 50, pady = 25, command = startClick)
frame = Frame(root, padx = 10, pady = 10)
Combo = ttk.Combobox(frame, values = analysts)
comm1 = 'Investigation initiated at: ' + nowString

root.title('S.O.C.R.A.T.E.S.')
##root.iconbitmap('C:\Users\KBarthauer\AppData\Local\Programs\Python\Python310\seal.ico')
root.geometry('500x500')

frame.pack()
Combo.set('Analyst Name')
Combo.pack(padx = 5, pady = 5)


startButton.pack()


root.mainloop()
