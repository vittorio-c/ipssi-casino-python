from tkinter import *
import time
import tkinter as tk
from classes.Game import Game

class UserPseudo :
    root = tk.Tk()
    root.title("Casino Game")
    root.geometry("600x400")

    # Create label Pseudo
    user_name_label = tk.Label(root, text="Je suis Python. Quel est votre pseudo ?")
    user_name_label.grid(row=2, column=0)

    # Create chaps de saisie for Pseudo
    user_name = tk.Entry(root, width=30)
    user_name.grid(row=2, column=1, padx=20)
    print(user_name.get())

    # Create Start button
    startButton = tk.Button(root, text="Start Game")
    #startButton.bind("<Button>", startGame)
    startButton.grid(row=3, column=1, columnspan=2, pady=10, padx=10, ipadx=100)

    '''my_progress = ttk.Progressbar(root, orient=HORIZONTAL, length=300, mode='determanate')
    my_progress.pack(pady=20)
    my_progress.start(10)'''
    root.mainloop()

    def startGame(self):
        print()
        # Clear the text of ussr_name
        #user_name.delete(0, END)
