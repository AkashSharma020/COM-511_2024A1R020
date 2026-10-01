'''
Create a database using lists and tuples. Each student record must contain roll number, name,
branch, and CGPA. Store each record as a tuple inside a list. Display all records and search for a student using 
roll number.

Conditions:
> Each record should be stores as a tuple. 
> The complete datacase should be stored as a list. 
> Roll numbers must be unique. 
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
    cgpa = float(input("Enter CGPA of the Studnet: "))

    stu = (roll_no, name, cgpa  )

    students.append(stu)


print("\nAll Student Records:")

for i in range(n):
    print(students[i])

search_roll = int(input("Enter roll number to search: "))

for i in range(n):
    if students[i][0] == search_roll:
        print("Student Record:")
        print(students[i])
        break
else:
    print("Records not found!!!")
