# global / modular level namespece : x, name, result, demo, outer

x = 10
name = "Hugh Jackman"
result = lambda x: x* 2

# print(dir())

def demo():
  # Local namespace : belongs to function scope
   x = 55
   str = 'Sample Text'
   print(dir()) #['str', 'x']
   
# demo()

# print(dir())

def outer():
  # local scope
  isActive = False
  print('outer',dir()) # ['isActive']
  def inner():
    # Enclosed scope
    num = 22
    print('inner',dir()) # ['num']
  print('outer',dir()) # ['isActive','inner']
  inner()
  
outer()