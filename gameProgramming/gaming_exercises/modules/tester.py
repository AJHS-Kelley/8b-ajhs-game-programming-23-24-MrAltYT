import dice
import perfmon
start = perfmon.execStart()

roll = dice.display(1,6)
roll2 = dice.display(1,6)



if dice.isExploding(roll, 6):
    print("This roll exploded!\n")
    roll += dice.roll(1,6)
    print(roll)

# if dice.isDoubles(roll, roll2):
#     print("You Rolled a double, go again!")
# else:
#     print("It wasn't a double...")

