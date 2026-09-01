# Write a program to calculate simple interest and total amount using principal, Rate and time entered by user

principle = int(input("Enter Your Amount: "))

rate = float(input("Enter Interest Rate: "))

time = int(input("Enter the Period of time to deposit the amount: "))

simple_interest = (principle*rate*time)/100

total_amount = principle + simple_interest

print(total_amount)