import matplotlib.pyplot as plt
from matplotlib.figure import Figure



def histogramme(data):
    skipRate = []
    for user in data:
        skipRate.append(float(user["skip_rate"]))

    #skipRate.sort()
    return importHist(skipRate)
    

def showHistogram(list):
    plt.hist(list, bins=12, edgecolor="black", rwidth=0.75, color="#B9C1E6")
    plt.xlabel("skip rate value")
    plt.ylabel("number of occurence")

    plt.show()


def importHist(list):
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.hist(list, bins=12, edgecolor="black", rwidth=0.75, color="#B9C1E6")
    ax.set_xlabel("skip rate value")
    ax.set_ylabel("number of occurence")
    return fig

