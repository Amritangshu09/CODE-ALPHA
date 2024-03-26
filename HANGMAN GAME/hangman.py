import random
import string
import tkinter as tk
from tkinter import messagebox

def load_words(file_path):
    """
    Load words from a file and return a list of words.
    """
    with open(file_path, 'r') as file:
        words = [word.strip().lower() for word in file.readlines()]
    return words

def get_word(word_list):
    """
    Returns a random word from the list of words.
    """
    return random.choice(word_list)

def play_hangman(word_list):
    """
    Main function to play the Hangman game.
    """
    word = get_word(word_list)
    word_letters = set(word)
    alphabet = set(string.ascii_lowercase)
    used_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 5

    def guess_letter(letter):
        nonlocal word_letters, used_letters, incorrect_guesses

        if letter in used_letters:
            result_label.config(text="You have already used that letter. Please try again.")
        else:
            used_letters.add(letter)
            if letter in word_letters:
                word_letters.remove(letter)
            else:
                incorrect_guesses += 1
            update_display()

    def update_display():
        word_progress = "".join(letter if letter in used_letters else "_" for letter in word)
        word_label.config(text=word_progress)
        used_label.config(text="Used letters: " + " ".join(used_letters))
        guesses_left = max_incorrect_guesses - incorrect_guesses
        result_label.config(text=f"You have {guesses_left} guesses left.")

        if len(word_letters) == 0:
            result_label.config(text=f"Congratulations! You guessed the word '{word}'.")
            play_again(True)
        elif incorrect_guesses >= max_incorrect_guesses:
            result_label.config(text=f"Sorry, you ran out of guesses. The word was '{word}'.")
            play_again(False)

    def play_again(won):
        answer = messagebox.askyesno("Play Again", f"You {'won' if won else 'lost'} the game.\nWould you like to play again?")
        if answer:
            start_new_game(word_list)
        else:
            window.quit()

    def start_new_game(word_list):
        nonlocal word, word_letters, used_letters, incorrect_guesses
        word = get_word(word_list)
        word_letters = set(word)
        used_letters.clear()
        incorrect_guesses = 0
        update_display()
        disable_buttons(False)

    def disable_buttons(disabled):
        for button in letter_buttons:
            button.config(state=tk.DISABLED if disabled else tk.NORMAL)

    # Create the main window
    window = tk.Tk()
    window.title("Hangman Game")

    # Create labels
    word_label = tk.Label(window, font=("Arial", 16))
    word_label.pack(pady=10)
    used_label = tk.Label(window, font=("Arial", 12))
    used_label.pack(pady=5)
    result_label = tk.Label(window, font=("Arial", 12))
    result_label.pack(pady=5)

    # Create letter buttons
    letter_buttons = []
    for letter in string.ascii_lowercase:
        button = tk.Button(window, text=letter.upper(), font=("Arial", 12), width=2,
                            command=lambda x=letter: guess_letter(x))
        button.pack(side=tk.LEFT, padx=2, pady=2)
        letter_buttons.append(button)

    update_display()
    window.mainloop()

if __name__ == "__main__":
    # Load words from a file
    word_list_file = "D:\\Heritage Institute of Technology,Kolkata\\PycharmProjects\\pythonProject\\Hangman.txt"
    word_list = load_words(word_list_file)
    play_hangman(word_list)
