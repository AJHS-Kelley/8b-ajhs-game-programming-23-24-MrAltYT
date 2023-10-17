# Collections 02 Johnson Traevon v0.1 


playerInventory = []

while len(playerInventory) < 10: 
    item = input("What Item do you want to add to your Inventory\n")
    playerInventory.append(item)
playerInventory.sort()
print(playerInventory)