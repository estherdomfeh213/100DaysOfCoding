try:
  num = int(input("Enter a number: "))
  result = 10 / num 
except  ZeroDivisionError:
  print("You can't divide by zero!")
except ValueError:
  print("Invalid input! Please enter a number.")
# This runs if there were no errors
else:
  print(f"The result is {result}.")
# This is always 
finally:
  print("Execution completed.")