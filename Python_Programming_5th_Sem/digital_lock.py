# Write a python code to simulate a digital lock system. 

''' The lock Should ask the user to enter a 4 digit PIN. If the entered PIN does not contain
exactly 4 digits, the program should display an error message and ask again. If the entered PIN is correct, the
lock should open. Otherwise, the program should ask the user to try again. 
'''


pin = input("Enter the PIN Here: ")

if len(pin) != 4:
    print("Error! Try Again.") 

elif pin == '1234':
    print("Lock Opened!")

else:
    print("Wrong PIN entered, try again!")




