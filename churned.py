
churnByType = {"Free": 0, "Premium": 0, "Family": 0, "Student": 0}
subByType = {"Free": 0, "Premium": 0, "Family": 0, "Student": 0}
attritionRate = {}

def churnTotal(data):
    churnTotal = 0
    for user in data:
        if user["is_churned"] == "1":
            churnTotal += 1
    return churnTotal / len(data)

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
        
    attritionRate["Free"] = churnByType["Free"] / subByType["Free"]
    attritionRate["Premium"] = churnByType["Premium"] / subByType["Premium"]
    attritionRate["Family"] = churnByType["Family"] / subByType["Family"]
    attritionRate["Student"] = churnByType["Student"] / subByType["Student"]

    return attritionRate

def updateDictionnaries(subType, user):
    subByType[subType] += 1
    if user["is_churned"] == "1":
        churnByType[subType] += 1
