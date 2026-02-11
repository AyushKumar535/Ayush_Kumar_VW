def overlapping(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

print("Overlap result:", overlapping([1, 2, 3], [4, 5, 3]))
print("Overlap result:", overlapping([1, 2, 3], [4, 5, 6]))