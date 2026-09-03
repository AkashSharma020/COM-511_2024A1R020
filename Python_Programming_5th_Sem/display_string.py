# Write a program to take a student's full name and display:


''' > The number of characters
     > First Character
     > Last Character
     > Name in uppercase form 
     '''

name = input("Enter Your name: ")


print("Number of characters:", len(name))
print("First character:", name[0])
print("Last character:", name[-1])
print("Name in uppercase:", name.upper())