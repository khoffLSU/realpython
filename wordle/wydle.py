# wyrdle.py

'''Python Wordle game based on tutorial on realpython.com by Geir Arne Hjelle.'''
import pathlib
import random


WORD = "SNAKE"

for guess_num in range(1,7):
    # Using Walrus operator to combine condition and assignment
    guess = input(f"\n{guess_num} Guess a word: ").upper()
    if guess == WORD:
        print("Correct")
        break
    
    print("Wrong")

    correct_letters = {letter for letter,correct in zip(guess,WORD) if letter == correct}
    missplaced_letters = set(guess)&set(WORD) - correct_letters
    incorrect_letters = set(guess)-set(WORD)
    print("Correct Letters: ",", ".join(correct_letters))
    print("Missplaced Letters: ",", ".join(missplaced_letters))
    print("Incorrect Letters: ",", ".join(incorrect_letters))