def odd_numb(start,end):
    print("Odd numb: ")
    for i in range(start,end +1):
        if i%2 != 0:
            print(i, end=" ")
    print()


def even_numb(start,end):
    print("Even numb: ")
    for i in range(start,end +1):
        if i%2 == 0:
            print(i, end=" ")
    print()


def all_numb(start,end):
    print("All numb: ")
    for i in range(start,end +1):
            print(i, end=" ")
    print()

if __name__ == "__main__":
    start = int(input("Enter starting numb :"))
    end = int(input("Enter ending numb :"))

    odd_numb(start,end)
    even_numb(start,end)
    all_numb(start,end)