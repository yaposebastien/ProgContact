'''
Ce programme est une amelioration d'un carnet d'adresse avec un fichier de type json

'''

import json

#Chargement de ma liste de contact existante 

nomSupp = input('Saisir le nom a supprimer:')

with open('Contact_Telephonique') as fichier_initial:
    mesContacts = json.load(fichier_initial)
    for personne in mesContacts['contact']:
        if personne['nom'] == nomSupp:
            del personne['nom']
            del personne['telephone']
            ListeModifiee = json.dumps(mesContacts)
            print(ListeModifiee)


