# I have converted decor function as per Closure rules:
def decor(func):
  def inner():
    func() # existing functionality
    # Add new functionality
    print("Please feel comfortable and enjoy Python learning!!")
  return inner

@decor
def greet():
  print("Hello !!")
  print("Wel-come all!")
  
# greet()
# inner = decor(greet)
# inner()

# greet = decor(greet)
# greet()
  
  
