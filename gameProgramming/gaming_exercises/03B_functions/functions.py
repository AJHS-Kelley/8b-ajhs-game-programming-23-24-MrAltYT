# 8B 03_functions Johnson Traevon, 10/25/2023 v0.3
import random
# Function -- A named piece of code that can be used easily.
# Function signature -- Syntax for creating a new function.
def exampleFunctionA(): # no parameters
    count = 0
    num = int(input("How many times do you want to be wished happy birthday?"))
    while count < num:
        print("Happy Birthday!\n")
        count += 1

def exampleFunctionB(num, count):
    while count < num:
        print("Happy Birthday!\n")
        count += 1
    


# If a function requires parameters, your code will crash without them!
# Returning a Function is known as calling a function
# exampleFunctionA()
# exampleFunctionB(5, 0)

def rollDice(numDice, sizeDice):
    numRolled = 0
    sum = 0
    while numRolled < numDice:
        roll = random.randint(1, sizeDice)
        sum += roll
        print(f"Roll: {roll}\n")
        print(f"Sum: {sum}\n")
        numRolled += 1
    return sum # return will imediantely exit a loop, function, if/else block. 
rollDice(3, 6)
# rollDice(1, 20)
constitutionPlayer = rollDice(3, 6)
dexterityPlayer = rollDice(3, 6)
intelligencePlayer = rollDice(3, 6)
wisdomPlayer = rollDice(3, 6)
charisma = rollDice(3, 6)


print(constitutionPlayer)
print(dexterityPlayer)
print(intelligencePlayer)
print(wisdomPlayer)
print(charisma)



def getStats():
    playerStats =[0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0]
    i = 0
    while i < len(playerStats):
    
        playerStats[i] = rollDice(3, 6)
        i += 1

    print(playerStats)
    
getStats()