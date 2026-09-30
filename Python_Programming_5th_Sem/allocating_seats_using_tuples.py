'''
Write a python program to allocatwe seats to a gropu in a single row of cinema hall.
First, input the total number of seats n. Then enter the status of each seat:

    1. 0 means the seat is available. 
    2. 1 means the seat is already booked. 

Next, input the number of people in the group. The progam must find the first consecutive block of
available seats that can accomodate the entire group, If such seats are found:

    1. Book all those seats by changing their status from 0 to 1. 
    2. Display the allocated seat numbers as a tuple.
    Display the updated list of seat statuses. 

If no consecutive block is available, display: Consecutive seats not avaialable and print
the original seat list without any changes. 
Conditions:
    1. Seat nubering starts from 1. 
    2. The group size must be at least 1 and cannot exceed n.
    3. All gropu members must be allotted seats together in consecutive order. 
    4. If more than one suitable block is available, allocate the first block from the left. 
    5. Input seat status must be either 0 or 1. 

Example:
Enter number fo seats:9
Seat Status: [1,0,0,1,0,0,0,0,1]
Enter group size: 3
Expected Output: 
Allocated Seats: (5,6,7)
Updated Seats: [1,0,0,1,1,1,1,0,1]

'''
n = int(input("Enter number of seats: "))

seats = []

for i in range(n):
    status = int(input("Enter seat status (0/1): "))
    seats.append(status)

group = int(input("Enter group size: "))

found = False

for i in range(n - group + 1):

    if all(seats[j] == 0 for j in range(i, i + group)):

        for j in range(i, i + group):
            seats[j] = 1

        allocated = tuple(range(i + 1, i + group + 1))

        print("Allocated Seats:", allocated)
        print("Updated Seats:", seats)

        found = True
        break

if found == False:
    print("Consecutive seats not available")
    print("Original Seats:", seats)
