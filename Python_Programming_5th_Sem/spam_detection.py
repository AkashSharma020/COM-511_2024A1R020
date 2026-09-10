# Write a python program to detect whether a comment is spam or not a comment should be reated as spam if it contains any of these keywords. "Make a lot of money", "buy now", "subscribe this ", "Click this"


cmnt = input("Enter your comment: ")

cmnt = cmnt.lower()

if "make a lot of money "in cmnt or "subscribe this" in cmnt or "buy now" in cmnt or "click this" in cmnt:
    print("This is a spam comment!")

else:
    print("This is not a spam message!")

