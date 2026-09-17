# Write a program to input numbers in a list and create two separate lists for even and odd numbers. 

n = int(input("Enter the number of enteries: "))

list = []

for i in range(n):
    m = float(input(f"Enter the {i + 1}st entry: "))
    list.append(m)

even = []
odd = []

for i in range(n):
     if list[i] % 2 == 0:
         even.append(list[i])

     else:
         odd.append(list[i])


print("Even numbers:", even) 
print("Odd numbers:", odd)

# Example
'''
Enter the number of enteries: 5
Enter the 1st entry: 20
Enter the 2st entry: 33
Enter the 3st entry: 45
Enter the 4st entry: 90
Enter the 5st entry: 21
Even numbers: [20.0, 90.0]
Odd numbers: [33.0, 45.0, 21.0]
'''
