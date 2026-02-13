# mixing of *args and **kwargs :

def function1(*names,**nums):
  print(f"{type(names)} {names}")
  print(f"{type(nums)} {nums.values()}")
  
  
# function1('Tim', 'Sam', 'Tom', n1=23.44, n2 = 55, n3 = 10, n4 =5)
  
# demo = function1
# demo('Tim', 'Sam', 'Tom', n1=23.44, n2 = 55, n3 = 10, n4 =5)

# Tag :x = Value: 10
# Tag : y = x = 10