# Take student full name and roll number. Generate email using first 3 letters of first name, first 3 letters of last name, and last 3 characters of roll number. 

name = input("Enter your full name: ")
roll = input("Enter your roll number: ")

first_name, last_name = name.split(" ", 1)

first_name = first_name.lower()
last_name = last_name.lower()

email = first_name[:3] + last_name[:3] + roll[-3:]
print(email+"@gmail.com")