#print("Hello Python!")

# This is a single line comment

"""This is a multi-line comment
    1. This is comment
    2. This is a comment 
     """

'''
 problems: 
 
 4. Write a python program to print the contents of a directory using the os module. Search online for the fnuctoin which does that'''


'''
import os 

contents = os.listdir(".")

for item in contents:
    print(item)

    '''


# current working directory
'''
import os

print(os.getcwd())
'''

# Create another directory in present working directory using os module 

'''
import os 
os.mkdir("Practice Directory")
'''

# Printing path of any folder present 
'''
import os 
print(os.path.exists("Practice Directory"))
'''

# Renaming a folder 

'''
import os 
os.rename("hello.py", "Hello.py")
'''

# Checking whether a function exists or not

'''
import os 
print(os.path.isfile("Practice Directory"))
'''


# Checking whether a directory exists or not 
'''
import os 
print(os.path.isdir("Practice Directory"))
'''

# Remove a file 
'''
import os 
os.remove("practice1.py")
'''


# Removing a Driectory/Folder

import os 
os.rmdir("practice")