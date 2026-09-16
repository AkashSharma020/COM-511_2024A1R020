# Write a python program to print a square pattern of stars for n rows and

n = int(input("Enter the number of rows and columns: "))

for i in range(n):
    for j in range(n):
        print("*", end = " ")
    print()

    
