subscriptions = {"Free": {"adsTotal": 0, "userTotal": 0}, "Premium": {"adsTotal": 0, "userTotal": 0}, "Family": {"adsTotal": 0, "userTotal": 0}, "Student": {"adsTotal": 0, "userTotal": 0}}

def adsPerSub(data):
    for user in data:
        addToDict(user)
    return f"Ads listened by Free users: {averageAds('Free'):.2f}"



def addToDict(user):
    subType = user["subscription_type"]
    subscriptions[subType]["adsTotal"] += int(user["ads_listened_per_week"])
    subscriptions[subType]["userTotal"] += 1


def averageAds(subType):
    return subscriptions[subType]["adsTotal"] / subscriptions[subType]["userTotal"]