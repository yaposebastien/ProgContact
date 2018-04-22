#!/usr/bin/env python3.6
from sys import argv

script, nomdufichier = argv


print("Ouverture de notre fichier")
fichier = open(nomdufichier, "a")
entree = input(f'Ajouter une nouvelle ligne dans {fichier}')
fichier.write(entree)
fichier.write("\n")
fichier.close()

