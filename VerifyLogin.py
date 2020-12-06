# EFFECT: Function to check if combination is correct
def checkCombination(users, passwords, user, password):
    index = 0
    
    # Check if its correct 
    for u in users:
        if (user == u):
            break
        else:
            index = index + 1

    if (user in users):
        if (password == passwords[index]):
            print("Combination Correct")
        else:
            print("Incorrect Username/Password. Please try again.")
