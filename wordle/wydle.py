# wyrdle.py

'''Python Wordle game based on tutorial on realpython.com by Geir Arne Hjelle.'''
import pathlib
import random
from string import ascii_letters
from rich.console import Console
from rich.theme import Theme

console = Console(width = 40, theme = Theme({"warning": "red on yellow"}))

NUM_LETTERS = 5
NUM_GUESSES = 6
WORDS_PATH = pathlib.Path(__file__).parent / "wordlist.txt"

def main():
    # Pre Process
    word_path = pathlib.Path(__file__).parent / "wordlist.txt"
    word = get_random_word(word_path.read_text(encoding="utf-8").split("\n"))
    guesses = ["_" * NUM_LETTERS] * NUM_GUESSES

    # Process (Main Loop)
    for idx in range(NUM_GUESSES):
        refresh_page(headline = f"Guess {idx + 1}")
        show_guesses(guesses, word)

        guesses[idx] = guess_word(previous_guesses=guesses[:idx])
        if guesses[idx] == word:
            break
    
    # Post Process
    game_over(guesses, word, guessed_correctly = (guesses[idx] == word))


def get_random_word(word_list):
    '''Pull random word from text corpus for game

    ## Example:
    
    >>> get_random_word(["snake", "worm", "it'll"])
    'SNAKE'
    '''
    if words := [
        word.upper() for word in word_list
        if len(word) == 5 and all(letter in ascii_letters for letter in word)
        ]:
            return random.choice(words)
    else:
        console.print("No words of length 5 in word list", style = "warning")
        raise SystemExit()

def show_guesses(guesses, word):
    for guess in guesses:
        styled_guess = [] # initalize a list
        for letter, correct in zip(guess, word):
            if letter == correct:
                style = "bold white on green"
            elif letter in word:
                style = "bold white on blue"
            elif letter in ascii_letters:
                style = "bold white on red"
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

def game_over(guesses, word, guessed_correctly):
    '''Finish game message upom losing'''
    refresh_page(headline="Game Over")
    show_guesses(guesses, word)
    
    if guessed_correctly:
        console.print(f"\n[bold white on green]Correct, the word is {word}[/]")
    else:
        console.print(f"\n[bold white on red]Sorry, the word was {word}[/]")

def refresh_page(headline):
    '''Page refresh for Wordle game'''
    console.clear()
    console.rule(f"[bold blue]:leafy_green: {headline} :leafy_green:[/]\n")

def guess_word(previous_guesses):
    '''Function to handle user guess and give feedback'''
    guess = console.input("\nGuess word:").upper()

    if guess in previous_guesses:
        console.print(f"You've already guessed {guess}.", style = "warning")
        return guess_word(previous_guesses)
    
    if len(guess) < 5:
        console.print("Your guess must be 5 letters.", style = "warning")
        return guess_word(previous_guesses)
    
    if any((invalid := letter) not in ascii_letters for letter in guess):
        console.print(
            f"Invalid letter: {invalid}. Please use English letters.",
            style = "warning"
        )
        return guess_word(previous_guesses)

    return guess

if __name__ == "__main__":
    main()