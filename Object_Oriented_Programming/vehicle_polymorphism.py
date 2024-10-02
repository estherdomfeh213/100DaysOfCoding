# Base class
class Vehicle:
    def start_engine(self):
        return "The vehicle's engine is starting."

# Subclass 1
class Car(Vehicle):
    def start_engine(self):
        return "The car's engine is starting with a roar."

# Subclass 2
class Truck(Vehicle):
    def start_engine(self):
        return "The truck's engine is starting with a heavy rumble."

# Subclass 3
class Bicycle(Vehicle):
    def start_engine(self):
        return "Bicycles don't have engines, but we're ready to ride!"

# Function to demonstrate polymorphism
def start_vehicle_engine(vehicle):
    print(vehicle.start_engine())

# Instantiate objects of different types
my_car = Car()
my_truck = Truck()
my_bicycle = Bicycle()

# Demonstrating polymorphism
start_vehicle_engine(my_car)     # Calls Car's start_engine
start_vehicle_engine(my_truck)   # Calls Truck's start_engine
start_vehicle_engine(my_bicycle) # Calls Bicycle's start_engine
