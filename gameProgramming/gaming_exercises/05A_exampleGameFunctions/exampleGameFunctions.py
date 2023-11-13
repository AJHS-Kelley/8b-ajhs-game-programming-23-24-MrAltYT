# 05A--PlatformerGameFunctions By Johnson Traevon 11/13/23 v0.1
import random

def functionOne():
    pass

def functionTwo(param1):
    pass

def functionThree(param1 = "Default Value"):
    pass

def functionFour(param1, param2, param3):
    pass
 
characters = ["Goku Saitama Anya AiHoshino Kanada"] 


print("Welcome to Anime Abologists!")
characterChoice = input("Choose Your Character")


def startGame(characterChoice):
    if characterChoice == "Goku" or "goku":
        print("You have chosen Goku!\n")
    elif characterChoice == "Saitama" or "saitama":
        print("You have chosen Saitama!\n")
    elif characterChoice == "Anya" or "anya":
        print("You have chosen Anya!\n")
    elif characterChoice == "AiHoshino" or "aihoshino":
        print("You have chosen Ai Hoshino!\n")
    elif characterChoice == "Kanada" or "kanada":
        print("You have chosen Kanada!\n")
    return startGame

startGame(characters)