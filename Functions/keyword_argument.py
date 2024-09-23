# These are arguments identified by their parameter names when passed to a function or script. They allow you to specify which parameter each argument corresponds to, regardless of the order.

def greet(name, greeting):
  print(f"{greeting}, {name}!")
  
  
#passing keyword argument
greet(greeting="Hello", name="Bob")

def user_info(name, age=None):
  """Prints user information."""
  print(f"Name: {name}")
  if age:
    print(f"Age: {age}")

user_info(name="Bob", age=30)


# *Default Values 
# *Function definition with default values 
def greet(name="World"):
  """Prints a greeting message."""
  print(f"Hello, {name}!")
greet()  # Output: Hello, World!
greet("Alice")  # Output: Hello, Alice! 


#* Return are the values that a function sends back to a caller after execution. 
def square(number):
  """Returns the square of a number"""
  return number * number

squared_value = square(4)
print(squared_value)