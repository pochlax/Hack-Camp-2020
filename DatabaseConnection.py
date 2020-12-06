users = [] 
passwords = []
status = []

def loadFromDatabase(login_db, users, passwords, status):
    # EFFECT: Connect to the Database
    print (login_db)

    if (login_db):
        print("Connection Successful")
    else:
        print("Connection Unsuccessful")

    # EFFECT: Initialize a cursor for the database
    cur = login_db.cursor()

    # EFFECT: Obtain the required table from database
    cur.execute("SELECT * FROM userPass")

    # Note: The username and passwords have to be maintained together
    # as the combinations are linked together by their index ID.
    for row in cur.fetchall():
        users.append(row[1])
        passwords.append(row[2])
        status.append(row[3])

def disconnectFromDatabase(login_db):
    login_db.close()
