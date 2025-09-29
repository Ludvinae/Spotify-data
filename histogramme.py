import matplotlib.pyplot as plt




def histogramme(data):
    skipRate = []
    for user in data:
        skipRate.append(user["skip_rate"])
    
    
    plt.hist(skipRate,bins=5,edgecolor="black")
    plt.show()

