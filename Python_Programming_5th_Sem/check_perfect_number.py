# Write a program to check whether a number is a perfect number. A number is perfect if the sum of it's proper divisors is equal to the number itself. 

num = int(input("Enter the number: "))

sum_divisors = 0

for i in range(1, num):
    if num % i == 0:
        sum_divisors += i

if sum_divisors == num:
    print("The number is a perfect number.")
else:
    print("The number is not a perfect number.")
