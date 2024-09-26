# Take user input and use function check if number meet conditions 
number = int(input("Please enter an integer: "))

def change_integer(number):
  match number:
    case _ if number < 0:
      number = 0
      return 'Negative changed to zero'
    case _ if number == 0:
      return "Zero"
    case _ if number == 1:
      return "Single"
    case _:
      return "More"
    
print(change_integer(number))