'''Règles métier :

Taux de skip > 30%
Taux d’écoute < 100 min par jour
Pour les comptes gratuits :
aucune écoute offline
écoute de pub > 20 par semaine'''

def isSkipping(user):
    if float(user["skip_rate"]) > 0.3:
        return True
    return False

def hasLowListeningTime(user):
    if int(user["listening_time"]) < 100:
        return True
    return False

def hasFreeSub(user):
    if user["subscription_type"] == "Free":
        return True
    return False

def hasNoOfflineListening(user):
    if user["offline_listening"] == "0":
        return True
    return False

def hasHeardAds(user):
    if int(user["ads_listened_per_week"]) > 20:
        return True
    return False

def isRiskUser(user):
    if isSkipping(user) and hasLowListeningTime(user):
        if not hasFreeSub(user):
            return True
        else:
            if hasNoOfflineListening(user) and hasHeardAds(user):
                return True
    return False

def altRiskUser(user):
    if hasFreeSub(user):
        if hasNoOfflineListening(user) and hasHeardAds(user):
                return True
    else:
        if isSkipping(user) and hasLowListeningTime(user):
            return True
    return False