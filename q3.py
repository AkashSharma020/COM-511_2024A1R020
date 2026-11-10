# Milestone 3 - Standard and Express Parcels using OOP (inheritance)
# Smart Parcel Dispatch and Delivery Tracker

class Parcel:
    company_name = "SwiftTrack Logistics"        # class variable

    # constructor
    def __init__(self, parcel_id, receiver_name, weight_kg, distance_km):
        self.parcel_id = parcel_id
        self.receiver_name = receiver_name
        self.weight_kg = weight_kg
        self.distance_km = distance_km

    # standard charge = weight x 40 + distance x 1.50
    def calculate_charge(self):
        return self.weight_kg * 40 + self.distance_km * 1.50

    def display_details(self):
        print("-" * 40)
        print(" ", Parcel.company_name.upper())
        print("-" * 40)
        print("Parcel Type :", type(self).__name__)
        print("Parcel ID   :", self.parcel_id)
        print("Receiver    :", self.receiver_name)
        print("Weight      :", self.weight_kg, "kg")
        print("Distance    :", self.distance_km, "km")
        print(f"Charge      : Rs. {self.calculate_charge():.2f}")
        print("-" * 40)

    # short summary used by print(object)
    def __str__(self):
        return (f"{self.parcel_id} | {self.receiver_name} | "
                f"{self.weight_kg} kg | {self.distance_km} km")


class ExpressParcel(Parcel):
    # method overriding: 25% express surcharge on the standard charge
    def calculate_charge(self):
        base_charge = super().calculate_charge()
        return base_charge + base_charge * 0.25


# creating one object of each class
parcel1 = Parcel("PKG401", "Rohan Verma", 2.5, 120)
parcel2 = ExpressParcel("PKG402", "Simran Kaur", 2.5, 120)

parcel1.display_details()
parcel2.display_details()

# same method name, different result (polymorphism)
print("\nPolymorphism check:")
for p in (parcel1, parcel2):
    print(f"{type(p).__name__:<14} calculate_charge() = "
          f"Rs. {p.calculate_charge():.2f}")

print("\nObject summaries:")
print(parcel1)
print(parcel2)
