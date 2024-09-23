def outer_function():
  x = 10 # Variable in enclosing function 
  
  def inner_function():
    nonlocal x # Using nonlocal to modify x from the enclosing function
    x += 5
  inner_function() # Calling the nested function 
  print("Modified value of x from inner function:", x)
  outer_function()
  
