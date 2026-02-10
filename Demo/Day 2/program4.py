#List : indexed collection, [], nested lists

# numbers = []

# numbers.append(1)
# numbers.append(2)
# numbers.append(3)
# print(numbers , type(numbers))
# print(numbers[1])
# print(len(numbers))

# ===============================================

# position = [1,2,3,[4,5,6]]
# print(position,len(position))
# print(position[3])
# print(position[3][1])
# print(position[-4])
# print(position[-1][-1])


# ==================================================
#  slicing:

# numbers = [1,2,3,4,5,6,7,8,9,10]
# print(numbers[2:6])
# print(numbers[:6])
# print(numbers[6:])
# print(numbers[0:6:2])
# print(numbers[1:6:2])


# =========================================

# greeting = ['hello','hi','hey']
# greeting.reverse()
# print(greeting)

# shopping_list = ['bread','apple','milk']
# print(shopping_list)

# shopping_list.sort()
# print(shopping_list)

# shopping_list.sort(reverse=True)
# print(shopping_list)

# new_shopping_list = sorted(shopping_list,reverse=True)
# print(new_shopping_list)


# ===========================================================

lst = ['a','b','c','d']
lst1 = ['j','k']
print(lst)
print(lst1)

lst += lst1
print(lst)

# lst -= lst1  #TypeError
# print(lst1)

print(len(lst))
lst[4] = 'm'
print(lst)