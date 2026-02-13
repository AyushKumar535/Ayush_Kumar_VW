def function1(expenses={},day="Today"):
  total_expenses = sum(expenses.values())   
  print(f"Day {day} total expenses are : {total_expenses}")
  
  
daily_expense = {'breakfast': 150, 'autoforffice': 60, 'shopping': 2000, 'autoforhome': 40}

# function1(daily_expense,'Wed')
# function1(daily_expense)
# function1()

# ----------------------

def display(name='Tim',age=0):
  return name,age

# print(type(display()))
# print(display.__defaults__)

# print(display('Tom', 55))
# print(display.__defaults__)

# print(print.__doc__)

#-----------------------------------

# def add_names(name, emp_data=[]): # Peter, Olivia
#   emp_data.append(name)
#   print(f"All employee names: {emp_data}")

def add_names(names, emp_data=None):
  if emp_data is None:
    emp_data = []
  emp_data.append(names)
  print(f"All employee names: {emp_data}")
 
names = ['Peter', 'Olivia', 'Walter', 'Jean']  

# add_names(names)
# print(add_names.__defaults__)

# add_names('Olivia')
# print(add_names.__defaults__)

# add_names('Walter')
# print(add_names.__defaults__)

# add_names('Jean')
# print(add_names.__defaults__)