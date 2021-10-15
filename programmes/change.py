print("Je suis un petit programme d'échange de chiffre. Donnez-moi deux valeurs, et je les échangerai ! \n") #petite introduction
first = int(input("Quel est le premier chiffre ?\n")) #  Je demande à l'utilisateur le premier chiffre
second = int(input("Quel est le deuxième chiffre ?\n"))#  Je demande à l'utilisateur le deuxième chiffre
print(f"Voici les valeurs dans l'ordre avant échange :\n{first} & {second}.") # J'affiche les deux
first, second = second, first # je fais l'échange
print(f"Voici les valeurs après échange :\n{first} & {second}.") # j'affiche le changement
