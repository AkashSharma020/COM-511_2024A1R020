# Write a python program to input a number and reverse it using arithmetic operations only. 

num = int(input("Enter the number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reverse of the number is:", reverse)
