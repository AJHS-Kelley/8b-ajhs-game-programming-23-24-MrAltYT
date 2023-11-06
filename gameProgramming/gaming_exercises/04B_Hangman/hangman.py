# 04B--Hangman By Johnson Traevon 10/31/23 v1.7
import random
# words = 'aqua scp batman reconstruction rehabilitation celestial brilliant segregational continentaldrift blunder chess inaccuracy Pseudopseudohypoparathyroidism Pneumonoultramicroscopicsilicovolcanoconiosis honorificabilitudinitatibus chargoggagoggmanchauggagoggchaubunagungamaugg radiation  '.split()
# Dictionary version
# Stores in Key:Value Pairs
# Actual Dictionary word (Key) : Value (Definition)
# Uses {} to specify a dictionary
words = {'Colors': 'red black cyan purple orange blue green silver pink white'.split(),
         'Animals': 'dog cat fish lion monkey gorilla butterfly mouse bear cheetah'.split(),
         'Shapes' : 'triangle circle sphere cube tesseract orthoplex hexeract star diamond rhombus'.split(),
         'Foods':  'pasta sushi pizza cinnamonroll cookie biscut bento noodles chicken schlong'.split()}



HANGMAN_BOARD = ['''
    +---+
        |
        |
        |
    =======''','''
    +---+             
    O   |
        |
        |      
    =======''','''
    +---+
    O   |
    |   |
        |
    =======''','''
    +---+
    O   |
   /|   |
        |
    =======''','''
    +---+
    O   |
   /|\\ |
        |
    =======''','''
    +---+
    O   |
   /|\\ |
   /    |
    =======''','''
    +---+
    O   |
   /|\\ |
   / \\ |
    =======''','''
    +---+
    O   |
   /|\\ |
   /⚔︎\\ |
    =======''','''
    +---+
       
   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⡿⠋⣻⣿⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⡿⠋⣠⣾⣿⡿⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠋⣠⣾⣿⡿⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣔⣿⡿⠋⣠⣾⣿⡿⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣤⡀⠀⠀⠀⠀⣠⣾⣿⡿⠋⣠⣾⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢴⣿⡋⣠⡄⠀⠀⢸⣿⡿⠋⣠⣾⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⢿⣿⣡⣴⠶⢾⣿⣿⣾⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢹⡟⠀⠀⠀⢹⡏⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣼⣿⣤⣀⣠⡾⠃⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣴⣿⣿⠟⠉⠉⠙⢿⣿⡋⢀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣶⣶⣿⣿⠟⠁⠀⠀⠀⠀⠀⠙⢿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠐⢿⣿⣿⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠁⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
        
    ''']


# Pick Word From List
# def getRandomWord(wordList):  
#     wordIndex = random.randint(0, len(wordList) - 1)
#     # len(listName) -1 is Extremely common for working with lists
#     return wordList[wordIndex]

# Pick Word From Dictionary
def getRandomWord(wordDict):
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0, len(wordDict[wordKey])- 1)
    # len(listName) -1 is Extremely common for working with lists
    return [wordDict[wordKey][wordIndex], wordKey]

# i = 0
# while i < 3:
#     word = getRandomWord(words)
#     print(word)
#     i += 1

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_BOARD[len(missedLetters)])
    print()

    print('Missed Letters:', end = ' ')
    for eachLetter in missedLetters:
        print(eachLetter, end = ' ')
    print()
    
    blanks = '_' * len(secretWord)

    # Replace Blanks with Correct Letters
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end = ' ')
    print()


def getGuess(alreadyGuessed): 
    while True:
        print('Please guess a letter and press enter')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('You Guessed to many letters, Please enter a single letter')
        elif guess in alreadyGuessed:
            print('Letter has been guessed already, try again brotha')
        elif guess not in 'qwertyuiopasdfghjklzxcvbnm':
            print('Please guess a LETTER from the English alphabet (Sorry! I wanted to do a japanese ver)')
        else:
            return guess
        
def playAgain():
    print('Wanna play again? ( ͡° ͜ʖ ͡°)')
    return input().lower().startswith('y')

# Introduce the Game
print('Hello!, Welcome to Hangman!')

# Choose Difficulty
difficulty = 'x'
while difficulty not in 'EMHI':
    print('Please Choose Easy, Medium, Hard or Impossible.  Type the first letter then press Enter.')
    difficulty =  input().upper()
if difficulty == 'M':
    del HANGMAN_BOARD[8]
    del HANGMAN_BOARD[7]
if difficulty == 'H':
    del HANGMAN_BOARD[8]
    del HANGMAN_BOARD[7]
    del HANGMAN_BOARD[5]
    del HANGMAN_BOARD[3]
if difficulty == 'I':
    del HANGMAN_BOARD[8]
    del HANGMAN_BOARD[7]
    del HANGMAN_BOARD[5]
    del HANGMAN_BOARD[3]
    del HANGMAN_BOARD[2]
         
missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

# Main Game Loop
while True:
    print('The Secret word is from the ' + secretSet + ' category.\n')
    displayBoard(missedLetters, correctLetters, secretWord)


    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check to see if the Player won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:   # If True: 
            print('W! You found the word Amazing!(✿ ♡‿♡)')
            print('The secret word was' + secretWord)
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMAN_BOARD)- 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You Lost, Im Disappointed in you')
            print('Your Ip adress has been leaked and the cops have been called')
            print('You made this number of correct letters ' + str(len(correctLetters)))
            print('The secret word was' + secretWord)
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet = getRandomWord(words)
        else:
            break














        

