# Control Flow, Johnson Traevon, v0.6.5
# Declarations

favColor = "Crimson"
luckyNumber = 69
myGPA = 3.1
myAge = 16
pineappleOnPizza = True
favCharacter = "Ai Hoshino"

# # If Statements - Check for a condition to be True/False, do something if true
# if favColor == "Crimson":
#     print("Your hot fr")

# if favCharacter == "Ai Hoshino":
#     print("W manz/womanz")

# # If-else statement -- Check for a condition, do something if false
# if myGPA >= 3.0:
#     print("Congratulations on making the Honor Roll")
# else: 
#     print("Sorry!! Better Luck Next Year T-T")

# # If - elif - else statements -- Checks for mutiple conditions, if it something is True
# if myAge > 65:
#     print("Congrats on Retiring!!")
# elif myAge > 50:
#     print("Congrats on your $1000!!")
# else:
#     print("You'll get there eventually no worries!")
# # 1 If, 1 Else, any number of elif allowed

# # Nested if - elif - else Statements
# if myAge > 15:
#     print("Your eligible for a license!")
#     if myGPA >= 3.5:
#         print("You Qualify For a New Car!!")
#     elif myGPA > 2.0:
#         print("You Qualify For $500 off a Car!!")
#     else:
#         print("You get nothing L")
# else:
#     print("You are not yet old enough to drive")

# # When doing if-elif-else statements, check for the highest values first!!
# if myGPA <= 1.5:
#     print("You are in danger of failing for the year")
# elif myGPA >= 2.0:
#     print("You are on the track to gradualte")
# elif myGPA >= 3.0:
#     print("You Qualify for some scholarship money!!")
# elif myGPA > 3.99:
#     print("You Qualifyfor Bright Futures 100 percent scholarship!")
# else:
#     print("GPA was not calculated. Please try again later")

# white loop -- think of playing musical chairs -- used when you do not know how many iterations
# interation = one complete trip through a loop
# Parentheses ()
# Brackets []
# Braces {}
# Angle Brackets <>

x = 0
while x < 100:
    print(f"Ai's Love is currently equal to {x}")
    x += 3

while x >= 0:
    print(f"Ai's Love is currently equal to {x}")
    x -= 3

# for Loop --  Think 'Go fish', used when you know number of interations needed.

# Parentheses ()
# Brackets []
# Braces {}
# Angle Brackets <>
print("For Loop Starts Here")
for i in range(10): # i = iterable variable
    print(i) 

print("Even or Odd Loop!")
for i in range(101):
    print(i)
    if i % 2 == 0:
        print("That number is Even")
    else:
        print("That number is Odd") 























