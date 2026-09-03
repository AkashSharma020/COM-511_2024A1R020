# Write a program to take a string and separate characters present at even index positions and odd indes positions. 

string = input("Enter a string: ")

even_index_chars = string[::2]

odd_index_chars = string[1::2]

print(f"Characters at even indices: {even_index_chars}")
print(f"Characters at odd indices: {odd_index_chars}")