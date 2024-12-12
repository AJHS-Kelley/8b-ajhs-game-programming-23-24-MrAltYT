# Data types and Operators, Johnson Traevon, v0.7

# Variable Rules
# CANNOT START WITH A NUMBER!!
# CANNOT USE BUILT-IN KEYWORDS AS VARIABLE
# VARIABLE NAME SHOULD DISCRIBE THE DATA BEING STORED
# snake_case variables use_ to separate words, all lower case
# camelCase variables do not use spaces, 1st word lowercase, rest is uppercased

# Spring literal Examples
playerName = "Ai Hoshino"
emptyString= ""
spaceString = " "
Ai_Children = "Ruby Hoshino and Aqua Hoshino"

# Interger Data Types
health =  100
extraLives = 5
temperature = -17
Ability =  "kekeigenkai"

# Floating Point Data Types
pi = 3.141592678
lapTime = 3.5
velocity = -2.0
Age = 16

# Boolean Data Types 
isFireType = False
weaponEquipped = True
pvpEnabled = False
weaponExsistance = False

# # Arithmetic Operators
# # PEMDAS APPLIES JUST LIKE IN MATH CLASS
# print(3 + 3) # Addition
# print(10 - 1) # Subtraction
# print(3 * -6)# Mutiplication 
# print(10 / 5) # Division
# print(6 ** 9) # Exponets
# print(15 % 7) # Modulus -- Divides, then returns the remainder, most commonly used to determine even/odd

# Comparison Operators 
# Evaluate the expression then return True or False
print(5 > 3) # Greater Than
print(7 >= -1) # Greater than or equal to
print(-1 < 21) # Less than
print(7 <= 7) # Less than or equal
print(5 == 0) # Is equal to
print(-99 != 99) # Is not equal to

# Assignment Operators
animeSolos = "myValue" #Assign variable on the left the value on the right, throw out any current value
opm = (20 + 5)

# Addition Assignment 
myWallet = 0
myWallet += 1
myWallet += 6
print(myWallet)

# Same Effect
x = 0
x += 1
x = x + 1

# Logical operators
print(3 > 5 and 4 < 3) # requires all expressions to be true
print(3 > 2 and 4 < 3)
print(3 > 2 and 4 != 3)
print(3 > 2 and 4 != 3 and "Ai Hoshino" == "Purple" and "Ruby Hoshino and Aqua Hoshino" == -5)
# when writing and expressions, put the value most likely to be False first!

# Logical OR -- Requires ONE exspression to be True
print(5 > 2 or 2 < -2)
print( 3 != 3 or 5 == 5)

# AND OR Combined
print(3 > 2 and 4 <3 or 5 != 7)
print(True and False or True)

# NOT Logical Operator
print(not (3 >2))
print(not (not (not (5 != 3))))

























