# Write a program to input numbers in a list and find the second largest number. 

n = int(input("Enter the number of enteries: "))

list = []

for i in range(n):
    m = float(input(f"Enter the {i + 1}st entry: "))
    list.append(m)

largest = list[0]
second_largest = list[0]

for i in range(1, n):
    if list[i] > largest:
        second_largest = largest
        largest = list[i]
    elif list[i] > second_largest and list[i] != largest:
        second_largest = list[i]

print("The second largest number is:", second_largest)
