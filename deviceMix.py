# Mix des devices par pays (dictionnaires imbriqués)
# Problème : Équipe growth : savoir quels devices dominent selon les marchés.

countries = {}

def deviceMix(data):
    for user in data:
        updateDict(user)
    printDeviceMix()
    


def updateDict(user):
    country = user["country"]
    if country not in countries:
        newCountry(country)
    device = getDevice(user)
    countries[country][device] += 1


def newCountry(country):
    countries[country] = {"Mobile": 0, "Desktop": 0, "Web": 0}


def getDevice(user):
    return user["device_type"]

def printDeviceMix():
    for country in countries:
        print(f"Device mix for {country}:")
        print(f"Mobile users: {countries[country]["Mobile"]}; Desktop users: {countries[country]["Desktop"]}; Web users: {countries[country]["Web"]}")