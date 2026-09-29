# Write a python program to store one student data as a tuple:name, roll number, and marks. Display grade based on marks. 


name = input("Enter student name: ")
roll_no = int(input("Enter roll number: "))
marks = int(input("Enter marks: "))


student = (name, roll_no, marks)


print("\nStudent Data:")
print("Name:", student[0])
print("Roll Number:", student[1])
print("Marks:", student[2])


if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)
