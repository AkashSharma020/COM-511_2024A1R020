# Write a program to tkae a word and print it in reverse order using slicing. Also check whether it is the same forward and backward. 

word = input("Enter your word: ")
reversed_word = word[::-1]

print("Reversed Word:", reversed_word)

print("Pallindrome:", word == reversed_word)

