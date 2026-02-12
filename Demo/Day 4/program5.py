result = (lambda a,b : a+b)(3,2)
# print(f'Add :{result}')

# result1 = (lambda a : a * 2)(int(input('Eneter a number: ')))
# print(f'double :{result1}')

# result2 = (lambda nm: f"Mr./Mrs. {nm}")(input('Enter your name: '))
# print(f"Wel-come {result2}")

#-------------------------

num1 = 10
num2 = 20

# if(num1 >= num2):
#   print(num1)
# else:
#   print(num2)

result4 = num1 if num1>=num2 else num2
# print(result4)
# print(num1 if num1>=num2 else num2)

#--------------------------------------

print((lambda num1, num2 : num1 if num1>=num2 else num2)(num1, num2))

