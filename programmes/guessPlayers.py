combienDeFois = 0 # J'initialise les variables qui me seront utiles
choix = 0
commencer = 1 # Cette variable me servira pour vérifier une condition
# j'introduis le jeu
print(f"Aujourd'hui je suis en bonne compagnie, et je souhaitais jouer au jeu mystère.\nLe joueur 2 choisis le nombre mystère, et le joueur 1 est censé le deviner :P")
joueur1 = input("Qui sera le joueur 1 ?\n")
joueur2 = input("Qui sera le joueur 2 ?\n")
print('\x1bc')
print(f"Très bien, les informations sont à jour !")
nombreMystere = int(input(f"{joueur2}, choisis un nombre mystère entre 1 et 20 😜 !\n")) # Je demande à l'utilisateur d'entrer un nombre mystère !

while commencer == 1: # Tant que ma variable commencer est sur 1,
    if nombreMystere < 1 or nombreMystere > 20: # Si le nombre mystère n'est pas entre 1 et 20 comprit,
        print('\x1bc')
        print(f"J'attends un nombre entier entre 1 et 20 !") # Je réitère la consigne
        nombreMystere = int(input(f"{joueur2}, choisis un nombre mystère entre 1 et 20 comprit!\n"))
    else: # sinon,
        commencer = 0 # Je commence le jeu !
        print('\x1bc')
        print(f"Entrée prise en compte ! \n")

while nombreMystere != choix: # Tant que le nombre mystère est différent de la valeur entrée par l'utilisateur,
    choix = int(input(f"{joueur1}, devine le nombre mystère entre 1 et 20 🤞\n")) # Je récupère la nouvelle valeur choisit dans ma variable choix.
    if choix < nombreMystere: # Je précise quoi afficher à l'utilisateur si son choix est plus petit que le nombre mystère
        print(f"Un peu plus !")
        combienDeFois += 1; # J'ajuste le nombre de coup
    elif choix > nombreMystere: # Je précise quoi afficher à l'utilisateur si son choix est plus grand que le nombre mystère
        print(f"Un peu moins !")
        combienDeFois += 1

print('\x1bc')
print(f"\n")
print(f"************************")
print(f"Bingo {joueur1} 🎉!\nTu as réussi en {combienDeFois + 1} coup(s) !") # // Je félicite le joueur quand il a gagné et affiche quelques détails.
print(f"************************")
exit(0) # termine le programme
