import math
def NumberGuessingGame():
    firstq = input("Hello there! Are you ready to have your mind read by me? \n A. Yes! \n B. Nah \n")
    if (firstq == "A." or firstq == "A"):
        (MovetoSecond())
    elif (firstq == "B." or firstq == "B"):
        return "Alright, bye!"
    else:
        return "Not a valid input"

def MovetoSecond():
    secondq = input("First, think of any number between 1 and 10 \n Respond with 'Done' once you complete this \n")
    if (secondq == "Done" or secondq == "Done." or secondq == "done"):
        (MovetoThird())
    else:
        print("Not valid. Try again")
        MovetoSecond()

def MovetoThird():
    thirdq = input("Now, multiply your number by 2. \n Type 'Done' once again \n")
    if (thirdq == "Done" or thirdq == "Done." or thirdq == "done"):
        fourthq = input("Now, multiply this new number by 5 and tpe 'Done' once again \n")
        if (fourthq == "Done" or fourthq == "Done." or fourthq == "done"):
            (MovetoFifth())
        else:
            print("Not valid. Try again")
            MovetoThird()
    else:
        print("Not valid. Try again")
        MovetoThird()

def MovetoFifth():
    fifthq = input("Now, divide this current number by your original one.\n Finally, subtract 7 from this.\n Type 'Done' \n")
    if (fifthq == "Done" or fifthq == "Done." or fifthq == "done"):
        print("Your answer is 3!")
    else:
        print("Not valid. Try again")
        MovetoFifth()
    
(NumberGuessingGame())
