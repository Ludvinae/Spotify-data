import matplotlib.pyplot as plt




def histogramme(data):
    skipRate = []
    for user in data:
        skipRate.append(float(user["skip_rate"]))

    #skipRate.sort()
    showHistogram(skipRate)
    

def showHistogram(list):
    plt.hist(list, bins=12, edgecolor="black", rwidth=0.75, color="#B9C1E6")
    plt.xlabel("skip rate value")
    plt.ylabel("number of occurence")

    plt.show()

