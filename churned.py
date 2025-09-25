

def churnTotal(data):
    churnTotal = 0
    for user in data:
        if user["is_churned"] == "1":
            churnTotal += 1
    return churnTotal / len(data)

def churnByType(data):
    churnByType = {"Free": 0, "Premium": 0, "Family": 0, "Student": 0}
    subByType = {"Free": 0, "Premium": 0, "Family": 0, "Student": 0}
    attritionRate = {}

    for user in data:
        match user["subscription_type"]:
            case "Free":
                subByType["Free"] += 1
                if user["is_churned"] == "1":
                    churnByType["Free"] += 1
            case "Premium":
                subByType["Premium"] += 1
                if user["is_churned"] == "1":
                    churnByType["Premium"] += 1
            case "Family":
                subByType["Family"] += 1
                if user["is_churned"] == "1":
                    churnByType["Family"] += 1
            case "Student":
                subByType["Student"] += 1
                if user["is_churned"] == "1":
                    churnByType["Student"] += 1
        
    attritionRate["Free"] = churnByType["Free"] / subByType["Free"]
    attritionRate["Premium"] = churnByType["Premium"] / subByType["Premium"]
    attritionRate["Family"] = churnByType["Family"] / subByType["Family"]
    attritionRate["Student"] = churnByType["Student"] / subByType["Student"]

    return attritionRate


