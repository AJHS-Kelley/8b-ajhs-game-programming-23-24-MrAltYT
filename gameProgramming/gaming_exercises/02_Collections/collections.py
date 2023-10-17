# Collections 02 Johnson Traevon v0.4

""" 
playerInventory = []

while len(playerInventory) < 10: 
    item = input("What Item do you want to add to your Inventory\n")
    playerInventory.append
playerInventory.sort()
print(playerInventory)

while len(playerInventory) > 5:
    item = input("What Item do you want to use from your Inventory\n")
    playerInventory.remove(item)
playerInventory.sort()
print(playerInventory) 
     """

""" doorKeys = ["purple",
        "aqua",
        "ruby",
        "emerald",
        "gold",
        "silver"
]

## print(f"{doorKeys}\n These are the keys you can choose from.\n")
key = input("Which color key do you need to unlock the door?")
if key in doorKeys:
    print("You have the correct Key!\n")
else:
    print(f"You don't have any of these keys\n {doorKeys}.\n") """

weaponList = [
    True, # Sword of Oblivion
    False, # Spear of Recreation
    True, # Magnus Carlsen Shirtless
    True, # Traevon's Banana
    False, # Nazi's Gernade
    False, # Minecraft's Command Block
    True, # Chess King
]

weaponNum = 0
while weaponNum < len(weaponList):
    if weaponNum == 0 and weaponList[0] == True: 
        print("You are wielding a Destructours Sword.\n")
    if weaponNum == 0 and weaponList[1] == True: 
        print("You are wielding A Beautiful Spear.\n")
    if weaponNum == 0 and weaponList[2] == True: 
        print("You have something Special.\n")
    if weaponNum == 0 and weaponList[3] == True: 
        print("You are wielding something interesting...\n")
    if weaponNum == 0 and weaponList[4] == True: 
        print("Yo Watch out!\n")
    if weaponNum == 0 and weaponList[5] == True: 
        print("Whoa!!! Check your inventory dude!\n")
    if weaponNum == 0 and weaponList[6] == True: 
        print("You have played the Kings Gambit.\n")
    weaponNum += 1
    
