# Segmentation par tranches d’âge
# Problème : Marketing : comparer les cohortes d’âge.

ages = {"Under 18": 0, "18-25": 0, "26-35": 0, "36-45": 0, "46-55": 0, "56-65": 0, "66+": 0}

def ageBracket(data):
    for user in data:
        updateDict(user["age"])
    displayCohorts()


def updateDict(age):
    if int(age) < 18:
        ages["Under 18"] += 1
    elif int(age) < 26:
        ages["18-25"] += 1
    elif int(age) < 36:
        ages["26-35"] += 1
    elif int(age) < 46:
        ages["36-45"] += 1
    elif int(age) < 56:
        ages["46-55"] += 1
    elif int(age) < 66:
        ages["56-65"] += 1
    elif int(age) >= 66:
        ages["66+"] += 1

def displayCohorts():
    for age in ages:
        
        
        print(f"Number of user in the {age} bracket: {ages[age]}")