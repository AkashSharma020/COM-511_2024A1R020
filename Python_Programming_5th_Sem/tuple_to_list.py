# Write a python program to show that tuple values can not be changed directly. Convert tuple into list, update it, and convert it back into tuple. 

t = (10,20,30)

print("Original tuple:", t)

l =  list(t)
l[1] = 50

t = tuple(l)
print("Updated Tuple:", t)

