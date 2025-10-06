# Mix des devices par pays (dictionnaires imbriqués)
# Problème : Équipe growth : savoir quels devices dominent selon les marchés.

countries = {}

def deviceMix(data):
    for user in data:
        updateDict(user)
    return printDeviceMix()
    


def updateDict(user):
    country = user["country"]
    if country not in countries:
        newCountry(country)
    device = getDevice(user)
    countries[country][device] += 1
    countries[country]["total"] += 1

def newCountry(country):
    countries[country] = {"Mobile": 0, "Desktop": 0, "Web": 0, "total" : 0}


def getDevice(user):
    return user["device_type"]

def printDeviceMix():
    message = ""
    for country in countries:
        message += f"Most used device for {country}: "
        device = getMax(country)
        match device:
            case "Mobile":
                message += f"Mobile users ({getpercent(country, 'Mobile'):.2f} %)\n"
            case "Desktop":
                message += f"Desktop users ({getpercent(country, 'Desktop'):.2f} %)\n"
            case "Web":
                message += f"Web users ({getpercent(country, 'Web'):.2f} %)\n"
            case _:
                message += "error\n"
    return message


def getpercent(country, device):
    return int(countries[country][device]) / int(countries[country]["total"]) * 100


def getMax(country):
    deviceList = ["Mobile", "Desktop", "Web"]
    max = 0
    deviceMax = ""
    for device in deviceList:
        if countries[country][device] > max:
            max = countries[country][device]
            deviceMax = device
    
    return deviceMax