# Write a python program to check whether a given value is present in a tuple. If present, display it's position.


numbers = (10, 20, 30, 40, 50)


value = int(input("Enter the value to search: "))


if value in numbers:
    position = numbers.index(value)
    print(value, "is present at position", position)
else:
    print(value, "is not present in the tuple.")
