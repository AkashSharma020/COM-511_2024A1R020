# Milestone 1 - Calculate the Charge for One Parcel
# Smart Parcel Dispatch and Delivery Tracker

print("===== Smart Parcel Dispatch - Single Parcel Charge =====")

# taking input and converting numbers to float
sender_name = input("Enter sender name: ")
parcel_id = input("Enter parcel ID: ")
weight = float(input("Enter weight (kg): "))
distance = float(input("Enter distance (km): "))
weight_rate = float(input("Enter weight rate per kg (Rs.): "))
distance_rate = float(input("Enter distance rate per km (Rs.): "))

# checking the data types
print("\nData type of weight   :", type(weight))
print("Data type of distance :", type(distance))

# charge calculation
weight_charge = weight * weight_rate
distance_charge = distance * distance_rate
total_charge = weight_charge + distance_charge

# printing the slip, title() and upper() change the text style
line = "-" * 44
print()
print(line)
print("         SMART PARCEL DISPATCH SLIP")
print(line)
print("Sender Name     :", sender_name.title())
print("Parcel ID       :", parcel_id.upper())
print(f"Weight          : {weight} kg")
print(f"Distance        : {distance} km")
print(line)
print(f"Weight Charge   : {weight} x {weight_rate:.2f} "
      f"= Rs. {weight_charge:.2f}")
print(f"Distance Charge : {distance} x {distance_rate:.2f} "
      f"= Rs. {distance_charge:.2f}")
print(line)
print(f"Total Charge    : Rs. {total_charge:.2f}")
print(line)
