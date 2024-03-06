from functools import partial
from tkinter import *
from tkinter import ttk
# from calculator import add, subtract, divide, multiply
from calculator import add, subtract, divide, multiply


#placeholder function for building widgets
def placeHolderFunc():
    print("you are using the placeholder function")


# empty list to hold current working value
currentValue = []
# empty list to hold values to be expressed upon
heldValues = []

# idea is:
#   when expression button is hit >> currentValue gets stored into heldValues
#           currentValue >> heldValues
#   when equal button is hit, heldValues list get iterated and each element gets solved into 
#       one value
#  - how will you let the equalButton know which function to produce??
#       


# function to add digits to label and update
def digitPress(digit):
    # add each digit to a list then add each list item into a string
    currentValue.append(str(digit))
    newLabel = ""
    for i in range(len(currentValue)):
        newLabel = newLabel + currentValue[i]
    #update label and print debug values
    calcLabel['text'] = newLabel
    print("digit: ", digit, "newValue: ", newLabel)

# zero button fuction
def pressZeroButton():
    currentValue.append("0")
    newLabel = ""
    for i in range(len(currentValue)):
        newLabel = newLabel + currentValue[i]
    calcLabel['text'] = newLabel
    print('newLabel: ', newLabel, "-- currentValue: ", currentValue)

def pressDecimalButton():
    currentValue.append(".")
    newLabel = ""
    for i in range(len(currentValue)):
        newLabel = newLabel + currentValue[i]
    calcLabel['text'] = newLabel
    print('newLabel: ', newLabel, "-- currentValue: ", currentValue)

# clear calcutor function
def clearCalc(): 
    currentValue.clear()
    calcLabel['text'] = str(0)
    print(currentValue)

# delete last entry function
def deleteLast():
    if len(currentValue) < 1:
        return
    currentValue.pop()
    newLabel = ""
    for i in range(len(currentValue)):
        newLabel = newLabel + currentValue[i]
    calcLabel['text'] = newLabel
    print('newLabel: ', newLabel, "-- currentValue: ", currentValue)

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
        ttk.Button(mainframe, text=str(b), command= lambda b = b : digitPress(b)).grid(row=(row+2), column=col)

# ZERO, DECIMAL, CLEAR buttons
    # equals (*needs function)
equalsButton = ttk.Button(mainframe, text="=", command=placeHolderFunc)
equalsButton.grid(row=5, column=2)
    # decimal (WORKS)
decimalButton = ttk.Button(mainframe, text=".", command=pressDecimalButton)
decimalButton.grid(row=5, column=1)
    # zero (WORKS)
zeroButton = ttk.Button(mainframe, text="0", command=pressZeroButton)
zeroButton.grid(row=5, column=0)
    # clear (WORKS)
clearButton = ttk.Button(mainframe, text="C", command=clearCalc)
clearButton.grid(row=1, column=2)
    # delete (WORKS)
delButton = ttk.Button(mainframe, text="DEL", command=deleteLast)
delButton.grid(row=0, column=4)


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