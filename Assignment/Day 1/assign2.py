import assign1

start = int(input("Enter starting numb:"))
end = int(input("Enter ending numb:"))

while True:
    print("Choice to print numbs:")
    print("1.Odd Numbers")
    print("2.Even Numbers")
    print("3.All Numbers")
    print("4.Exit")

    choice = int(input("Enter ur choice:"))

    if choice == 1:
        assign1.odd_numb(start, end)
    elif choice ==2:
        assign1.even_numb(start,end)
    elif choice == 3:
        assign1.all_numb(start,end)
    elif choice ==4:
        print("Program exist")
        break
    else:
        print("Invalid Choice")