# Dice Rolling Module by Johnson Traevon v0.1
import random

def roll(numDice, sizeDice):
    numRolled = 0
    sum = 0
    while numRolled < numDice:
        roll = random.randint(1, sizeDice)
        sum += roll
        numRolled += 1
    return sum 
    
def display(numDice, sizeDice):
    numRolled = 0
    sum = 0
    while numRolled < numDice:
        roll = random.randint(1, sizeDice)
        sum += roll
        print(f"Roll: {roll}\n")
        print(f"Sum: {sum}\n")
        numRolled += 1
    return sum 

def isDoubles(roll, roll2):
    if roll == roll2:
        isDoubles = True
    else:
        isDoubles = False
    return isDoubles

def isExploding(roll, sizeDice):
    if roll == sizeDice:
        isExploding = True
    else:
        isExploding = False
    return isExploding

