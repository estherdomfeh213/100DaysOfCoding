from abc import ABC, abstractmethod 


# Abstract class 
class Payment(ABC):
  # Abstract method for processing payment, subclasses must implement this method
  @abstractmethod
  def process_payment(self, amount):
    pass # No implementation here, it's a placeholder for the subclasses
  
  @abstractmethod
  def refund(self, amount):
    pass 
  
  
# Concrete class for Credit Card payment 
class CreditCardPayment(Payment):
  def process_payment(self, amount):
    return f"Processing credit card payment of ${amount}"
  
  def refund(self, amount):
    return f"Refunding ${amount} to credit card"
  
  
# Concrete class for PayPal payment 
class PayPalPayment(Payment):
  def  process_payment(self, amount):
    return f"Processing PayPal payment of ${amount}"
  
  def refund(self, amount):
    return f"Refunding ${amount} to paypal"
  
# Concrete class for Bank Transfer payment
class BankTransferPayment(Payment):
  def process_payment(self, amount):
    return f"Processing bank transfer of ${amount}"
  
  def refund(self, amount):
    return f"Refunding ${amount} via bank transfer"
  
 # Concrete class for cryptocurrency 
class Cryptocurrency(Payment):
  def process_payment(self, amount):
    return f"Processing cryptocurrency of ${amount}"
  
  def refund(self, amount):
    return f"Refunding ${amount} to cryptocurrency"
  
# Usage 
def make_payment(payment_method, amount):
  print(payment_method.process_payment(amount))
  print(payment_method.refund(amount))


# Creating object of different  payment types 
credit_payment = CreditCardPayment()
paypal_payment = PayPalPayment()
bank_payment = BankTransferPayment()
crypto_payment = Cryptocurrency()

#process a credit card payment 
make_payment(credit_payment, 100)

# Process a Paypal payment 
make_payment(paypal_payment, 150)

# Process a bank transfer 
make_payment(bank_payment, 200)

# Process a cryptocurrency payment
make_payment(crypto_payment, 3400)



#! Abstraction: The Payment class hides the details of the of how the payments are processed and refunded. it only provides a general interfaces that subclasses must follow.

#! Concrete Implementation: Each specific payment method(credit card, Paypal, bank transfer) providers its own implementation of process_payment and refund()