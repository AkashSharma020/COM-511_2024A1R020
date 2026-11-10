# q4.py - Milestone 4
# Smart Parcel Dispatch and Delivery Tracker (functions + module)

from delivery_utils import (calculate_charge, classify_weight,
                            estimate_delivery_hours, summarize_records,
                            sort_by_distance)


class Parcel:
    company_name = "SwiftTrack Logistics"

    def __init__(self, parcel_id, receiver_name, weight_kg, distance_km):
        self.parcel_id = parcel_id
        self.receiver_name = receiver_name
        self.weight_kg = weight_kg
        self.distance_km = distance_km

    def calculate_charge(self):
        # uses the function from delivery_utils
        return calculate_charge(self.weight_kg, self.distance_km)

    def display_details(self):
        print(f"{self.parcel_id} | {self.receiver_name} | {self.weight_kg} kg | "
              f"{self.distance_km} km | Rs. {self.calculate_charge():.2f}")

    def __str__(self):
        return (f"{self.parcel_id} | {self.receiver_name} | "
                f"{self.weight_kg} kg | {self.distance_km} km")


class ExpressParcel(Parcel):
    def calculate_charge(self):
        base_charge = super().calculate_charge()
        return base_charge + base_charge * 0.25


# sample parcels
parcels = [
    Parcel("PKG501", "Aarav Gupta", 1.5, 35),
    ExpressParcel("PKG502", "Meera Pandey", 4.0, 220),
    Parcel("PKG503", "Kabir Singh", 7.5, 90),
    ExpressParcel("PKG504", "Isha Malhotra", 0.8, 150),
]

# build the parcel-record collection (list of dictionaries)
records = []
for p in parcels:
    records.append({"id": p.parcel_id, "type": type(p).__name__,
                    "weight": p.weight_kg, "distance": p.distance_km,
                    "charge": p.calculate_charge()})

# sort by distance using the lambda-based function
sorted_records = sort_by_distance(records)

print("========== Smart Parcel Dispatch - Delivery Summary ==========")
print(f"{'Parcel':<8}{'Type':<15}{'Weight':>7}{'Class':>8}"
      f"{'Km':>6}{'Hours':>7}{'Charge':>10}")
print("-" * 61)
for r in sorted_records:
    hours = estimate_delivery_hours(r["distance"])     # default speed 40 km/h
    weight_class = classify_weight(r['weight'])
    print(f"{r['id']:<8}{r['type']:<15}{r['weight']:>7.1f}{weight_class:>8}"
          f"{r['distance']:>6}{hours:>7}{r['charge']:>10.2f}")
print("-" * 61)

total_amount, average_distance = summarize_records(records)
print(f"Total amount     : Rs. {total_amount:.2f}")
print(f"Average distance : {average_distance:.2f} km")

# keyword argument: the same parcel with a faster vehicle (60 km/h)
print("\nKeyword argument demo for PKG502 (220 km):")
print("  Default speed 40 km/h ->", estimate_delivery_hours(220), "hours")
print("  average_speed=60 km/h ->",
      estimate_delivery_hours(220, average_speed=60), "hours")
