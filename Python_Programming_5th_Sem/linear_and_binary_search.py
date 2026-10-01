# Write a python program to perform searching activity using Linear and Binary Search.



a = [10, 20, 30, 40, 50]

x = int(input("Enter number to search: "))

# Linear Search
found = False

for i in range(len(a)):
    if a[i] == x:
        print("Linear Search: Found")
        found = True
        break

if found == False:
    print("Linear Search: Not Found")


# Binary Search
low = 0
high = len(a) - 1
found = False

while low <= high:

    mid = (low + high) // 2

    if a[mid] == x:
        print("Binary Search: Found")
        found = True
        break

    elif x > a[mid]:
        low = mid + 1

    else:
        high = mid - 1

if found == False:
    print("Binary Search: Not Found")
