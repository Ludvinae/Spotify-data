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


def riskUsers(data):
    while True:
        choice = input("What version do you want? (1 / 2): ")
        if choice != "1" and choice != "2":
            choice = "2"
        riskUsers = []
        riskUsers2 = []
        count = 0
        count2 = 0
        for user in data:
            if isRiskUser(user):
                riskUsers.append(user)
                count += 1
            if altRiskUser(user):
                riskUsers2.append(user)
                count2 += 1
        match choice:
            case "1":
                print(count / len(data))
                print(len(riskUsers))
                break
            case "2":
                print(count2 / len(data))
                print(len(riskUsers2))
                break