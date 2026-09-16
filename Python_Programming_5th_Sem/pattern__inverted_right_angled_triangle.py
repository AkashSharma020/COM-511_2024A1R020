# WAP to print an inverted right angles triangle. 

# 12. Write a Python program to print an inverted right-angle triangle
n = int(input("Enter number of rows: "))
for i in range(n, 0, -1):
    print("* " * i)

