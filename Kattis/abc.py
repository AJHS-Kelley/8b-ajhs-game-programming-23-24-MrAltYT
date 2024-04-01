# input intergers
# .split() the 3 intergers in seperate variables
# casting the 3 variables to intergers
# assign values from least to greatest
# A < B < C

intergers = input()
a, b, c = intergers.split()
a = int(a)
b = int(b)
c = int(c)

if a >= b:
    a, b = b, a
    
if b >= c:
    b, c = c, b
    
if b <= a:
    b, a = a, b
# print(f"A = {a}, B = {b}, C = {c}")
    
# input the string variable
# determine order of a b and c
# create correct string
# output string

order = input()
aiHoshino = ""

for i in range(len(order)):
    if order[i] == "A":
        aiHoshino += str(a) + " "
    elif order[i] == "B":
        aiHoshino += str(b) + " "
    else: 
        aiHoshino += str(c) + " "

print(aiHoshino)