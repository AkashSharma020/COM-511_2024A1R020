# Take a sentence containing double spaces an unwanted spaces at the beginning or end. Clean the sentence. 

sent = input("Enter the sentence: ")
cleaned_sentence = " ".join(sent.split())

print(f"Original: '{sent}'")
print(f"Cleaned: '{cleaned_sentence}'")

