# 8B 03_functions Johnson Traevon, 10/23/2023 v0.1

# Function -- A named piece of code that can be used easily.
# Function signature -- Syntax for creating a new function.
def exampleFunctionA(): # no parameters
    count = 0
    num = int(input("How many times do you want to be wished happy birthday?"))
    while count < num:
        print("Happy Birthday!\n")
        count += 1

def exampleFunctionB(num, count):
    while count < num:
        print("Happy Birthday!\n")
        count += 1
    


# If a function requires parameters, your code will crash without them!
# Returning a Function is known as calling a function
exampleFunctionA()
examplefunctionB(5, 0)