from tkinter import *
from tkinter import ttk

# function to add digits to label and update
currentDigits = []
def digitPress(digit):
    # add each digit to a list then add each list item into a string
    currentDigits.append(str(digit))
    newLabel = ""
    for i in range(len(currentDigits)):
        newLabel = newLabel + currentDigits[i]
    #update label and print debug values
    calcLabel['text'] = newLabel
    print("digit: ", digit, "newValue: ", newLabel)

#tkinter setup with added frame
root = Tk()
root.title("Python Calculator")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# calculator value ("screen")
labelValue: str = 0
calcLabel = ttk.Label(mainframe, text=labelValue, anchor=N, padding=5)
calcLabel.grid(row=0,column=2,  sticky=( E))
calcLabel['borderwidth'] = 2
calcLabel['relief'] = 'solid'

# create a 3x3 grid for numbers 1 to 9
# 1 2 3
# 4 5 6
# 7 8 9
b = 0
for row in range(3):
    for col in range(3):
        b = b + 1
        # dont understand the lambda, but it works
        ttk.Button(mainframe, text=str(b), command = lambda b = b : digitPress(b)).grid(row=(row+1), column=col)

 

root.mainloop()