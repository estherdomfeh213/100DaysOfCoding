# Parent class (Base class)

class Vehicle:
  def __init__(self, make, model, year):
    self.make = make 
    self.model = model 
    self.year = year 
    
  def start_engine(self):
    return f"The engine of {self.year} {self.make} {self.model} is starting. "
  
  def stop_engine(self):
     return f"The engine of {self.year} {self.make} {self.model} is stopping."
   
   
# Child class (Derived class)
class Car(Vehicle):
  def __init__(self, make, model, year, num_doors):
    # Inherit from the Vehicle class 
    super().__init__(make, model, year) # Call the parent class's constructor
    self.num_doors = num_doors
    
  def honk(self):
    return "Car is honking: Beep beep!"
  
  
# Another child class (Derived class)
class Truck(Vehicle):
  def __init__(self, make, model, year, payload_capacity):
    super().__init__(make, model, year)
    self.payload_capacity = payload_capacity # Truck-specific attribute 
    
  def load_cargo(self, weight):
    if weight <= self.payload_capacity:
      return f"Loaded {weight} tons of cargo into truck."
    else:
      return "Exceeds payload capacity"
    
# Another child class (Derived class)
class Bicycle(Vehicle):
  
  def __init__(self, make, model, year, has_basket):
    super().__init__(make, model, year)
    self.has_basket = has_basket  # attribute specific to class bicycle 
    
  def ring_bell(self):
    return f"Bicycle bell rings: Ring ring!"
  
  def check_basket(self):
    if self.has_basket:
      return f"The bicycle has a basket."
    else:
      return f"The bicycle does not have a basket"
    
    
# Usage of inheritance:
# Create instances of Car and Truck
my_car = Car('Toyota', 'Corolla', 2020, 4)
my_truck = Truck('Ford', 'F-150', 2022, 5)
my_bicycle = Bicycle('Two-wheel', 'Scooter', 2013, False)

# Call methods from the base class 
print(my_car.start_engine())
print(my_truck.start_engine())
print(my_bicycle.start_engine())


# Call child-specific methods
print(my_car.honk())
print(my_truck.load_cargo(3))
print(my_bicycle.ring_bell())
print(my_bicycle.check_basket())
print(my_bicycle.check_basket())
      