import matplotlib.pyplot as plt




def histogramme(data):
    skipRate = []
    for user in data:
        skipRate.append(user["skip_rate"])

    #skipRate.sort()
    showHistogram(skipRate)
    

def showHistogram(list):
    
    plt.hist(list, bins=10, edgecolor="black", rwidth=0.8)
    plt.xlabel("skip rate value")
    plt.ylabel("number of occurence")

    plt.show()

