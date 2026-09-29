# Write a python program to store all month names in a tuple. Input a month number and display the corresponding month name. 

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", 
          "October", "November", "December")

month_no = int(input("Enter month number: "))

if month_no >= 1 and month_no <= 12:
    print("Month:", months[month_no - 1])

else:
    print("Invalid month number!!")
    
