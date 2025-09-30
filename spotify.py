import csv
from churned import displayAttrition
from riskUsers import riskUsers
from revenus import getRevenusByCountry
from powerUsers import getPowerUsers
from adsPerSubType import adsPerSub
from deviceMix import deviceMix
from ageBracket import ageBracket
from histogramme import histogramme
import user360
from uniqueValues import checkUnique


def read_spotify_data(file_path, debug=True):
    spotify_data = []
    
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            spotify_data.append(row)

    if debug: 
        for record in spotify_data[:5]:
            print(record)

    return spotify_data

dataset = read_spotify_data(file_path="spotify_churn_dataset.csv", debug=False)



while True:
    choice = input("Quelle fonction voulait vous tester? (Q pour arrêter, 1-10 pour choisir une fonction): ")
    match choice:
        case "1":
            # Attrition is the rate of "is_churned" divided by the total of users
            displayAttrition(dataset)
        case "2":
            riskUsers(dataset)
        case "3":
            getRevenusByCountry(dataset)
        case "4":
            powerUsers = getPowerUsers(dataset)
            print(f"Power Users count : {len(powerUsers)}")
        case "5":
            adsPerSub(dataset)
        case "6":
            deviceMix(dataset)
        case "7":
            ageBracket(dataset)
        case "8":
            histogramme(dataset)
        case "9":
            user360.createIndex(dataset)
            index = input("Please enter the ID of the user you're looking for: ")
            print(user360.userData(index))
        case "10":
            checkUnique(dataset)
        case "q" | "Q":
            break
        case _:
            print("wrong input, try again or type 'Q' to abort")


