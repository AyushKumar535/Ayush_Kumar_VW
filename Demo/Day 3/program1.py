# we are violating DRY Principle over here..
# Single Responsibilty Principle
# no = 10

# mult = no * 2
# print(mult)

# # // code 100lines of code

# mult = no * 2
# print(mult)

# -----------------------------------

def greet(name):
  '''This function ask user name and greet user as 'Hello, How are you '_NameHere' '''
  print(f'Hello, How are you {name} !')

# greet('Mugdha')
# greet('Hugh Jackman')

# print(greet.__doc__)

# -----------------------------------

## Non- parameterized functions
def function1():
  print("Hello World!")
  
# function1()

def function2():
  message = input("Enter message: ")
  print(f"You have a new message: {message}")
  
# function2()



# Parameterized functions
def function3(parameter):
  pass

def function4(parameter1, parameter2):
  pass


# Demo:

sales = 7000

def rating(sales):
  if(sales >= 10000):
    print('Gold Status')
  elif(sales >= 5000):
    print('Silver Status')
  elif(sales >= 1000):
    print('Bronze Status')
  else:
    print('Keep selling!!!')

# rating(sales)

# Demo: 

def request_age():
  age = ' '
  while age.isdigit() == False:
    age = input('Enter your age: ')
    if(age.isdigit() == False):
      print('Please enter digits only')
  return int(age)

# your_age = request_age()
# print(your_age)

