# Write a program that asks the user to enter a username and password. The user should get only 3 attempts. If the correct credentials are entered, display "Login Successful" and stop the loop. If all attempts are used, display "Account Locked".


username = "abc@123" 
password = "password@123"

for i in range(1,4):
    user = input("Enter your Username: ")
    pasw = input("Enter your Password: ")

    if "abc@123" in user and "password@123" in pasw:
        print("Login Successful!")
        break
    else:
        print("Either Username or Password is invalid! Try Again")
print("Account locked!!!")
