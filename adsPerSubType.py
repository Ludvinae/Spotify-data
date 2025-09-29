subscriptions = {"Free": {"adsTotal": 0, "userTotal": 0}, "Premium": {"adsTotal": 0, "userTotal": 0}, "Family": {"adsTotal": 0, "userTotal": 0}, "Student": {"adsTotal": 0, "userTotal": 0}}

def adsPerSubs(data):
    for user in data:
        addToDict(user)
    print(f"Ads listened by Free users: {averageAds("Free")}")
    print(f"Ads listened by Premium users: {averageAds("Premium")}")
    print(f"Ads listened by Family users: {averageAds("Family")}")
    print(f"Ads listened by Student users: {averageAds("Student")}")



def addToDict(user):
    subType = user["subscription_type"]
    subscriptions[subType]["adsTotal"] += user["ads_listened_per_week"]
    subscriptions[subType]["userTotal"] += 1


def averageAds(subType):
    return subscriptions[subType]["adsTotal"] / subscriptions[subType]["userTotal"]