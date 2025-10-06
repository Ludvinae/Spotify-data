# Problème : Support / CSM : afficher une fiche compactée pour un ID donné.

# Exemple d’utilisation : En ligne de commande, l’utilisateur donne un ID extrait du document, 
# puis on affiche les infos de l’utilisateur.

userIndex = {}

def userData(userID):
    return userIndex[userID]


def createIndex(data):
    for user in data:
        userIndex[user["user_id"]] = user


def displayUser(data):
    createIndex(data)
    index = input("Please enter the ID of the user you're looking for: ")
    user = userData(index)
    if user["is_churned"] == "0":
        churn = "active"
    else:
        churn = "inactive"
    return f"User with ID {user['user_id']}, {user['gender']} gender, age {user['age']} from {user['country']}\nHas {user['subscription_type']} subscription, {user['listening_time']} minutes of listening time and {user['songs_played_per_day']} songs played per day\nSkip rate of {(float(user['skip_rate'])) * 100} %, use a {user['device_type']}, listen to {user['ads_listened_per_week']} ads per week\nHas listened to {user['offline_listening']} minutes offline, and is {churn}.\n__________________________________________________________________________________"
    