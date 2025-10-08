
churnByType = {}
totalByType = {}


def churned(data):
    churnedList = filter(filterChurned, data)
    for user in churnedList:
        addToChurnedDict(user["subscription_type"])
        
    addToTotalDict(data)

    message = ""
    for subType in totalByType:
        message += f"Attrition for {subType}: {totalByType[subType]}\n"

    return message

def filterChurned(user):
    if user["is_churned"] == "1":
        return True
    return False

def addToChurnedDict(subType):
    if subType not in churnByType:
        churnByType[subType] = 0
    churnByType[subType] += 1

def addToTotalDict(data):
    total = 0
    for subType in churnByType:
        total += int(churnByType[subType])

        totalPerSubType = filter(lambda x: x["subscription_type"] == subType , data)
        totalByType[subType] = f"{(float(churnByType[subType]) / len(list(totalPerSubType))) * 100:.2f} %"

    totalByType["Total"] = f"{(float(total) / len(data)) * 100:.2f} %"