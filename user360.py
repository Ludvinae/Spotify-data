# Problème : Support / CSM : afficher une fiche compactée pour un ID donné.

# Exemple d’utilisation : En ligne de commande, l’utilisateur donne un ID extrait du document, 
# puis on affiche les infos de l’utilisateur.

userIndex = {}

def userData(userID):
    return userIndex[userID]


def createIndex(data):
    for user in data:
        userIndex[user["user_id"]] = user