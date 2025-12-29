import tkinter as tk
import random

words = ["python", "data", "game", "hang"]

hangman_art = [
" +---+\n |   |\n     |\n     |\n     |\n     |\n=========",
" +---+\n |   |\n O   |\n     |\n     |\n     |\n=========",
" +---+\n |   |\n O   |\n |   |\n     |\n     |\n=========",
" +---+\n |   |\n O   |\n /|  |\n     |\n     |\n=========",
" +---+\n |   |\n O   |\n /|\\ |\n     |\n     |\n=========",
" +---+\n |   |\n O   |\n /|\\ |\n /   |\n     |\n=========",
" +---+\n |   |\n O   |\n /|\\ |\n / \\ |\n     |\n========="
]

def choose_word():
    return random.choice(words)

def update_hangman(mistakes):
    hangman_label.config(text=hangman_art[mistakes])

def check_guess():
    global word_with_blanks, mistakes

    guess = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)

    if not guess or len(guess) != 1:
        return

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                word_with_blanks = word_with_blanks[:i] + guess + word_with_blanks[i+1:]
        word_label.config(text=word_with_blanks)

        if "_" not in word_with_blanks:
            end_game("win")
    else:
        mistakes += 1
        update_hangman(mistakes)
        if mistakes == 6:
            end_game("lose")

def end_game(result):
    if result == "win":
        result_label.config(text="You won!")
    else:
        result_label.config(text="You lost! Word was: " + word)

    guess_entry.config(state="disabled")
    guess_button.config(state="disabled")

root = tk.Tk()
root.title("Hangman")

hangman_label = tk.Label(root, font=("Courier", 20), bg="yellow")
hangman_label.grid(row=0, column=0, columnspan=2)

word = choose_word()
word_with_blanks = "_" * len(word)

word_label = tk.Label(root, text=word_with_blanks, font=("Arial", 24), bg="purple")
word_label.grid(row=1, column=0, columnspan=2)

guess_entry = tk.Entry(root, width=5, font=("Arial", 14), bg="pink")
guess_entry.grid(row=2, column=0)

guess_button = tk.Button(root, text="Guess", bg="green", command=check_guess)
guess_button.grid(row=2, column=1)

result_label = tk.Label(root, font=("Arial", 18))
result_label.grid(row=3, column=0, columnspan=2)

mistakes = 0
update_hangman(mistakes)

root.mainloop()