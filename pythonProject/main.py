import tkinter as tk
from tkinter import messagebox
import random


class GuessTheNumberGame:
    def __init__(self, master):
        self.master = master
        self.master.title("number")

        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(self.master, text="guess a number between 1 and 100:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.master)
        self.entry.pack(pady=5)

        self.button = tk.Button(self.master, text="Guess", command=self.check_guess)
        self.button.pack(pady=10)

        self.message = tk.Label(self.master, text="")
        self.message.pack()

        self.reset_button = tk.Button(self.master, text="Play Again", command=self.reset_game, state=tk.DISABLED)
        self.reset_button.pack(pady=10)

    def check_guess(self):
        guess = self.entry.get()
        try:
            guess = int(guess)
            self.attempts += 1

            if guess < self.secret_number:
                self.message.config(text="Too low! Try again.", fg="red")
            elif guess > self.secret_number:
                self.message.config(text="Too high! Try again.", fg="red")
            else:
                self.message.config(text=f"Congratulations! You guessed it right in {self.attempts} attempts.",
                                    fg="green")
                self.button.config(state=tk.DISABLED)
                self.reset_button.config(state=tk.NORMAL)
        except ValueError:
            self.message.config(text="Please enter a valid number!", fg="orange")

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.message.config(text="")
        self.button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.DISABLED)
        self.entry.delete(0, tk.END)


# Create the main window
root = tk.Tk()
game = GuessTheNumberGame(root)
root.mainloop()