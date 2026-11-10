# delivery_utils.py - Milestone 5 (final version)
# Reusable functions + file handling for the Smart Parcel Dispatch Tracker

import math

# service types and their multipliers
SERVICES = {"Standard": 1.00, "Priority": 1.25, "Same-Day": 1.50}


# standard delivery charge (default rates: Rs. 40/kg and Rs. 1.50/km)
def calculate_charge(weight, distance, weight_rate=40, distance_rate=1.50):
    return weight * weight_rate + distance * distance_rate


# classify a parcel by its weight
def classify_weight(weight):
    if weight <= 2:
        return "Light"
    elif weight <= 5:
        return "Medium"
    else:
        return "Heavy"


# delivery time in whole hours, default average speed is 40 km/h
def estimate_delivery_hours(distance, average_speed=40):
    return math.ceil(distance / average_speed)


# returns the total amount and the average distance of all records
def summarize_records(records):
    total_amount = 0
    total_distance = 0
    for record in records:
        total_amount += record["charge"]
        total_distance += record["distance"]
    return total_amount, total_distance / len(records)


# sort the records by distance (longest first) using a lambda expression
def sort_by_distance(records):
    return sorted(records, key=lambda record: record["distance"], reverse=True)


# append one dispatch record to the file (append mode keeps the old records)
def save_record(line, filename="parcel_records.txt"):
    with open(filename, "a") as file:
        file.write(line + "\n")


# read all saved records; raises FileNotFoundError if the file is missing
def read_records(filename="parcel_records.txt"):
    with open(filename, "r") as file:
        return file.readlines()
