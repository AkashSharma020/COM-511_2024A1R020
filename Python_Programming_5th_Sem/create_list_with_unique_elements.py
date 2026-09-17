# Write a program to input a list of numbers and create a new list containing only unique elements.


n = int(input("Enter the number of entries: "))

numbers = []
unique = []

for i in range(n):
    m = float(input(f"Enter the {i + 1}st entry: "))
    numbers.append(m)

for i in range(n):
    if numbers[i] not in unique:
        unique.append(numbers[i])

print("List containing unique elements:", unique)
