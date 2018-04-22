#!/usr/bin/env python3.6
from sys import argv

script, nomdufichier = argv


print("Ouverture de notre fichier")
fichier = open(nomdufichier)
print(fichier.read())
