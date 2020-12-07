import mysql.connector
from VerifyLogin import checkCombination
from DatabaseConnection import loadFromDatabase
from DatabaseConnection import updateDatabase
from DatabaseConnection import disconnectFromDatabase

# EFFECT: Create local instances of the fields of the database
users = [] 
passwords = []
status = []

# EFFECT: Setting up a connection to database
login_db = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'password123', database = 'LoginCombos')

# EFFECT: Loading all the information from the database
loadFromDatabase(login_db, users, passwords, status)

print("Login to existing account(1) or Create new account (2)")
choiceInput = input()

if (choiceInput == "1"):
    # EFFECT: Request for user information. This will be given from the front end.
    print("Enter the Username:")
    userInput = input()

    print("Enter the Password:")
    passwordInput = input()

    #EFFECT: Prints a string determining whether the user and password combination is correct or not
    checkCombination(users, passwords, userInput, passwordInput)

elif (choiceInput == "2"):
    # EFFECT: Request for user information. This will be given from the front end.
    print("Enter the Username:")
    userInput = input()

    print("Enter the Password:")
    passwordInput = input()

    print("Are you an NGO? (Enter true or false)")
    statusInput = input()

    updateDatabase(login_db, len(users), userInput, passwordInput, statusInput)
    
else:
    print("Choose either 1 or 2")

#EFFECT: Close connection to database
disconnectFromDatabase(login_db)