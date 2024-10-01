class BankAccount:
  
  def __init__(self, account_holder, balance=0):
    self.account_holder = account_holder   # Public attribute 
    self._balance = balance                 # Private attribute 
    
    
  def deposit(self, amount):
    self._balance += amount
    print(f"{amount} deposited. New balance: {self._balance}")
    
    
  def withdraw(self, amount):
    if amount > self._balance:
      print("Insufficient balance")
    else:
      self._balance -= amount 
      print(f"{amount} withdrawn. New balance: {self._balance}")
      
      # ? This is the method to get the balance 
  def get_balance(self): #* Public method to access the private balance 
    return self._balance  # *Safely returns the private balance 
  def display(self):
    print(f"Account_holder: {self.account_holder}, Current balance: {self._balance}")
    
    
    
account1 = BankAccount('Esther', 0)

account1.display()
print(account1._balance) # !Although you can access it, it's is a bad practice 
print(account1.get_balance()) #* Correct way to access private attributes is through public methods 

account1.withdraw(20)
account1.deposit(200)
account1.display()