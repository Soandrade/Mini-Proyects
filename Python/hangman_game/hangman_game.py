"""
@author: Soandrade
"""

import random
import os


def choose_word():
    data = open("hangman_game\words.txt", "r")
    return random.choice([i for i in data])


def clean_word():
    word = choose_word()
    word = word.upper() 
    return word.rstrip(word[-1]) #remove line break


def game():
    print("¡WELCOME TO HANGMAN GAME!")
    word = list(clean_word())
    lines = ["-" for i in range(len(word))]
   

    while True:
        print("Guess the word")
        print(*lines)
        letter = input("Enter a letter: ").upper()
        indexes = []

        for i in range(len(word)):
            if letter == word[i]:
                indexes.append(i)

        for i in indexes:
            lines[i] = letter

        print(*lines)
            
        if lines == word:
            print("Great job")
            break
        os.system("cls")



if __name__ == '__main__':
    os.system("cls")
    game()
