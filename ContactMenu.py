#!/usr/bin/env python3.6

'''
Ce programme est une amelioration d'un carnet d'adresse avec un fichier de type json

'''


import json

#Creation liste de contacts pour les besoins de tests
mesContacts = []
mesContacts = ({ 'Momo': '+225454545', 'Marie-Paul': '+225787878'})


#Menu de l'application
def menuApplication():
    print('\f')
    print(f'\n\t\t Application Carnet d"Addresses .')
    print(f'\t\t Presser [L]ister tous vos contacts.')
    print(f'\t\t Presser [A]jouter un nouveau contact.')
    print(f'\t\t Presser [R]echercher un contact dans la liste.')
    print(f'\t\t Presser [S]upprimer un contact dans la liste.')
    print(f'\t\t Presser [Q]uitter votre carnet addresses .')

#Ajouter un nouveau contact
def AjouterContact():
    with open('mesContacts.txt', 'a') as monfichier:
        nvellePersonne = input('\t\t Saisir nom du nouveau contact: ')
        nveauContact = input('\t\t Saisir le numero du nouveau contact: ')
        mesContacts.update({ nvellePersonne : nveauContact }) #Important mot permettant l'ajout dans un dictionnaire de donnees
        SauvegarderCarnet()



#Rechercher un contact dans ma liste
def RechercherContact():
        nomRecher = input('\t\t Saisir le nom a rechercher: ')

        for Personne, Contact in mesContacts.items():

            if Personne == nomRecher:
                print('\n\t\t Resultat de votre recherche ')
                print('\t\t', Personne, Contact, '\n')


#Affichage de toute la liste des contacts
def AfficherMaListe():
        for Personne, Contact in mesContacts.items():
            print('\t\t', Personne, '---', Contact)

#Supprimer un contact de la liste
def SupprimerContact():
    nomSupp = input('\t\t Saisir le nom a supprimer: ')
    del mesContacts[nomSupp] #Importante syntaxe permettant de supprimer un objet dans un dictionnaire
    SauvegarderCarnet()

#Sauvegarder votre carnet dans le fichier apres chaque modification
def SauvegarderCarnet():
    with open('mesContacts.txt', 'w') as monfichier:
        json.dump(mesContacts, monfichier) #Importante syntaxe permettant d'ajouter notre dictionnaire au format json 
        monfichier.close()




if __name__ == '__main__' :
    

    continuer = False
    while continuer == False:
        menuApplication()
        optionUtilisateur = input('\n\t\t Veuillez selectionner une action: ')

        if optionUtilisateur  in ["L", "l"]:
            AfficherMaListe()
        elif optionUtilisateur in ["A", "a"]:
            AjouterContact()
        elif optionUtilisateur in ["R", "r"]:
            RechercherContact()
        elif optionUtilisateur in ["S", "s"]:
            SupprimerContact()
        elif optionUtilisateur in ["Q", "q"]:
            print("\t\t Fin de l'application! ")
            continuer = True
