'''Règles métier :

Taux de skip > 30%
Taux d’écoute < 100 min par jour
Pour les comptes gratuits :
aucune écoute offline
écoute de pub > 20 par semaine'''

def isSkipping(user):
    if user["skip_rate"] > 0.3:
        return True
    return False

def hasLowListeningTime(user):
    if user["listening_time"] < 100:
        return True
    return False