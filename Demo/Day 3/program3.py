def function1(name = None,age = None):
  print(f"name is {name} and age is {age}")
 
# call based on positional argument sequence.  
# function1('Tom',48)
# you can not change sequence of the arguments: it may show incorrect results.
# function1(48,'Tom')

# keyword argument 
# function1(name='Tom',age=49)
# function1(age=49, name='Tom')

# function1()
# function1(age= 55)

def function2(salary, name='Jim'):
  print(f"{name}'s salary is {salary}")
  
 # combine positional args , keywords args
# function2('Tom',salary=50000)
# function2(45000, name='Tim')




