names = ['Frodo', 'Sam', 'Golum', 'Gandalf']

# print(sorted(names,key=len))

# sorted_names = sorted(names)
# for name in sorted_names:
#   print(len(name))

# print(sorted(names))

# for name in names:
  # print(len(name))

#---------------------------------------

players = ['Sachin Tendulkar', 'Virat Kohli', 'Rohit Sharma', 'Suresh Raina']

def function1(nm):
  player = nm.split() # whitespace
  return  player[0]

# print(sorted(players, key= lambda nm: nm.split()[1]))

# print(sorted(players,key=function1))

# for nm in players:
#   function1(nm)

#------------------------

# print((lambda x: x * 2)(4))

#------------------------

num = -2
if((lambda x: x > 0)(num)):
  print(f'{num} is greater than 0')
else:
  print(f'{num} is less than 0')



  
