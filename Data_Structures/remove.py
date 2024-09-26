# Removing is deleting elements from a list. 
# ! You can use the remove() method to delete a specific element by its value or use the del keyword followed by the index to delete by index.

my_list = [10, 20, 30, 40, 50]

print(my_list)

my_list.remove(30)

print(my_list)

#?  use the del keyword followed by the index to delete by index.
del my_list[2]
print(my_list)