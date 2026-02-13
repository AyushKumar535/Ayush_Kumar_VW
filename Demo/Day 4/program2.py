# normal function : def keyword
# Single Responsibility Principles
# DRY : Do not repeat yourself principle

def check(n):
  return n >= 10

def check_even(n):
  return n % 2 == 0

def even_result(num):
  print(f"{num} is even")
  
# print(check(23))

def check_numbers(n):
  num = n
  if(check(num)):
    print(f"{n} is greater than or = to 10")
    # even_result(num)
  else:
    print(f"{num} is less than 10")
    
# check_numbers(2)
    
#--------------------

# lambda function:
isTrue = lambda n : n >= 10
# print(isTrue(55))

def check_nums(n):
  num = n
  if(isTrue(num)):
    print(f"{num} is greater than or = to 10")
  else:
    print(f"{num} is less than 10")
    
# check_nums(22)

# ------------------

def square(num):
  return num**num

num = 2
# print(f"{num} square: {square(num)}")

# lambda
squ = lambda x: x**x
# print(f"{num} square: {squ(num)}")
# print(type(squ))

#---------------------------

add = lambda x,y=0 : x + y

# print(f"Add result: {add(2,5)}")
# print(f"Add result: {add(4)}")

#---------------------------
# function body can be hold using variable names

hi = lambda : print("Hello Hugh Jackman!")
# hi()
# print(hi())

demo = lambda : input('Enter your name: ')

# print(f"You enetered name = {demo()}")

#-----------------------------

nms = lambda *nm : nm
# print(nms('Jim', 'Tim', 'Kim'))

names = lambda **nms : nms.values()
# print(list(names(n1=20, n2 =33, n3 =25)))

#--------------------------------------------

my_func = lambda x,y : (x+y , x-y)

add, sub = my_func(8, 3)
# print(f"Addition : {add}")
# print(f"Sub : {sub}")

# result = my_func(30,8)
# print(result)
# print(f"Addition : {result[0]}")
# print(f"Sub : {result[1]}")

#-----------------------------

