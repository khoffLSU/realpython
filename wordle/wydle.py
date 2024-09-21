# wyrdle.py

'''Python Wordle game based on tutorial on realpython.com by Geir Arne Hjelle.'''
import pathlib
import random
from string import ascii_letters
    

def main():
    # Pre Process
    word_path = pathlib.Path(__file__).parent / "wordlist.txt"
    word = get_random_word(word_path.read_text(encoding="utf-8").split("\n"))

    # Process (Main Loop)
    for guess_num in range(1,7):
        guess = input(f"\n{guess_num}. Guess a word: ").upper()

        show_guess(guess, word)

        if guess == word:
            break
    
    # Post Process
    else:
        game_over(word)


def get_random_word(word_list):
    '''Pull random word from text corpus for game
      ## Example:
      >>> get_random_word(["snake", "worm", "it'll"])
      'SNAKE' 
    '''
    words = [word.upper() for word in word_list
         if len(word) == 5 and all(letter in ascii_letters for letter in word)
         ]
    
    return random.choice(words)

def show_guess(guess, word):
    '''Show break down of word guessed versus secret word in terms of letters
       Correct, missplaced and incorrect letters
       
       ## Example:

       >>> show_guess("CRANE","SNAKE")
       Correct letters: A, E
       Misplaced letters: N
       Wrong letters: C, R
       '''
    correct_letters = {letter for letter,correct in zip(guess,word) if letter == correct}
    missplaced_letters = set(guess)&set(word) - correct_letters
    incorrect_letters = set(guess)-set(word)
    print("Correct letters:",", ".join(sorted(correct_letters)))
    print("Misplaced letters:",", ".join(sorted(missplaced_letters)))
    print("Wrong letters:",", ".join(sorted(incorrect_letters)))

def game_over(word):
    '''Finish game message upom losing'''
    print(f'The word was {word}')

if __name__ == "__main__":
    main()