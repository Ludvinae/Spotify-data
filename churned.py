
churnByType = {"Free": 0, "Premium": 0, "Family": 0, "Student": 0}
subByType = {"Free": 0, "Premium": 0, "Family": 0, "Student": 0}


def churnTotal(data):
    churnTotal = 0
    for user in data:
        if user["is_churned"] == "1":
            churnTotal += 1
    return round(churnTotal / len(data) * 100, 2)

def getChurnByType(data):
    for user in data:
        match user["subscription_type"]:
            case "Free":
                updateDictionnaries("Free", user)
            case "Premium":
                updateDictionnaries("Premium", user)
            case "Family":
                updateDictionnaries("Family", user)
            case "Student":
                updateDictionnaries("Student", user)

def updateDictionnaries(subType, user):
    subByType[subType] += 1
    if user["is_churned"] == "1":
        churnByType[subType] += 1

def attritionRate(subType):
    return round((churnByType[subType] / subByType[subType]) * 100, 2)

def displayAttrition(data):
    getChurnByType(data)
    print(f"Total Attrition rate: {churnTotal(data)} %")
    print(f"Free subs Attrition rate: {attritionRate('Free')} %")
    print(f"Premium subs Attrition rate: {attritionRate('Premium')} %")
    print(f"Family subs Attrition rate: {attritionRate('Family')} %")
    print(f"Student subs Attrition rate: {attritionRate('Student')} %")

