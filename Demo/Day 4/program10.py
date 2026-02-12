# Closuers in Python
def parent():
    print("Hi from parent function")
    x = 11
    def child(x):
      x = x +1 
      print("Hi from child function")
    return child

inner = parent()
inner()
print('How are you!')