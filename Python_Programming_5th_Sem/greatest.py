# Write a program to input 4 numbers from the user and find the greatest number among them. 



num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))
num4 = int(input("Enter 4th number: "))

greatest = max(num1, num2, num3, num4)

print("The Greatest number is:", greatest)
