'''
Ce programme est une amelioration d'un carnet d'adresse avec un fichier de type json

'''

import json

#Chargement de ma liste de contact existante 

nomRecher = input('Saisir le nom a rechercher:')

with open('Contact_Telephonique') as MaListe:
    mesContacts = json.load(MaListe)
    for personne in mesContacts['contact']:
        if personne['nom'] == nomRecher:
            print('Resultat de la recherche')
            print('Nom: ' +personne['nom'])
            print('Telephone: ' +personne['telephone'])
            print('\n')
            break
        else:
            print(f'{nomRecher} non retrouve!')


