# Segmentation par tranches d’âge
# Problème : Marketing : comparer les cohortes d’âge.

ages = {"Under 20": 0, "20-35": 0, "36-50": 0, "50+": 0}

def ageBracket(data):
    for user in data:
        updateDict(user["age"])
    displayCohorts()


def updateDict(age):
    if int(age) < 18:
        ages["Under 20"] += 1
    elif int(age) < 26:
        ages["20-35"] += 1
    elif int(age) < 36:
        ages["36-50"] += 1
    elif int(age) < 46:
        ages["50+"] += 1

def displayCohorts():
    for age in ages:    
        
        print(f"Number of user in the {age} bracket: {ages[age]}")