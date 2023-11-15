# 05A--PlatformerGameFunctions By Johnson Traevon 11/13/23 v0.2
import random



 
characters = ['goku', 'saitama', 'anya', 'aihoshino', 'kanada']



print("Welcome to Anime Abologists!\n")

print(f"Here are the character choices so far: {characters}")

characterChoice = input("Choose Your Character\n").lower()


if characterChoice in characters:
    if characterChoice == 'Goku' or characterChoice == "goku":
        print("You have chosen Goku!\n")

    elif characterChoice == "Saitama" or characterChoice == "saitama":
        print("You have chosen Saitama!\n")

    elif characterChoice == "Anya" or characterChoice == "anya":
        print("You have chosen Anya!\n")

    elif characterChoice == "AiHoshino" or characterChoice == "aihoshino":
        print("You have chosen Ai Hoshino!\n")

    elif characterChoice == "Kanada" or characterChoice == "kanada":
        print("You have chosen Kanada!\n")

else: print(f"Please choose a character from {characters}")

mapChoice = input("Choose your map\n")














# def functionOne():
#     pass

# def functionTwo(param1):
#     pass

# def functionThree(param1 = "Default Value"):
#     pass

# def functionFour(param1, param2, param3):
#     pass