# Practice Question 2: Product Inventory with Encapsulation
# Create a class Product with:
class Product:
  
# Private attributes: name, price, and stock
# Public methods:
# __init__: Initializes the product name, price, and stock quantity.
  def __init__(self, name, price=0, stock=0):
    self._name = name 
    self._price = price
    self._stock = stock
    
# Returns the price of the product.
  def get_price(self):
    return f"Price of {self._name}: ${self._price:.2f}" # The price is now formatted to 2 decimal places using .2f to make it look more like real-world pricing.
  
  # Returns the stocks available 
  def get_stock(self):
    return f"Stock for {self._name}: {self._stock} units"
  
# Increases the stock by a specified amount.
  def add_stock(self, amount):
    self._stock += amount
    return f"New stock for {self._name}: {self._stock} units"
    
# Reduces the stock by the specified amount (but only if enough stock is available).
  def sell(self, amount):
    if amount > self._stock:
      return "Not enough stocks to sell!"
    else:
      self._stock -= amount
      return f"Sold {amount} units of {self._name}. Remaining stock: {self._stock} units"
      

# Create two products and perform the following actions:
product1 = Product('soap', 20, 2)
product2 = Product('coffee', 90, 6)

# Display their price and stock.
print(product1.get_price())
print(product2.get_price())
# Add stock to one product and sell some units of the other.
print(product1.add_stock(2))
print(product2.sell(2))
# Print the remaining stock after each operation.
print(product1.get_stock())