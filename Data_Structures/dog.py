class Dog:
  
  def __init__(self, name, age):
    self.name = name 
    self.age = age 
    
    
  
  def bark(self):
    print(f"{self.name} says Woof!")
    
  def is_old(self):
    print(f"{self.name} is {self.age} years old")
    
    

my_dog = Dog('happy', 3)

my_dog.bark()
my_dog.is_old()