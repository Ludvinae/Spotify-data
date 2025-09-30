# Sets : valeurs uniques utiles (pays, plans, devices) — bonus
# Problème : Marketing : lister rapidement l’étendue des marchés et supports.

# Liste des devices uniques
# Liste des pays uniques

deviceSet = set()
countrySet = set()
subSet = set()

def checkUnique(data):
    deviceSet = set()
    countrySet = set()
    subSet = set()
    for user in data:
        deviceSet.add(user["device_type"])
        countrySet.add(user["country"])
        subSet.add(user["subscription_type"])

    print(deviceSet)
    print(countrySet)
    print(subSet)

