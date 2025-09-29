import csv
from churned import displayAttrition
from riskUsers import isRiskUser, altRiskUser
from revenus import getRevenusByCountry
from powerUsers import getPowerUsers
from adsPerSubType import adsPerSub
from deviceMix import deviceMix

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


# Attrition is the rate of "is_churned" divided by the total of users
displayAttrition(dataset)

# Check the dataset for risk users and add them to a list
riskUsers = []
count =0
for user in dataset:
    #if isRiskUser(user):
     #   riskUsers.append(user)
      #  count += 1
    if altRiskUser(user):
        riskUsers.append(user)
        count += 1

print(count / len(dataset))
getRevenusByCountry(dataset)

powerUsers = getPowerUsers(dataset)
print(f"Power Users count : {len(powerUsers)}")

adsPerSub(dataset)

deviceMix(dataset)