# Write a program to take two inputs a and b, swap their values using a temporary variable, and print updated values. 


a = int(input("Enter first variable: "))
b = int(input("Enter second variable: "))

temp = a 
a = b 
b = temp 

print("The updated values are: ")
print("a =", a)
print("b =", b)