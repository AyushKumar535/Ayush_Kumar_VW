# print("modone: The value of __name__ is {} .format(__name__)")

# __x__=100          #Custom Attribute

# #Custom Function
# def display():
#     print("Hugh Jackman!!")

# display()

# # print(__name__)
# print(dir())


#===============================================

print("modone: The value of __name__ is {}".format(__name__))

def task1():
    print("Doing task 1")
def task2():
    print("Doing task 2")
def task3():
    print("Doing task 3")

if __name__ == "__main__":
    task1()
    task2()
    task3()