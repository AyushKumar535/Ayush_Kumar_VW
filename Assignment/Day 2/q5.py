def maximum(a,b,c):
    if a>=b and a >= c:
        return a
    elif b>= a and b >= c:
        return b
    else:
        return c

x = int(input("Enter a first numb :"))
y = int(input("Enter a second numb :"))
z = int(input("Enter a third numb :"))

print("Maximum number is :=",maximum(x,y,z))