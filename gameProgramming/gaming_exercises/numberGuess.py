# Select the secret Number from a given range.
# Player must guess the number.
# Compare guess to the secret number.
# What happens if the guess is wrong?
    # Tell them the guess is wrong.
    # Tell them the number of guesses left
    # Tell them if too High or to Low.
# What happens if the guess is right?
    # Tell them guess is correct.
    # Award a point.
# What happens if the player runs out of guesses?
    # Tell them if they lost that round.
    # Award the CPU the point.
# Check to see if player or CPU has >= 3 points, if so they win.

import random # import the random module to our code

# DECLARATIONS
secretNumber = -1
playerGuess = -1
playerScore = 0
cpuScore = 0
numGuesses = 0
playerName = ""
difficulty = ""
rangeMin = -1
rangeMax = -1
numAttempts = -1
Difficulty = "Easy, easy, Normal, normal, Hard, hard, Impossible, impossible"




print("""
        *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
        |                             |
        |        Guess a Number       |
        |          Traevon J          |
        |            2023             |
        |                             |
        |                             |
        |                             |
        |                             |
        *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
      """)

# CPU SECRET NUMBER GENERATOR
secretNumber = random.randint(1, 20)
#print(secretNumber)

print(input("Please Input Your Name.\n\n"))
Difficulty = print(input("Choose Your Difficulty\n"))
# Game Loop


while playerScore != 3 or cpuScore != 3: # Start of Match (Game)
#    pass -- Tells python to skip this line of code   
#    Difficulty code need to be Before the round starts
    print(f"Player Score: {playerScore}\nCPU Score: {cpuScore}.\n")
    secretNumber = random.randint(1, 25)
    # Whenever you assign a specific value to something, it's called "hard coded"
    #print(secretNumber)

    numGuesses = 0
    for guesses in range(3):
        # Put Difficulty CODE
        if Difficulty == "Impossible" or Difficulty == "impossible":
            rangeMin = 0
            rangeMax = 1000
            numAttempts = 8
            print("You have chosen impossible!\n")
            print("You need to guess a number from 0 to 1000 and you have eight guesses.\n if you guess it right, you get a point\n if you can't guess it in eight guesses, the CPU gets a point\n")

        elif Difficulty == "Hard" or Difficulty == "hard":
            rangeMin = 0
            rangeMax = 375
            numAttempts = 6
            print("You have chosen Hard!\n")
            print("You need to guess a number from 0 to 375 and you have six guesses.\n if you guess it right, you get a point\n if you can't guess it in six guesses, the CPU gets a point\n")

        elif Difficulty == "Normal" or Difficulty == "normal":
            rangeMin = 0
            rangeMax = 75
            numAttempts = 4
            print("You have chosen Normal!\n")
            print("You need to guess a number from 0 to 75 and you have four guesses.\n if you guess it right, you get a point\n if you can't guess it in four guesses, the CPU gets a point\n")

        else:
            rangeMin = 0
            rangeMax = 25
            numAttempts = 3
            print("You have chosen Easy!\n")
            print(f"You need to guess a number from {rangeMin} to {rangeMax} and you have {numAttempts} guesses.\n if you guess it right, you get a point\n if you can't guess it in three guesses, the CPU gets a point\n")

        print(f"You have {3 - numGuesses} guesses remaining.\n")
        playerGuess = int(input("Tpye a number from 1 to 20 and press Enter.\n"))
        # input saves everything you type in as a string by default.
        # int() will convert to a interger
        # float() will convert to a float
        print(f"You have chosen {playerGuess}.\n Let's see if you're right!\n")
        if playerGuess == secretNumber:
            print("GoodJob! You got it right!!\n")
            playerScore += 1
            break # IMEDIANTELY EXIT ANY LOOP YOU ARE IN!
        else: 
            print("Aww you failed!\n It's okay, you can always retry!\n")
            if playerGuess > secretNumber:
                print("Your guess was a bit to high btw!\n")
            else:
                print("Your guess was a bit to low, Sorry!")
            numGuesses += 1
   
    if playerGuess != secretNumber:
        cpuScore += 1
        print("The CPU wins a point since you ran out of guesses")
        break
        
    if playerScore >= 3:
        print("Winner, Winner, Chicken Dinner! You scored 3 points first! You earned my Love!\n")
    else:
        if cpuScore >= 3:
            print("Yo, you lost to a computer. You are a scrub\n")
