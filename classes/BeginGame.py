from tkinter import * 
from tkinter import messagebox
from classes.Game import Game

game = Game()

class BeginGame:
    #centrer la page             
    def run(self):
        window= Tk()
        window.title("Casino Game")
        window.iconbitmap("images/casinoIcon.ico")
        
        # centrer  le window
        x = (window.winfo_screenwidth()/2) - (900/2)    
        y = (window.winfo_screenheight()/2) - (506/2)
        window.geometry('%dx%d+%d+%d' % (900, 506, x, y))
 
        window.resizable(False,False)
        window.config(background="#123225")

        #La frame
        frame=Frame(window,bg="#123225")

        #text de user name
        label=Label(window, text="Je suis Python. Quel est votre pseudo ?", font=("Courrier","18"), bg="#123225", fg="#ffffff")
        label.place(x=40 , y=40)

        #champs de saisie user name
        user_name=Entry(window, width=25, font=("Courrier","18"))
        user_name.place(x=530,y=42)

    #button de récuppération
        def jouer():
            user_nametext=user_name.get()
            if (not user_nametext):
                messagebox.showerror("Error message", "Please, intrduce your user name to start the game")
            else:
                print(user_nametext)
                user_name['state'] = DISABLED
                button_startgame.destroy()
                game.run(user_nametext)
            
        button_startgame=Button(window,text="Start Game",font=("Courrier","18"), width=20, bg="#123225", fg="#ffffff", command = jouer)
        button_startgame.place(x=320, y =200)
        window.mainloop()

                 
                    