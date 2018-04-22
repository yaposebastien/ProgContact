#!/usr/bin/env python3.6
"""
Ce Script est une reecriture du programme d'un carnet d'addresse en Python.
L'objectif est de sauvegarder les contacts permanemment d'un fichier texte et 
le gerer par un menu.

"""

    print("Nom du contact ou Saisir Q pour stopper :", end=' ')
    nom = input()

    print("Telephone du contact :", end=' ')
    telephone = input()

    print(f"Votre contact est : {nom} : {telephone}")

