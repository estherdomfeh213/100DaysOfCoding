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
    
# get_price(): Returns the price of the product.
  def get_price(self):
    return f"{self._name} is ${self._price}, {self._stock} available"
  
# add_stock(amount): Increases the stock by a specified amount.
  def add_stock(self, amount):
    self._stock += amount
    return f"Available stock: {self._stock}"
    
# sell(amount): Reduces the stock by the specified amount (but only if enough stock is available).
  def sell(self, amount):
    if amount > self._stock:
      return "Not Enough Stocks"
    else:
      self._stock -= amount
      return f"Current stock: {self._stock}"
      

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