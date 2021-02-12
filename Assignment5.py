# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Ehren Williamson,2/10/2021,complete assignment):
# RRoot,1.1.2030,Created started script
# Ehren Williamson,02/10/2021,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
file = open(objFile,"r")
for item in file:
    lstRow = item.split(",") #split the rows in the file based on comma and put in a list
    dicRow = {"Task":lstRow[0].strip(), "Priority":lstRow[1].strip()} # take the list and put index 0 and 1 in dictionary
    lstTable.append(dicRow)
file.close()
# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
       print("This is the current data")
       for item in lstTable:
           print(item["Task"] +"," + item["Priority"])
       continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        taskName = input("Please type in the task name:")
        taskPriority = input("Please type in the task priority:")
        dicAdd = {"Task":taskName, "Priority":taskPriority}
        lstTable.append(dicAdd)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        print("This is the current list:")
        for item in lstTable:
            print(item["Task"] + "," + item["Priority"])
        taskRemove = input("What is the name of the task you would like to remove:")
        for item in lstTable:
            if item["Task"] == taskRemove:
                lstTable.remove(item)
            else:
                print("Could not find task")
        print("This is the current list:")
        for item in lstTable:
            print(item["Task"] + "," + item["Priority"])
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        file = open(objFile, "w")
        for item in lstTable:
            file.write(item["Task"] + "," + item["Priority"] + "\n")
        file.close()
        print("Data Saved!")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Exiting program, have a nice day!")
        break  # and Exit the program

