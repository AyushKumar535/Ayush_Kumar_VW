def subtract(list1, list2):
    return [element for element in list1 if element not in list2]

list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]
print(subtract(list1, list2))  
