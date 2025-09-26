#Finance : estimer le MRR de base par plan et par pays (utilisateurs non churnés).
'''
PRICES = {
    "Free": 0.0,
    "Premium": 9.99,
    "Family": 14.99,
    "Student": 4.99
}
'''

def isNotChurned(user):
    if user["is_churned"] == "0":
        return True
    return False

subTypeCount = [] * 4

def subType(user):
    match user["subscription_type"]:
        case "Free":
            subTypeCount[0] += 1
        case "Premium":
            subTypeCount[1] += 1
        case "Family":
            subTypeCount[2] += 1
        case "Student":
            subTypeCount[3] += 1

countries = {}

def newCountryCode(user):
    country = user["country"]
    countries[country] = [0, 0, 0, 0]

def countryDict(user):
    if user["country"] not in countries:
        newCountryCode(user)
    countries[user["country"]] = subType(user)

def buildCountriesDict(data):
    for user in data:
        if isNotChurned(user):
            countryDict(user)