from spotify import dataset
from functools import reduce

churnByType = {}


def churned(data):
    churnedList = filter(filterChurned, data)
    for user in churnedList:
        addToChurnedDict(user["subscription_type"])
    
    for subType in churnByType:
        total = filter(lambda x: x["subscription_type"] == subType , data)
        return total

    return churnByType

def filterChurned(user):
    if user["is_churned"] == "1":
        return True
    return False

def addToChurnedDict(subType):
    if subType not in churnByType:
        churnByType[subType] = 0
    churnByType[subType] += 1

def findTotalPerSubType(subType):
    pass

def attritionPercent(churned):
    pass

print(churned(dataset))