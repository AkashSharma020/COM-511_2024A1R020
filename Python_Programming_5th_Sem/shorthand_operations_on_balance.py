# Initialize a variable balance = 1000. perform operations using shorthand operators like +=, -=, *=, /= and print the updated balance after each operation. 


amount = 1000

deposit = int(input("Enter amount to deposit: "))

amount += deposit
print("Amount after Deposit operation:", amount)

withdrawl = int(input("Enter amount to withdraw: "))

amount -= withdrawl 
print("Amount after withdraw operation:", amount)

mult = int(input("Enter amount to multiply: "))

amount *= mult 
print("Amount after  multiplicaiton operation:", amount)

div  = int(input("Enter amount to divide: "))

amount /= amount 

print("Amount after  division operation:", amount)