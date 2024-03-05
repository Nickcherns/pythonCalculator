from functools import partial
from tkinter import *
from tkinter import ttk
# from calculator import add, subtract, divide, multiply

#placeholder function for building widgets
def placeHolderFunc():
    print("you are using the placeholder function")


## list is only being changed in the function, instead of actually changing the original list
##      advice was to "change the actual elements instead of temporarily adding elements"



# function to add digits to label and update
currentDigits = []
def digitPress(digit):
    # add each digit to a list then add each list item into a string
    currentDigits[-1:] = (str(digit))
    newLabel = ""
    for i in range(len(currentDigits)):
        newLabel = newLabel + currentDigits[i]
    #update label and print debug values
    calcLabel['text'] = newLabel
    print("digit: ", digit, "newValue: ", newLabel)

def clearCalc(currentDigits): 
    currentDigits = ["0"]
    calcLabel['text'] = str(0)

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
calcLabel.grid(row=0,column=0)
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

# ZERO, DECIMAL, CLEAR buttons
    # zero
zeroButton = ttk.Button(mainframe, text=0, command=placeHolderFunc)
zeroButton.grid(row=4, column=2)
    # decimal
decimalButton = ttk.Button(mainframe, text=".", command=placeHolderFunc)
decimalButton.grid(row=4, column=1)
    # clear 
clearButton = ttk.Button(mainframe, text="C", command=partial(clearCalc, currentDigits))
clearButton.grid(row=4, column=0)

# fourth row buttons (expression's)
    # ADD, SUBTRACT, DIVIDE, MULTIPLY
divideButton = ttk.Button(mainframe, text="÷", command=placeHolderFunc)
divideButton.grid(row=1,column=4)

multiplyButton = ttk.Button(mainframe, text="×", command=placeHolderFunc)
multiplyButton.grid(row=2,column=4)

subtractButton = ttk.Button(mainframe, text="−", command=placeHolderFunc)
subtractButton.grid(row=3,column=4)

addButton = ttk.Button(mainframe, text="+", command=placeHolderFunc)
addButton.grid(row=4,column=4)


root.mainloop()