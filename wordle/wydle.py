# wyrdle.py

'''Python Wordle game based on tutorial on realpython.com by Geir Arne Hjelle.'''

# Using Walrus operator to combine condition and assignment
if (guess := input("Guess a word: ")).upper() == "SNAKE":
    print("Correct")
else:
    print("Wrong")