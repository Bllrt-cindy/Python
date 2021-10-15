from tkinter import * # J'importe les librairies necessaires
import tkinter as tk

################################ Petit projet en construction, celui-ci n'est pas terminé ################################

guessWindow = Tk() # Je crée une fenêtre et je la paramètre
guessWindow['bg']='#111'
guessWindow.title("Guess my mystery number !")

# ###################################################JOUEUR 2#######################################################
# ###################################################JOUEUR 2#######################################################


# create a Label widget
myLabel = Label(guessWindow, text="Joueur 2, choisis un numéro mystère !", font=("Gabriola", 40), fg='#eee', bg='#111')
myLabel.pack(pady="55") # j'écris une petite intro

input = Entry(guessWindow, width="30", bg="#111", fg='#eee', borderwidth="5")
input.pack() # je crée un input



def lancer(): # je paramètre la fonction qui se lancera au click sur le bouton associé
    if int(input.get()) < 1 or int(input.get()) > 20:
        input.delete(0, END)
        input.insert(0, "Un chiffre entre 1 et 20 svp !")
    else:
        input.pack_forget()

lancer = tk.Button(guessWindow, text ="Masquer", command = lancer)
lancer.pack() # je crée mon bouton et je l'affiche


# ###################################################JOUEUR 1########################################################
# ###################################################JOUEUR 1########################################################

myLabel2 = Label(guessWindow, text="Joueur 1, devine le nombre mystère !", font=("Gabriola", 20), fg='#eee', bg='#111')
myLabel2.pack()

input2 = Entry(guessWindow, width="30", bg="#111", fg='#eee', borderwidth="5")
input2.pack()


def lancer2():
        if input2.get() < input.get(): # Je précise quoi afficher à l'utilisateur si son choix est plus petit que le nombre mystère
            labelid1['text'] = "Plus grand !"
        elif input2.get() > input.get(): # Je précise quoi afficher à l'utilisateur si son choix est plus grand que le nombre mystère
            labelid1['text'] = "Plus petit"
        else:
            labelid1['text'] = "Bingo !"
        input2.delete(0, END)

lancer2 = tk.Button(guessWindow, text ="Enregistrer", command = lancer2)
lancer2.pack()

labelid1 = tk.Label(guessWindow , borderwidth=1, relief="ridge", height=5, width=20)
labelid1.pack(pady=30)

Button(guessWindow, text="Quit", command=guessWindow.destroy).pack() #Je crée un bouton pour quitter le jeu

guessWindow.mainloop()