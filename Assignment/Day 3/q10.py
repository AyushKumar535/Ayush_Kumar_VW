tup = tuple(input("Enter tuple elements separated by space: ").split())
value = input("Enter value to find: ")

count = tup.count(value)
if count > 1:
    print(f"{value} is repeated {count} times")
else:
    print(f"{value} is not repeated")