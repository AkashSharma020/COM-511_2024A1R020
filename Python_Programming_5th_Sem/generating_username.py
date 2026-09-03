# Write a program to take a student name and roll number, then generate a username using the first letters of the name asn last 2 digits of the roll number



name = input("Enter your name: ")

roll_no = input("Enter your roll number: ")

username = name[:3] + roll_no[-2:]

print("Username:", username)