count = 0 # Global scope 

def increment():
  count += 1 # This refers to the local count within the function 
  
  increment()
print(count)

#! To fix this

def increment_global():
  global count #? if you use the global keyword, the variable belongs to the local scope
  count += 1 # This refers to the local count within the function 
  
increment_global()
print(count)



