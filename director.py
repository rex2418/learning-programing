def giveName(userInput):
    name = input().upper()
    print("good to meet you " + name)
    return name

def firstChoice(userInput, name):
    if userInput == "L":
        print(f"{name} has found the woods")
    elif userInput == "R":
        print(f"{name} has found the town")
    else:
        print("please enter L or R")
        firstChoice(input().upper())
