# Write a program to take input from the user without typecasting and multiply it by 3. Then typecast the same input to int and multiply it by 3. Print both results to show the difference. 

num = input("Enter your number: ")

num1 = num*3
print("Result of multiplication without typecasting:", num1)

num = int(num)

num2 = num*3

print("Result of multipilcation with typecasting:", num2)

