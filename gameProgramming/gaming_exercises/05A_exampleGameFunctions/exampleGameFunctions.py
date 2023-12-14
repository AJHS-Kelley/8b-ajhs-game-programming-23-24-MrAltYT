# 05A--PlatformerGameFunctions By Johnson Traevon 12/8/23 v1.1
import random

# Missing loops: for 


 
characters = ['goku', 'saitama', 'anya', 'aihoshino', 'kanada']
mapPlace = ['t.o.p', 'monster assocication', 'forger residence', 'idol stage', 'canada']
items = ['Kamehameha', 'Fist of flowing water crushing rock', 'Supressed pistol', 'Star wand', 'Maplebranch']
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
    mapChoice = input("Choose your map\n")

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

def defaultMapStats(mpSize):

    return mpSize
mpSize = defaultMapStats(medium)

for mapChoice in mapPlace:
    if mapChoice in mapPlace == 't.o.p':
        mpSize = huge
    elif mapChoice in mapPlace == 'monster assocication':
        mpSize = defaultMapStats
    elif mapChoice in mapPlace == 'forger residence':
        mpSize = defaultMapStats
    elif mapChoice in mapPlace == 'idol stage':
        mpSize = small
    elif mapChoice in mapPlace == 'canada':
        mpSize = huge
    else: mapChoice = "who knows?"




if mpSize == small:
    hearts = 3
    strength = 50
    speed = 75
    stamina = 300
elif mpSize == huge:
    hearts = 5
    strength = 100
    speed = 75
    stamina = 600
else:
    hearts = 3
    strength = 100
    speed = 75
    stamina = 450


print(f"Your current number of hearts are {hearts}\n")
print(f"Your current strength is {strength}\n")
print(f"Your current speed is {speed}\n")
print(f"Your current stamina is {stamina}\n")

print("You have hit a item block!\n")

def itemRoll(roll, block):
    roll = random.randint(1, 6)


  

    










# def functionOne():
#     pass

# def functionTwo(param1):
#     pass

# def functionThree(param1 = "Default Value"):
#     pass

# def functionFour(param1, param2, param3):
#     pass