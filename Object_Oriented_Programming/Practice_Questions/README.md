Here are some practice questions to help you solidify your understanding of Encapsulation and OOP principles in Python:

!Practice Question 1: Employee Class with Encapsulation
Create a class Employee with the following:
Private attributes: name and salary
Public methods:
**init**: Initializes the name and salary.
get_name(): Returns the employee's name.
get_salary(): Returns the employee's salary.
set_salary(new_salary): Updates the employee's salary (but only if the new salary is higher than the old one).
Create an instance of the Employee class, and:
Display the employee’s name and salary.
Try to change the salary with the set_salary() method and print the updated salary.

! Practice Question 2: Product Inventory with Encapsulation
Create a class Product with:

Private attributes: name, price, and stock
Public methods:
**init**: Initializes the product name, price, and stock quantity.
get_price(): Returns the price of the product.
add_stock(amount): Increases the stock by a specified amount.
sell(amount): Reduces the stock by the specified amount (but only if enough stock is available).
Create two products and perform the following actions:

Display their price and stock.
Add stock to one product and sell some units of the other.
Print the remaining stock after each operation.
Practice Question 3: Bank Account with Limits
Update the BankAccount class with the following:
Private attribute withdraw_limit which represents the maximum amount that can be withdrawn at once.
A new method set_withdraw_limit(new_limit) that allows changing the withdrawal limit.
Modify the withdraw() method so that it checks both the balance and the withdrawal limit before allowing the withdrawal.
Create an account and test:
Setting a withdrawal limit.
Trying to withdraw an amount greater than the limit.
Making valid deposits and withdrawals, and printing the final balance.
Practice Question 4: Student Grades System
Create a class Student with:

Private attributes: name, grades (a list of grades).
Public methods:
**init**: Initializes the student's name and an empty list for grades.
add_grade(grade): Adds a grade to the list (only if it’s between 0 and 100).
calculate_average(): Returns the average of the student’s grades.
Create a few students and:

Add some grades for each student.
Print their average grade.
Challenge Question: Shopping Cart System
Create a class ShoppingCart with:

Private attribute items (a dictionary where the key is the item name, and the value is the quantity).
Public methods:
**init**: Initializes an empty cart.
add_item(item, quantity): Adds the item and its quantity to the cart (or updates the quantity if the item already exists).
remove_item(item): Removes the item from the cart.
view_cart(): Prints all items in the cart and their quantities.
Create a shopping cart object and:

Add some items.
Remove an item.
View the final contents of the cart.
