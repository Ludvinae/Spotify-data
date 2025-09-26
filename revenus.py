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

countries = {}

def subType(user, countryCode):
    match user["subscription_type"]:
        case "Free":
            countries[countryCode][0] += 1
        case "Premium":
            countries[countryCode][1] += 1
        case "Family":
            countries[countryCode][2] += 1
        case "Student":
            countries[countryCode][3] += 1

def newCountryCode(user):
    country = user["country"]
    countries[country] = [0, 0, 0, 0]

def countryDict(user):
    if user["country"] not in countries:
        newCountryCode(user)
    subType(user, user["country"])

def buildCountriesDict(data):
    for user in data:
        if isNotChurned(user):
            countryDict(user)

def displayCountryRevenus(country):
    #print("Free plan: ", prices[0] * float(countries[country][0]), " €", end="| ")
    print("Premium plan: ", prices[1] * float(countries[country][1]), " €", end="| ")
    print("Family plan: ", prices[2] * float(countries[country][2]), " €", end="| ")
    print("Student plan: ", prices[3] * float(countries[country][3]), " €")


prices = [0.00, 9.99, 14.99, 4.99]

def getRevenusByCountry(data):
    buildCountriesDict(data)
    for country in countries:
        print(f"Revenues for {country}:")
        displayCountryRevenus(country)
       