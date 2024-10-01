class BanAccount:
  
  def __init__(self, account_holder, balance):
    self.account_holder = account_holder
    self.balance = balance
    
    
  def deposit(self, amount):
    self.balance += amount
    print(f"{amount} was deposited into your account. New balance: {self.balance}")
     
  def withdraw(self, amount):
    if amount > self.balance:
      print("Insufficient balance")
    else: 
      self.balance -= amount
      print(f"{amount} was withdrawn. New balance: {self.balance}" )
    
  def display(self):
    print(f"Account holder: {self.account_holder}, Current balance: {self.balance}")
    


account_user1 = BanAccount("Domfeh Esther", 300)
account_user2 = BanAccount("Nathan", 800)

account_user1.display()
account_user1.deposit(200)
account_user1.withdraw(300)

account_user2.display()



