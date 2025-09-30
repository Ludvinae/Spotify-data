# Produit : cibler les gros utilisateurs pour bêta-tests.
# Plus de 200 min d’écoute par jour
# Plus de 50 titres écoutés par jour


def getPowerUsers(data):
    powerUserList = []
    for user in data:
        if isPowerUser(user):
            powerUserList.append(user)
    return powerUserList

def isPowerUser(user):
    if hasHighListeningTime(user) and hasHighTrackCount(user):
        return True
    return False

def hasHighListeningTime(user):
    if int(user["listening_time"]) > 200:
        return True
    return False

def hasHighTrackCount(user):
    if int(user["songs_played_per_day"]) > 50:
        return True
    return False