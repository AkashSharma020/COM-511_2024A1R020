# Write a python program to input a student's marks in n consecutive tests and and store them in a list. Find the longest consecutive sequence in which each mark is strictly greater than the previous mark. 

# Display the sequence, it's length and it's starting and ending test numbers as a tuple. If multiple swquences have the same maximum length, display the first one. 


'''
Marks : [55, 60, 68, 62, 65, 70, 78,74]
Longest improving sequence: [62, 65, 70, 78]
Number of tests: 4
Test Range: [4,7]

Conditions:
> Accept at least one test.
> Equal marks break the improving sequence. 
> Test numbers begin at 1.
> Do not sort the list because the original test order matters.

'''
n = int(input("Enter number of tests: "))

marks = []
for i in range(n):
    marks.append(int(input("Enter marks: ")))

longest = []
current = []

for i in range(n):
    if i == 0 or marks[i] > marks[i - 1]:
        current.append(marks[i])
    else:
        current = [marks[i]]

    if len(current) > len(longest):
        longest = current.copy()

start = marks.index(longest[0]) + 1
end = start + len(longest) - 1

print("Marks:", marks)
print("Longest improving sequence:", longest)
print("Number of tests:", len(longest))
print("Test Range:", (start, end))



