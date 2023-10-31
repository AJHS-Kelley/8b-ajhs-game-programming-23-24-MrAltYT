# 04B--Hangman By Johnson Traevon 10/31/23 v0.2
import random

words = 'aqua scp batman reconstruction rehabilitation celestial brilliant segregational continentaldrift blunder chess inaccuracy Pseudopseudohypoparathyroidism Pneumonoultramicroscopicsilicovolcanoconiosis honorificabilitudinitatibus chargoggagoggmanchauggagoggchaubunagungamaugg radiation '.split()
HANGMAN_BOARD = ['''
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

    
i = 0
while i < len(HANGMAN_BOARD):
    print(HANGMAN_BOARD[i])
    i += 1