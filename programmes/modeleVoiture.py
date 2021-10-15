import csv

file = open("modeleVoiture.csv", "a") # je crée le fichier modeleVoiture avec l'extension .csv si il n'existe pas, et j'écris à chaque ligne.

modelOfTheCar = input("Model of the car:\n") #Je demande à l'utilisateur un modèle de voiture
numberPlate = int(input("numberplate ?\n")) #Je demande à l'utilisateur une plaque de voiture

#print to file
writer = csv.writer(file) # déclaration de variable nommée writer qui permettra d'écrire
writer.writerow((modelOfTheCar, numberPlate)) # writerow est une fonction de la bibliothèque csv

file.close() # je ferme le fichier