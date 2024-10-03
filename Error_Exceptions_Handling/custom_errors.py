# you can create custom exceptions by defining a new class that inherits from the built-in Exception class (or any other appropriate exception class). This allows you to define errors specific to your program's logic.

class MyCustomError(Exception):
  def __init__(self, message, code=None):
    self.message = message
    self.code = code 
    super().__init__(self.message)
    
    
# Usage
try:
  raise MyCustomError("An error occurred", code=404)
except MyCustomError as e:
  print(f"Error: {e.message}, Code: {e.code}")