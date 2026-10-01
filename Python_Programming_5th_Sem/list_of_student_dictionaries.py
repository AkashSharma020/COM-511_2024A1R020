'''
Write a program to create records of n students. Store each student record
as a dictionary containing roll number, name, branch and marks. Store all records in a list and
search for a student using roll number. (Condition: Roll numbers must be unique.)
'''


n = int(input("Enter number of students: "))

students = []


for i in range(n):
    roll_no = int(input("Enter Roll Number: "))
    for stu in students:
        if roll_no == stu[0]:
            print("Already exists! Enter Unique Roll")
            roll_no = int(input("Enter Roll Number: "))
    name = input("Enter name of Student: ")
    branch = input("Enter branch of the Student: ")
    marks = int(input("Enter Makrs of the Studnet: "))

    stu_dict = {
        "roll_no" : roll_no,
        "name" : name,
        "branch" : branch,
        "marks" : marks
    }

    students.append(stu_dict)

search_roll = int(input("Enter roll number to search: "))

for i in range(n):
    if students[i]["roll_no"] == search_roll:
        print("Student Record:")
        print(students[i])
        break
else:
    print("Records not found!!!")

