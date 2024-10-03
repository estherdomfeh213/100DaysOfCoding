def check_positive(number):
  if number < 0:
    raise ValueError("This number must be positive!")
  
  
try:
  check_positive(-5)
except ValueError as e:
  print(e)