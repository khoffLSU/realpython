# wyrdle.py

'''Python Wordle game based on tutorial on realpython.com by Geir Arne Hjelle.'''
import pathlib
import random
from string import ascii_letters
from rich.console import Console
from rich.theme import Theme

console = Console(width = 40, theme = Theme({"warning": "red on yellow"}))

def main():
    # Pre Process
    word_path = pathlib.Path(__file__).parent / "wordlist.txt"
    word = get_random_word(word_path.read_text(encoding="utf-8").split("\n"))
    guesses = ["_" * 5] * 6

    # Process (Main Loop)
    for idx in range(6):
        refresh_page(headline = f"Guess {idx + 1}")
        show_guesses(guesses, word)

        guesses[idx] = input("\nGuess word: ").upper()

        if guesses[idx] == word:
            show_guesses(guesses, word)
            print("CORRECT! YOU WIN!")
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
    words = [
        word.upper() for word in word_list
        if len(word) == 5 and all(letter in ascii_letters for letter in word)
        ]
    
    return random.choice(words)

def show_guesses(guesses, word):
    for guess in guesses:
        styled_guess = [] # initalize a list
        for letter, correct in zip(guess, word):
            if letter == correct:
                style = "bold white on green"
            elif letter in word:
                style = "bold white on yellow"
            elif letter in ascii_letters:
                style = "red on #666666"
            else:
                style = "dim"
            styled_guess.append(f"[{style}]{letter}[/]")
        
        console.print("".join(styled_guess), justify="center")

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

def refresh_page(headline):
    '''Page refresh for Wordle game'''
    console.clear()
    console.rule(f"[bold blue]:leafy_green: {headline} :leafy_green:[/]\n")

if __name__ == "__main__":
    main()