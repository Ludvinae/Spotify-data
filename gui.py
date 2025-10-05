from tkinter import *
from tkinter import ttk
from spotify import getFunction

# this line have to be on top
root = Tk()
root.title("Spotify")
root.geometry("800x600")

def show():
    choice = functions.get()
    match choice:
        case "Churn":
            display = getFunction("Churn")
        case "Risk users":
            display = getFunction("Risk users")
        case "Revenue":
            display = getFunction("Revenue")
        case "Power users":
            display = getFunction("Power users")
        case "Ads average":
            display = getFunction("Ads average")
        case "Device mix":
            display = getFunction("Device mix")
        case "Age brackets":
            display = getFunction("Age brackets")
        case "Skip rate":
            display = getFunction("Skip rate")
        case "Specific user":
            display = getFunction("Specific user")
        case "Unique values":
            display = getFunction("Unique values")
    result = Label(root, text=display).pack()

def jobCard(option):
    match option:
        case "Churn":
            job = "Global and per subscription type attrition"
        case "Risk users":
            job = "Users to get in touch with"
        case "Revenue":
            job = "MRR per subscription type and per country for active users"
        case "Power users":
            job = "Target very active users for beta tests"
        case "Ads average":
            job = "Average ads time per subscription type"
        case "Device mix":
            job = "On what type of device users run spotify"
        case "Age brackets":
            job = "Compare users age brackets"
        case "Skip rate":
            job = "Display skip rate distribution"
        case "Specific user":
            job = "Display the full data on a user selected with their ID"
        case "Unique values":
            job = "Show individual countries, devices and subscription types"
    card = Label(root, text=job)
    card.pack()

options = ["Churn", "Risk users", "Revenue", "Power users", 
           "Ads average", "Device mix", "Age brackets", 
           "Skip rate", "Specific user","Unique values"]
functions = StringVar()
functions.set(options[0])


# Creating objects
myTitle = Label(root, text="Spotify data analysis")
myLabel = Label(root, text="What function do you want to run?")
dropDown = OptionMenu(root, functions, *options, command=jobCard)
#dropDown = ttk.Combobox(root, values=options)
#dropDown.current(0)
#dropDown.bind(functions, jobCard)

myButton = Button(root, text="Run", command=show)


# Displaying objects
myTitle.pack()
myLabel.pack()
dropDown.pack()

myButton.pack()


root.mainloop()