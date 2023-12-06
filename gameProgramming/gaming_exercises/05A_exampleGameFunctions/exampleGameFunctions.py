# 05A--PlatformerGameFunctions By Johnson Traevon 11/13/23 v0.4
import random

# Missing loops: for 


 
characters = ['goku', 'saitama', 'anya', 'aihoshino', 'kanada']
mapPlace = ['t.o.p', 'monster assocication', 'forger residence', 'idol stage', 'canada']
defaultHp = 3
mapsize = 0
small = 1
medium = 3
huge = 5



print("Welcome to Anime Abologists!\n")

print(f"Here are the character choices so far: {characters}")

characterChoice = input("Choose Your Character\n").lower()

while characterChoice not in characters:
    print("Invalid Character...\n")
    characterChoice = input("Choose Your Character\n").lower()

    

print(f"Here are the Map choices so far: {mapPlace}\n")

mapChoice = input("Choose your map\n").lower()

while mapChoice not in mapPlace:
    print("I can't find your map...\n")
    mapChoice = input("Choose your map")

while mapChoice in mapPlace:
    if mapChoice == "t.o.p":
        print("You have chosen T.O.P!\n")
    elif mapChoice == "monster assocication":
        print("You have chosen Monster Assocication!\n")
    elif mapChoice == "forger residence":
        print("You have chosen Forger Residence!\n")
    elif mapChoice == "idol stage":
        print("You have chosen Idol Stage!\n")
    elif mapChoice == "canada":
        print("You have chosen canada!\n")
    else: 
        print("Your map was not found.\n")
    break

if mapChoice == mapPlace[2]:
    mpSize = small
elif mapChoice == mapPlace[3]:
    mpSize = small
elif mapChoice == mapPlace[0]:
    mpSize = huge
elif mapChoice == mapPlace[1]:
    mpSize = huge
else: mapChoice = medium


def defaultMapStats(mpSize):

    return mpSize
mpSize = defaultMapStats(3)


def defaultStats(hearts, strength, speed, stamina):
    if mpSize == small:
        hearts = 3
        strength = 50
        speed = 75
        stamina = 300
    elif mpSize == medium:
    

    pass










# def functionOne():
#     pass

# def functionTwo(param1):
#     pass

# def functionThree(param1 = "Default Value"):
#     pass

# def functionFour(param1, param2, param3):
#     pass