# Write a python program to create a simple password validation system. 

'''
The program should repeatedly ask the user to enter a password until a valid is entered. 
A password will be considered valid only if it has at least 8 characters and contains the @ symbol.

Once the user enters a valid password the program should display "Password Acccepted" and stop. 
Otherwise, it should display "Weak Password. Try Again." and ask for the password again.  '''



while True:
    password = input("Enter your password: ")

    if len(password) >= 8 and "@" in password:
        print("Password Accepted")
        break
    else:
        print("Weak Password. Try Again.")
