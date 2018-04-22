#!/usr/bin/env python3.6
from sys import argv
"""
Ce Script est une reecriture du programme d'un carnet d'addresse en Python.
L'objectif est de sauvegarder les contacts permanemment d'un fichier texte et 
le gerer par un menu.

"""

script, fichierContact = argv

estArrete = False

while estArrete == False:
    nom = input('Nom du contact ou Q pour stopper:')
    
    if nom == 'Q':
        estArrete = True
    else:
        telephone = input('Telephone du contact: ')
        print(f"Votre contact est : {nom} -- {telephone}")
        
        #Ouverture du fichier en mode ecriture et ajouter du noveau contact
        fichier = open(fichierContact, 'w')
        fichier.write(nom)
        fichier.write(" ")
        fichier.write(telephone)
        fichier.write("\n")
        fichier.close()    #Fermeture du fichier


