# Write a python program to take a word and count the number of vowels a,e,i,o,u

word = input("Enter the word: ")

count = word.count("a") + word.count("e") + word.count("i") + word.count("o") + word.count("u")

print(count)