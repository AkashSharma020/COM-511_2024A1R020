# Write a program to input two numbers and find their greatest common divisor using a loop.


import math
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

result = math.gcd(num1, num2)
print("GCD is:", result)
