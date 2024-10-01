# A Person Class 
class Person:
  
  def __init__(self, name, age):
    # constructor method to initialize the object's attributes
    self.name = name #'self.name' refers to the 'name' of the object 
    self.age = age  # 'self.age' refers to the 'age' of the object
    
    
  def say_hello(self):
    # Using 'self' to access the object's attributes 
    print(f"Hello, my name is {self.name} and I am {self.age} years old")
    

# * Creating an object     
person1 = Person('Alice', 24)

person1.say_hello()
