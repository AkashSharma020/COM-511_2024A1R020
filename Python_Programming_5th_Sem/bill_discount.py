# Write a program to calculate the final bill amount after applying a discount. The program should take the total bill amount as input from the user and apply the discount according to the following rules. After calculating the discount, the program should ddisplay the discount and the final bill amount payable by the customer.

'''
Bill Amount          Discount
Above 5000           20 percent
3000 to 5000         10 percent
Below 3000           No discount
'''

bill_amount = int(input("Enter the actual Bill amount: "))

if bill_amount > 5000:
    bill_amount = bill_amount - (0.2*bill_amount) 
    print("Amount to pay after discount:", bill_amount)

elif bill_amount <= 5000 and bill_amount >= 3000:
    bill_amount = bill_amount - (0.1*bill_amount) 
    print("Amount to pay after discount:", bill_amount)


elif bill_amount < 3000:
    print("The final bill:", bill_amount)


