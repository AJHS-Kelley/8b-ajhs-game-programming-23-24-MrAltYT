# 05A--PlatformerGameFunctions By Johnson Traevon 12/8/23 v1.1
import random

# Missing loops: for 


 
characters = ['goku', 'saitama', 'anya', 'aihoshino', 'kanada']
mapPlace = ['t.o.p', 'monster assocication', 'forger residence', 'idol stage', 'canada']
defaultHp = 3
mpsize = 3
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
else: mapSize = medium


def defaultMapStats(mpSize):

    return mpSize
mpSize = defaultMapStats(medium)

if mpSize == small:
    hearts = 3
    strength = 50
    speed = 75
    stamina = 300
elif mpSize == medium:
    hearts = 3
    strength = 75
    speed = 75
    stamina = 450
else:
    hearts = 5
    strength = 55
    speed = 75
    stamina = 600

print(f"Your current number of hearts are {hearts}\n")
print(f"Your strength is {strength}\n")
print(f"Your current speed is {speed}\n")
print(f"Your current stamina is {stamina}\n")



def baseStats():

    pass
  

    










# def functionOne():
#     pass

# def functionTwo(param1):
#     pass

# def functionThree(param1 = "Default Value"):
#     pass

# def functionFour(param1, param2, param3):
#     pass