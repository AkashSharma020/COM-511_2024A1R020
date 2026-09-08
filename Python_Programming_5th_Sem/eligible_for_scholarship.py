# Write a python program to determine whether a student is eligilble for scholarship. 

'''
 The schorlarship should be granted if the student satisfies either of the following conditions:
 
 a) The student has a cgpa of 8.5 or above and attendance of 85 percent or above. 
 b) The student has won a national-level competition.
 
 The program should take CGPA, attendance percentage, and national level competitions status as input, then display whether the student is eligible for the scholarship. 
 
 '''

cgpa = float(input("Enter your CGPA: "))

attendance = input("Enter your attendance(in percentage): ")

comp = input("Have you won any national level competitions(yes/no): ")

if cgpa >= 8.5 and attendance >= 85 and comp == 'yes':
    print("Eligible for scholarship!!!")

else:
    print("Hat Saala Anpadh Gareeb!!")