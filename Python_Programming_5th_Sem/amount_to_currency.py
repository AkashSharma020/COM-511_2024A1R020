# Write a program to take an amount in rupees and calculate how many Rs 500 and Rs 100 notes are needed. 


amount = int(input("Enter Your Amount: "))

big_notes = amount // 500

small_notes = (amount % 500)//100

print("Number of 500 rupee notes:", big_notes)
print("Number of 100 rupee notes:", small_notes)

