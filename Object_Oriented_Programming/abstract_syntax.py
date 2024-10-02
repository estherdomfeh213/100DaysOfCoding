from abc import ABC, abstractmethod

# 1. Define an abstract class
class AbstractClassName(ABC):  # Inherit from ABC (Abstract Base Class)
    
    # 2. Define abstract methods
    @abstractmethod
    def abstract_method(self):
        pass  # No implementation here, just a placeholder

    # 3. Optionally, you can define regular methods with implementation
    def regular_method(self):
        print("This is a regular method with implementation.")

# 4. Define a subclass that inherits from the abstract class
class ConcreteClass(AbstractClassNam
    # 5. Implement the abstract methods from the abstract class
    def abstract_method(self):
        print("Implementation of the abstract method in ConcreteClass.")

# 6. Create an object of the ConcreteClass and use its methods
obj = ConcreteClass()
obj.abstract_method()  # Calls the implemented abstract method
obj.regular_method()   # Calls the regular method inherited from the abstract class
