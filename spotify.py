import csv

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

def churnTotal():
    churnTotal = 0
    for user in dataset:
        if user["is_churned"] == "1":
            churnTotal += 1
    return churnTotal / len(dataset)

def churnByType():
    churnByType = {"Free": 0, "Premium": 0, "Family": 0, "Student": 0}
    subByType = {"Free": 0, "Premium": 0, "Family": 0, "Student": 0}
    attritionRate = {}

    for user in dataset:
        match user["subscription_type"]:
            case "Free":
                subByType["Free"] += 1
                if user["is_churned"] == "1":
                    churnByType["Free"] += 1
            case "Premium":
                subByType["Premium"] += 1
                if user["is_churned"] == "1":
                    churnByType["Premium"] += 1
            case "Family":
                subByType["Family"] += 1
                if user["is_churned"] == "1":
                    churnByType["Family"] += 1
            case "Student":
                subByType["Student"] += 1
                if user["is_churned"] == "1":
                    churnByType["Student"] += 1
        
    attritionRate["Free"] = churnByType["Free"] / subByType["Free"]
    attritionRate["Premium"] = churnByType["Premium"] / subByType["Premium"]
    attritionRate["Family"] = churnByType["Family"] / subByType["Family"]
    attritionRate["Student"] = churnByType["Student"] / subByType["Student"]

    return attritionRate

print(str(churnTotal() * 100) + " %")
print(churnByType())

