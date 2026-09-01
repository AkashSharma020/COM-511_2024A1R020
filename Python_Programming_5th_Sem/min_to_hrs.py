# Write a python program to take total minutes as input and convert it inot hours and remaining minutes


time = int(input("Enter the Total Minutes: "))

hours = time // 60 
minutes = time % 60 

print("Hours:", hours)
print("Minutes:", minutes)

