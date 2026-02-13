def parent():
    print('Hello from parent')
    def child():
        print('Hi from child')
    child()
    
# parent()

#--------------

def outer(num1, num2):
    def inner(n1, n2):
        return n1 + n2
    addresult = inner(num1,num2)
    return addresult
    
# print(outer(8,3))  

def outer1():
    def inner1(n1,n2):
        return n1 + n2
    return inner1

add = outer1()

# print(type(add))
# print(f"Add: {add(8,4)}")        
        
def outer2():
    return lambda n1,n2: n1 + n2

num1 = 22
num2 = 7
inner_func = outer2()
# inner_func = lambda n1,n2: n1 + n2
# print(f"Add: {inner_func(num1, num2)}")