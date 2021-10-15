print("Je suis un petit programme qui permmet de faire ressortir la valeur la plus haute saisis.\n"); #Introduction
first = int(input("Choisissez 3 Entiers.\nQuel est le premier chiffre ?\n")) # Je récupère la valeur saisi et l'assigne à ma variable 1
second = int(input("Quel est le deuxième chiffre ?\n")) # Je récupère la valeur saisi et l'assigne à ma variable 2
third = int(input("Quel est le troisième chiffre ?\n")) # Je récupère la valeur saisi et l'assigne à ma variable 3


if first > second and first > third: # Si ma première variable est supérieure aux deux autres,
    print(f" {first} est la valeur la plus élevée.\n") # J'affiche qu'elle est la plus élevée.
elif second > first and second > third:  # Autrement Si ma deuxième variable est supérieure aux deux autres,
    print(f"{second} est la valeur la plus élevée.\n") # J'affiche qu'elle est la plus élevée.
else: # sinon,
    print(f"{third} est la valeur la plus élevée.\n"); # j'en déduis que c'est l'autre valeur la plus grande.
