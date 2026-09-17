# Write a program to input marks of 10 students. Store only valid marks between 0 and 100 in a list. Skip invalid marks.  

marks = []

for i in range(0,10):
     m = float(input(f"Enter marks of student {i + 1}: "))
     if m >= 0 and m <= 100:
            marks.append(m)

print(marks)
