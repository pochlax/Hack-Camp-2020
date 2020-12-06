import mysql.connector
login_db = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'password123', database = 'LoginCombos')

print (login_db)

if (login_db):
    print("connection successful")
else:
    print("connection failed")

cur = login_db.cursor()

cur.execute("SELECT * FROM userPass")

users = [] 
passwords = []

for row in cur.fetchall():
    users.append(row[1])
    passwords.append(row[2])

print("Enter the Username:")
userInput = input()

print("Enter the Password:")
passwordInput = input()

index = 0

for u in users:
    if (userInput == u):
        break
    else:
        index = index + 1

if (userInput in users):
    if (passwordInput == passwords[index]):
        print("Combination Correct")

login_db.close()
