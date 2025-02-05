# Ask user for their name
# comments are notes to yourself in your code/ can also serve as pseudocode 
name = input("What's your name? ").strip().title()

# Split users name into first name and last name 
first, last = name.split(" ")

print(f"hello, {first}")
print(f"hello, {last}")

# #* Say hello to user 
# print("hello", name)

# # Remove whitespace from str
# name = name.strip()

# # Capitalize user's name 
# name = name.capitalize()

# name = name.title()

# # Remove whitespace from str and capitalize user's name 
# name = name.strip().title()


# print("hello," + name)
# print("hello, " + name)

# print("hello, ", name )

# print("hello " + name + "!")


#! reading python print fuction documentation 
"""
print(*objects, sep=' ', end='\n', file=None, flush=False)
Print objects to the text stream file, separated by sep and followed by end. sep, end, file, and flush, if present, must be given as keyword arguments.
"""
# print("hello,", name, sep="???")
# print ("hello," , name, end="&&&")


# # escape charaters \
# print("hello \"friend\"")

# # format string 
# print(f"hello, {name}")

