# Write a program to take a 2 digit number as nput and print the sum of it's digits.

num = int(input("Enter Your number: "))

dig1 = num // 10 
dig2 = num % 10 

print("Sum of digits of the two digit numbers:", dig1+dig2)