# Write a program to input marks of n students in a list. Display highest marks, lowest marks, average marks and number of students who passed. 


n = int(input("Enter number of students: "))

marks = []

for i in range(n):
    m = float(input(f"Enter marks of student {i + 1}: "))
    marks.append(m)

print("Highest marks:", max(marks))
print("Lowest marks:", min(marks))
print("Average marks:", sum(marks) / n)

passed = 0
for m in marks:
    if m >= 40:
        passed += 1

print("Number of students passed:", passed)
