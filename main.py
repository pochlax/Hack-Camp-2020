import mysql.connector
from VerifyLogin import checkCombination
from DatabaseConnection import loadFromDatabase
from DatabaseConnection import disconnectFromDatabase

# EFFECT: Create local instances of the fields of the database
users = [] 
passwords = []
status = []

login_db = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'password123', database = 'LoginCombos')

loadFromDatabase(login_db, users, passwords, status)

# Request for user information
print("Enter the Username:")
userInput = input()

print("Enter the Password:")
passwordInput = input()

checkCombination(users, passwords, userInput, passwordInput)

disconnectFromDatabase(login_db)