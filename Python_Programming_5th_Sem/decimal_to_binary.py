# Write a program to input a decimal number and convert it into binary without using the built-in-bin() function. 

num = int(input("Enter a decimal number: "))

binary = ""

while num > 0:
    remainder = num % 2
    binary = str(remainder) + binary
    num = num // 2

print("Binary number is:", binary)
