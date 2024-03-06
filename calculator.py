def lowerCaseFilter(word):
    strWord = str(word)
    finalWord = strWord.lower()
    return finalWord


def collectInputAndSolve(solveFunction):
#    create function that you can pass a equation function 
#      that collects x and y and prints then returns to menu
    x = input("Please enter your first number: \n")
    y = input("Please enter your second number: \n")
    x, y = int(x), int(y)
    print("Solution: ", solveFunction(x, y))

    while(1 > 0):
        returnAnswer = input("Return to menu? \n")
        finalAnswer = lowerCaseFilter(returnAnswer)
        if finalAnswer == "yes":
            mainMenu()
            break;
        elif finalAnswer == "no":
            exit()
            break;
        else: 
            print("\nPlease enter a valid answer (yes / no): ")

def add(x, y): 
    return (x + y)

def subtract(x, y):
    return (x - y)

def multiply(x, y):
    return (x * y)

def divide(x, y):
    return (x / y)

def mainMenu():
    print("\nCalculator")
    print("")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    userInput = input("Choose an option: ")

    if userInput == "1":
        collectInputAndSolve(add)
    elif userInput == "2":
        collectInputAndSolve(subtract)
    elif userInput == "3":
        collectInputAndSolve(multiply)
    elif userInput == "4":
        collectInputAndSolve(divide)
    else:
        print("Please select a valid option...")

# mainMenu()

