# Write a program to take student details like name, roll number, CGPA and hosel status from the user. Typecast them into appropriate types and print them along with their detected type. 


name = input("Enter your name: ")

roll_no = int(input("Enter your roll number: "))

cgpa = float(input("Enter your CGPA: "))

hostel_status = bool(int(input("Enter your hostel status")))

print("Name of Student: ", name)
print(type(name))

print("Roll number of student:", roll_no)
print(type(roll_no))

print("CGPA of student:", cgpa)
print(type(cgpa))


print("Hostel Status:", hostel_status)
print(type(hostel_status))