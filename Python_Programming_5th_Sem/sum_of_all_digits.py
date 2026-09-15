# Write a program to repeatedly calculate the sum of digits of a number until the result becomes a single digit.

num = int(input("Enter the number: "))

while num >= 10:
    sum = 0

    while num > 0:
        sum += num % 10
        num = num // 10

    num = sum

print("The single digit result =", num)
