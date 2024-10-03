# We catch multiple exceptions using a tuple 

try:
  value = int(input("Enter a number: ")) # Might cause a ValueError 
  result = 10 / value  # Might cause a ZeroDivisionError
except (ValueError, ZeroDivisionError) as e:
  print(f"An error occurred: {e}") # This will catch both errors and print a message
