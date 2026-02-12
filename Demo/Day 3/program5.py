# def additon(n1,n2,n3=0):
#   sum = 0
#   sum = n1+ n2
#   return sum

# print(additon(10,20))
# print(additon(10,20,30))

# *args : variable length positional argument
#demo:
def addition(*nums):
  print(type(nums))
  sum = 0
  for n in nums:
    sum += n
  return sum

# print(addition(1,2,3))
# print(addition(1,2,3,4))
# print(addition(1,2,3,5))

# demo:
def greet_players(*names):
    for name in names:
      print(f"Hello, {name}")
      
      
# greet_players('Tim', 'Peter', 'John')
# greet_players('Tim', 'Peter', 'John','Ted')
# greet_players('Tim', 'Peter', 'John','Ted', 'Walter')


# Keyword variable length arguments: **kwargs
#demo:

def my_sum(**nums):
  addition = sum(nums.values())
  # print(type(nums))
  return addition


# print(my_sum(n1=10,n2=20))
# print(my_sum(n1=10,n2=20,n3=30))
# print(my_sum(n1=10,n2=20,n3=30,n4=40))


# ------------------------------

def personal_info(**info):
  for key,value in info.items():
    print(f"The key {key} has a value {value}")
    
# personal_info(fnm= 'Tim', lnm= 'Burton', moviesinfo="Gothic Horror & Dark Fantancy Films")


#-----------------------------------------

# mixing *args, **kwargs:

def example(*args,**kwargs):
  print(f"Positional arguments: {args}")
  print(f"Keyword arguments: {kwargs}")
  
  
example(11,'sometext',33, name='Tim', salary = 55000.50, isActive=True)
  