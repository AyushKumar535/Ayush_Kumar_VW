value = int(input("Enter a numb :"))

a = value // 1000
b = (value //100) % 10
c = (value //10) % 10
d = value % 10


print("Face Value :", a, b, c, d)

print("Place values :")
print(value, "=", a*1000, "+", b*100, "+", c*10, "+", d)

reverse = d*1000 + c*100 + b*10 + a
print("Reverse a Numb :", reverse)