import json

ListeContact = {}
ListeContact['contact'] = []

#Ajout dans la liste
ListeContact['contact'].append({
    'nom': 'Momo Sylvain',
    'telephone': '+22547474747'
    })
ListeContact['contact'].append({
    'nom': 'Georgina Yapo',
    'telephone': '+2225787878778'
    })

with open('Contact_Telephonique', 'w') as monfichier:
    json.dump(ListeContact, monfichier)
