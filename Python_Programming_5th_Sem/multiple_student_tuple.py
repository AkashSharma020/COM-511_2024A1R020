# Write a program to store multiple student records as a list of tuples. Each tuple should contain name, roll number and marks. Display students who scored above 75. 

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter name: ")
    roll_no = int(input("Enter roll number: "))
    marks = float(input("Enter marks: "))
    students.append((name, roll_no, marks))

print("Students who scored above 75:")

for student in students:
    if student[2] > 75:
        print(student)
