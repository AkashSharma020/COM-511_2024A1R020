# Milestone 2 - Multiple Parcels using Collections, Decisions and Loops
# Smart Parcel Dispatch and Delivery Tracker

# service types and their multipliers stored in a dictionary
services = {"Standard": 1.00, "Priority": 1.25, "Same-Day": 1.50}

print("===== Smart Parcel Dispatch - Multiple Parcels =====")
print("Available services:")
for name in services:
    print(f"  {name:<9} x{services[name]:.2f}")
print("Type DONE as the parcel ID to finish.\n")

records = []     # every valid parcel is stored here as a dictionary

# keep taking parcels until the user types DONE
while True:
    parcel_id = input("Enter parcel ID (or DONE): ").upper()
    if parcel_id == "DONE":
        break

    weight = float(input("Enter weight (kg): "))
    distance = float(input("Enter distance (km): "))
    service = input("Enter service (Standard/Priority/Same-Day): ").title()

    # reject an invalid service and move to the next parcel
    if service not in services:
        print("Rejected: '" + service + "' is not a valid service.\n")
        continue

    # reject zero or negative weight/distance
    if weight <= 0 or distance <= 0:
        print("Rejected: weight and distance must be greater than 0.\n")
        continue

    # charge = (weight x 40 + distance x 1.50) x service multiplier
    charge = (weight * 40 + distance * 1.50) * services[service]
    records.append({"id": parcel_id, "weight": weight, "distance": distance,
                    "service": service, "charge": charge})
    print(f"Accepted: {parcel_id} -> Rs. {charge:.2f}\n")

# summary of all valid parcels
print("=" * 52)
print("DISPATCH SUMMARY")
print("=" * 52)

if len(records) == 0:
    print("No valid parcel was entered.")
else:
    total_amount = 0
    longest = records[0]
    print(f"{'Parcel':<8}{'Weight':>8}{'Distance':>10}  "
          f"{'Service':<9}{'Charge':>10}")
    for r in records:
        print(f"{r['id']:<8}{r['weight']:>8.1f}{r['distance']:>10.1f}  "
              f"{r['service']:<9}{r['charge']:>10.2f}")
        total_amount += r["charge"]
        if r["distance"] > longest["distance"]:
            longest = r
    print("-" * 52)
    print("Valid parcel count     :", len(records))
    print(f"Total dispatch amount  : Rs. {total_amount:.2f}")
    print("Longest distance parcel:", longest["id"],
          "(" + str(longest["distance"]) + " km)")
