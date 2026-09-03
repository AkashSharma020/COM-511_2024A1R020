# Write a program to take an email address and print the domain name. 

mail = input("Enter your email id: ")


domain = mail.split("@")[1]

print("Domain name:", domain)