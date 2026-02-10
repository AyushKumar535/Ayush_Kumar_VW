m1 = int(input("Enter a marks of Subject 1"))
m2 = int(input("Enter a marks of Subject 2"))
m3 = int(input("Enter a marks of Subject 3"))

average = (m1 + m2 + m3) /3
print("Average =", average)

if average >=90:
    print("Grade A")
elif average >=80:
    print("Grade B")
elif average >=70:
    print("Grade C")
elif average >=60:
    print("Grade D")
else:
    print("Grade F")