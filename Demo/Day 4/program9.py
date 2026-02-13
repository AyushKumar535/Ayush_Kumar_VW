# x = 555 # module level / global scope

# def function1():
#   num = 10 # local scope
  
  
# def function2():
#   num = 22 # local scope
  
##---------------

# Enclosed namespace:
def outer():
  # Local scope
  p = 10
  q = 2
  print(dir()) # ['p', 'q']
  def inner1():
    # Enclosed scope
    x = 22
    y = 53
    print(f"{p}") 
    print(dir()) # ['x', 'y']
  def inner2():
    # Enclosed scope
    m = 22
    n = 53
    print(dir()) # ['m', 'n']
  
  # print(f"{y}") #NameError: name 'y' is not defined
  print(dir()) # ['p', 'q',' inner1','inner2']
  inner1()
  inner2()
  
# outer()

# -----------------------

x = 100 # global

def outer():
  global x
  x = x + 10 # UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
  print(x) #110
  x = 20
  print(x) # 20

# print(x) # 100

# outer()

#--------------------

y = 22 # global scope
def outer1():
  y = 88 # local scope
  def inner():
    # Enclosed scope
    nonlocal y
    y = y + 100 
    print(y)# UnboundLocalError 
    y = 55
    print(y)
  inner()
  
# outer1()
    