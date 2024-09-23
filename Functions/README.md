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
  return x * 2

f(3)
>> 6
Now for a lambda function. We'll create it like this:

lambda x: x * 3

As I explained above, the lambda function does not have a return keyword. As a result, it will return the result of the expression on its own. The x in it also serves as a placeholder for the value to be passed into the expression. You can change it to whatever you want.

Now if you want to call a lambda function, you will use an approach known as immediately invoking the function. That looks like this:

(lambda x : x * 2)(3)

>> 6

