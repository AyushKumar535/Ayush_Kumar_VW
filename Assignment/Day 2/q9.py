Year = int(input("Enter a year :"))

if(Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
    print(Year, "is a leap year")
else:
    print(Year,"it is not a leap year")