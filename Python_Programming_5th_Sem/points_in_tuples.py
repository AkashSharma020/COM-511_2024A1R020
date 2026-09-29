# Write a python program to store two points as tuples and calculate the distance between them. 

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))

x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

point1 = (x1,y1)
point2 = (x2, y2)

distance = ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5

print("Distance:", distance)

