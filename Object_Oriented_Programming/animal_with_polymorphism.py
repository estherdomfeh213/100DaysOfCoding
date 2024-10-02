# base class 
class Animal:
  def make_sound(self):
    pass 
  
# derived class 
class Dog(Animal):
  def make_sound(self):
    return "Bark!"
  
class Cat(Animal):
  def make_sound(self):
    return "Meow!"
  
class Bird(Animal):
  def make_sound(self):
    return "Chirp!"
  
# Function to demonstrate polymorphism 
def animal_sound(animal):
  print(animal.make_sound())
  
# Using polymorphism  
dog = Dog()
cat = Cat()
bird = Bird()

animal_sound(dog)
animal_sound(cat)
animal_sound(bird)