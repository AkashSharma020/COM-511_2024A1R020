# q5.py - Milestone 5 (final version)
# Smart Parcel Dispatch and Delivery Tracker
# Run with:  python q5.py

from delivery_utils import (SERVICES, calculate_charge, classify_weight,
                            estimate_delivery_hours, save_record, read_records)


class Parcel:
    company_name = "SwiftTrack Logistics"

    def __init__(self, parcel_id, receiver_name, weight_kg, distance_km):
        self.parcel_id = parcel_id
        self.receiver_name = receiver_name
        self.weight_kg = weight_kg
        self.distance_km = distance_km

    def calculate_charge(self):
        return calculate_charge(self.weight_kg, self.distance_km)

    def display_details(self):
        print("-" * 44)
        print("  " + Parcel.company_name.upper())
        print("-" * 44)
        print("Parcel Type  :", type(self).__name__)
        print("Parcel ID    :", self.parcel_id)
        print("Receiver     :", self.receiver_name)
        print("Weight       :", self.weight_kg, "kg",
              "(" + classify_weight(self.weight_kg) + ")")
        print("Distance     :", self.distance_km, "km")
        hours = estimate_delivery_hours(self.distance_km)
        print("Delivery Time:", hours, "hour(s)")
        print(f"Charge       : Rs. {self.calculate_charge():.2f}")
        print("-" * 44)

    def __str__(self):
        return (f"{self.parcel_id} | {self.receiver_name} | "
                f"{self.weight_kg} kg | {self.distance_km} km")


class ExpressParcel(Parcel):
    def __init__(self, parcel_id, receiver_name, weight_kg, distance_km,
                 surcharge=0.25):
        super().__init__(parcel_id, receiver_name, weight_kg, distance_km)
        self.surcharge = surcharge

    # method overriding: add the express surcharge on the standard charge
    def calculate_charge(self):
        base_charge = super().calculate_charge()
        return base_charge + base_charge * self.surcharge


def dispatch_parcel():
    try:
        parcel_id = input("Enter parcel ID: ").upper()
        receiver = input("Enter receiver name: ").title()
        weight = float(input("Enter weight (kg): "))        # may raise ValueError
        distance = float(input("Enter distance (km): "))    # may raise ValueError
        if weight <= 0 or distance <= 0:
            raise ValueError("weight and distance must be positive")
        service = input("Enter service (Standard/Priority/Same-Day): ").title()
        multiplier = SERVICES[service]                      # may raise KeyError

        # Standard service -> Parcel, Priority/Same-Day -> ExpressParcel
        if multiplier == 1.00:
            parcel = Parcel(parcel_id, receiver, weight, distance)
        else:
            parcel = ExpressParcel(parcel_id, receiver, weight, distance,
                                   multiplier - 1)

    except ValueError:
        print("Error: weight and distance must be positive numbers.")
        print("Parcel not saved.")
    except KeyError:
        print("Error: service '" + service + "' is not available.")
        print("Parcel not saved.")
    else:
        parcel.display_details()
        charge = parcel.calculate_charge()
        line = (f"{parcel_id} | {receiver} | {service} | {weight} kg | "
                f"{distance} km | Rs. {charge:.2f}")
        save_record(line)
        print("Record saved to parcel_records.txt")


def view_records():
    try:
        records = read_records()
    except FileNotFoundError:
        print("No dispatch records found yet. Dispatch a parcel first.")
    else:
        print("\n====== SAVED DISPATCH RECORDS ======")
        for record in records:
            print(record.strip())


# main menu
print("===== Smart Parcel Dispatch and Delivery Tracker =====")
while True:
    print("\n1. Dispatch New Parcel\n2. View Dispatch Records\n3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        dispatch_parcel()
    elif choice == "2":
        view_records()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
