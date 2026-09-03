# Write a python program to take a passowrd and check whether it contains @ and has at least 8 characters. 


password = input("Enter Your Password: ")

has_at_symbol = "@" in password
has_min_length = len(password) >= 8 

is_valid = has_at_symbol and has_min_length

status_messages = {
    True: "Password is valid.", 
    False: "Invalid Password. It must be at least 8 characters long and contain '@'. " 
}

print(status_messages[is_valid])

