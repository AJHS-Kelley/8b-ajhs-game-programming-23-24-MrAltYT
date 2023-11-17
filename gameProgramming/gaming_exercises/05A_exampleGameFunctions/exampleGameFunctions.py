# 05A--PlatformerGameFunctions By Johnson Traevon 11/13/23 v0.4
import random



 
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

def character(characterChoice):
    if characterChoice in characters:
        if characterChoice == "goku":
            print("You have chosen Goku!\n")

        elif characterChoice == "saitama":
            print("You have chosen Saitama!\n")

        elif characterChoice == "anya":
            print("You have chosen Anya!\n")

        elif characterChoice == "aihoshino":
            print("You have chosen Ai Hoshino!\n")

        elif characterChoice == "kanada":
            print("You have chosen Kanada!\n")
    else: print(f"Please choose a character from {characters}")
    return characterChoice

print(f"Here are the Map choices so far: {mapPlace}\n")

mapChoice = input("Choose your map\n").lower()

if mapChoice in mapPlace:
    if mapChoice == "t.o.p":
        print("You have chosen T.O.P!\n")

    elif mapChoice == "monster assocication":
        print("You have chosen Monster Assocication!\n")

    elif mapChoice == "forger residence":
        print("You have chosen Forger Residence!\n")

    elif mapChoice == "idolstage":
        print("You have chosen Idol Stage!\n")

    elif mapChoice == "canada":
        print("You have chosen canada!\n")
else: print(f"Please choose a map.\n")



def defaultStats(mpSize, mapChoice):
    if mapChoice == mapPlace[2]:
        mpSize = small
    elif mapChoice == mapPlace[3]:
        mpSize = small
    elif mapChoice == mapPlace[0]:
        mpSize = huge
    elif mapChoice == mapPlace[1]:
        mpSize = huge
    else: mapChoice = medium
    return mpSize
mapSize = defaultStats(0, mapChoice)
print(mapSize)










# def functionOne():
#     pass

# def functionTwo(param1):
#     pass

# def functionThree(param1 = "Default Value"):
#     pass

# def functionFour(param1, param2, param3):
#     pass