# Write a python program to store repeated values in a tuple and count how many times a given value appears


numbers = (10, 20, 10, 30, 20, 10, 40, 20)


value = int(input("Enter the value to count: "))


count = numbers.count(value)

print(value, "appears", count, "times in the tuple.")
