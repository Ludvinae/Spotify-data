import matplotlib.pyplot as plt


skipRate = []

def histogramme(data):
    for user in data:
        skipRate.append(user["skip_rate"])
    
    
    plt.hist(skipRate,bins=5,edgecolor="black")
    plt.show

