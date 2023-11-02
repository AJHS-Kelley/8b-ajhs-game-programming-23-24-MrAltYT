# 04B--Hangman By Johnson Traevon 10/31/23 v0.5
import random

words = 'aqua scp batman reconstruction rehabilitation celestial brilliant segregational continentaldrift blunder chess inaccuracy Pseudopseudohypoparathyroidism Pneumonoultramicroscopicsilicovolcanoconiosis honorificabilitudinitatibus chargoggagoggmanchauggagoggchaubunagungamaugg radiation '.split()
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
   /|\  |
        |
    =======''','''
    +---+
    O   |
   /|\  |
   /    |
    =======''','''
    +---+
    O   |
   /|\  |
   / \  |
    =======''']


# Pick Word From List
def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    # len(listName) -1 is Extremely common for working with lists
    return wordList[wordIndex]

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

