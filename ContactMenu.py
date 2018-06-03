'''
Ce programme est une amelioration d'un carnet d'adresse avec un fichier de type json

'''


import json

#Menu de l'application
def menuApplication():
    print(f'\n\t Liste de contacts.')
    print(f'\t\t Presser[1] pour Afficher toute la liste.')
    print(f'\t\t Presser[2] pour Ajouter un nouveau contact.')
    print(f'\t\t Presser[3] pour Rechercher un contact dans la liste.')
    print(f'\t\t Presser[4] pour Supprimer un contact dans la liste.')

#Ajouter un nouveau contact
def AjouterContact():
    with open('Contact_Telephonique', 'a') as monfichier:
        nvellePersonne = input('Saisir le nom de la nouvelle personne')
        nveauContact = input('Saisir le numero de telephone')
        Personne = {contact: {'nom': nvellePersonne, 'telephone': nveauContact}}
        monfichier.write(json.dumps(Personne))
        monfichier.close()



#Rechercher un contact dans ma liste
def RechercherContact():
    with open('Contact_Telephonique') as MaListe:
        mesContacts = json.load(MaListe)
        
        nomRecher = input('Saisir le nom a rechercher:')
        
        for personne in mesContacts['contact']:
            if personne['nom'] == nomRecher:
                print('Resultat de la recherche')
                print('Nom: ' +personne['nom'])
                print('Telephone: ' +personne['telephone'])
                print('\n')
                break
            else:
                print(f'{nomRecher} non retrouve!')

#Affichage de toute la liste des contacts
def AfficherMaListe():
    with open('Contact_Telephonique') as MaListe:
        mesContacts = json.load(MaListe)
        for personne in mesContacts['contact']:
            print('Nom: ' +personne['nom'])
            print('Telephone: ' +personne['telephone'])
            print('\n')

#Supprimer un contact de la liste

def SupprimerContact():
    nomSupp = input('Saisir le nom a supprimer:')
    with open('Contact_Telephonique') as MaListe:
        mesContacts = json.load(MaListe)
        for personne in mesContacts['contact']:
            if personne['nom'] == nomSupp:
                del personne['nom']
                del personne['telephone']
                ListeModifiee = json.dumps(mesContacts)
                print(ListeModifiee)

                with open('Contact_Telephonique', 'w') as fichierModifier:
                    json.dump(ListeModifiee, fichierModifier)



if __name__ == '__main__' :
    
    continuer = False
    while continuer == False:
        menuApplication()
        optionUtilisateur = input('\t Veuillez selectionner une action')
        
        if optionUtilisateur == '1':
            AfficherMaListe()
        elif optionUtilisateur == '2':
            AjouterContact()
        elif optionUtilisateur == '3':
            RechercherContact()
        elif optionUtilisateur == '4':
            SupprimerContact()

