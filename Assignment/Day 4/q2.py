def union(list1, list2):
    return list(set(list1) | set(list2))

list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]
print(union(list1, list2))  
