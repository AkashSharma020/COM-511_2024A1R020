# Write a program to take an email address and print username, domain, and reversed domain


mail = input("Enter your email id: ")

username = mail.split("@") [0]

domain = mail.split("@") [1]

domain_reverse = domain[::-1]

print("Username:", username)
print("Domain:", domain)
print("Reversed Domain:", domain_reverse)


