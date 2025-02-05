# 1. Insert the missing part of the code below to output "Hello World".
print("Hello World")

# 2. Complete the code block, print "YES" if 5 is larger than 2.
# Hint: remember the indentation.
# if 5 > 2:

if 5 > 2:
  print("YES")
  
  
# Comments in Python are written with a special character, which one?
# This is a comment

#* This is a comment

# correct syntax to print data type 
myvar = "esther"

print(type(myvar))

# Create a variable named carname and assign the value Volvo to it
carname = "Volvo"

# Create a variable named x and assign the value 50 to it.
x = 50 

# Pyhton multiple variable 
x=y=z= "My name is Esther"
print(x)
print(y)
print(z)

# Insert the correct syntax to assign values to multiple variables in one line:
#  "Orange", "Banana", "Cherry"

x,y,z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


fruits = ['apple', 'banana', 'cherry']
a, b, c = fruits 
print(a)


# * Python Global variable

x = "awesome"  # this is a global variable 

def myfunc():
  x = 'fantastic'
myfunc()
print('Python is ' + x)

# Convert x into float 
x = 5 
x = float(x)
print(type(x))

# Python complex number 
x = complex(x)
print(type(x))

#! Python Casting: is the process of converting the value of one type into the value of another
print(int(35.88))

# Python Strings 
# Get the first character of the string txt.
txt = "Hello World"
x = txt[0]
print(x)


# Insert the correct keyword to check if the word 'free' is present in the text:

txt = 'The best things in life are free!'
if 'free' in   txt:
  print('Yes, free is present in the text.')
  

# Get the characters from index 2 to index 4 (llo).

txt = "Hello World"
x = txt[2:5]
print(x)

# Python Modify Strings 
# What is a correct syntax to print a string in upper case letters?
x = "Welcome".upper()
print(x)

# Remove whitespacce at the beginning and end
print(x.strip())

# Convert to lowercase 
print(x.lower())

# Replace the character H with a J.
txt = "Hello World"
txt = txt.replace('H','J')
print(txt)