Understanding Function in Python

This is an introduction to functions, a fundamental building block in Python programming.

- Functions help organize code, improve readability and promote re-useability of codes.

Functions are reuseable block of codes that perform specific tasks only when called.

- Two steps in functions

1. define the function
2. call function (invoke function)

- To create a function, use the keyword 'def' followed by the name you want to give the function.
- Basic syntax
  def function_name(parameter):
  function
  return expression

Lambda Functions
Python supports lambda functions, which are used fr writing simple, one-line expressions.

- Lambda functions are similar to user-defined functions but without a name. They're commonly referred to as anonymous functions.
- Lambda functions are efficient whenever you want to create a function that will only contain simple expressions – that is, expressions that are usually a single line of a statement.
- They are also useful when you want to use the function once.

You can define a lambda function like this:

lambda argument(s) : expression

1. lambda is a keyword in Python for defining the anonymous function.
   argument(s) is a placeholder, that is a variable that will be used to hold the value you want to pass into the
2. function expression. A lambda function can have multiple variables depending on what you want to achieve.
3. expression is the code you want to execute in the lambda function.

Notice that the anonymous function does not have a return keyword. This is because the anonymous function will automatically return the result of the expression in the function once it is executed.

Assume I want to write a function that returns twice the number I pass it. We can define a user-defined function as follows:

def f(x):
return x \* 2

f(3)

> > 6
> > Now for a lambda function. We'll create it like this:

lambda x: x \* 3

As I explained above, the lambda function does not have a return keyword. As a result, it will return the result of the expression on its own. The x in it also serves as a placeholder for the value to be passed into the expression. You can change it to whatever you want.

Now if you want to call a lambda function, you will use an approach known as immediately invoking the function. That looks like this:

(lambda x : x \* 2)(3)

> > 6

Parameters
Function parameters are variables defined in the function's declaration.

- Types of Parameters
  1.  Positional Parameters: Parameters passed based on their position in the function call.
  2.  Keyword Parameters: Parameters passed with their corresponding variable names.
  3.  Default Parameters: Parameters with predefined default values.
  4.  Variable-length Parameters: Parameters that can accept a variable number of arguments.

example:
def calculate_area(length,width):
area = length \* width
return area

Arguments
In Python, arguments refer to the values passed to a function or a script when it is called or executed.
These values provide necessary inputs or configurations that the function or script needs to operate correctly.

- There are generally two types of arguments in Python:

Positional Arguments:

These are arguments passed to a function or script in a specific order. The position of the argument determines which parameter it corresponds to in the function definition.
Example:
def greet(name, greeting):
print(f"{greeting}, {name}!")

greet("Alice", "Hello")
In this example, "Alice" is passed as the name argument and "Hello" as the greeting argument. The order matters; swapping them would change the output.
Keyword Arguments:

These are arguments identified by their parameter names when passed to a function or script. They allow you to specify which parameter each argument corresponds to, regardless of the order.
Example:
def greet(name, greeting):
print(f"{greeting}, {name}!")

greet(greeting="Hello", name="Bob")
Here, "Hello" is passed as the greeting argument and "Bob" as the name argument. The order of arguments does not affect the outcome because they are explicitly named.
Arguments in Python functions can also have default values, making them optional when the function is called. This flexibility allows functions to handle various scenarios without needing all arguments to be provided each time they are called.


Local VS Global Scope 
- Local Scope
  A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
  ExampleGet your own Python Server
A variable created inside a function is available inside that function:

def myfunc():
  x = 300
  print(x)

myfunc()