# function parameters: optional / default parameters

def greet(name,message='no message'):
  print(F"Hello, {name}! Mesaage: {message}")
  
# greet('Hugh Jackman',"I loved that new movie!")
# greet() # TypeError: greet() missing 1 required positional argument: 'name'

# greet('Mugdha') #TypeError: greet() missing 1 required positional argument: 'message'
# greet('Mugdha') # issue resolved by default parameter

def function1(a= 1,b= 'abc',c= True):
  print(f"a is : {a}, type: {type(a)}")
  print(f"b is : {b}, type: {type(b)}")
  print(f"c is : {c}, type: {type(c)}")
  
# function1(100, 'Hugh Jackman', False)
# function1(100, 'Hugh Jackman')
# function1(100)
# function1()
# function1(23.33, True, 'Bob') # argument values have highest prefernces, than default arguments




  
  