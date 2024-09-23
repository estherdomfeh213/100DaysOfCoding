# A function to check if a number is even or odd

def is_even(number):
  """Check if number is even."""
  if number % 2 == 0:
    return f"{number} is Even."
  else: 
    return f"{number} is Odd."
    
print(is_even(2))
print(is_even(3))
print(is_even(6))
print(is_even(0))