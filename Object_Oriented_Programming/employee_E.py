# class employee
class Employee: 
  
  def __init__(self, name, salary=0):
    self._name = name 
    self._salary = salary         #private attributes name and salary
    
  def get_name(self):
    return f"Employee Name: {self._name}"

  def get_salary(self):
    return f"Salary: {self._salary}"
  
  def set_salary(self, new_salary):
    if new_salary > self._salary:
      self._salary =  new_salary # update salary , dont all (+=)
      return f"Salary updated to: {self._salary}"
    else: 
       return f"New salary {new_salary} is lower or equal to the current salary. Update rejected."
  
  
  
# Create an instance of Employee class
employee1 = Employee('Benjamin')


print(employee1.get_name())
print(employee1.get_salary())
print(employee1.set_salary(200))