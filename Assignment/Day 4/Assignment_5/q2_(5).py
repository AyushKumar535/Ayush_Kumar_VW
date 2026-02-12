def fizz_buzz_while(start, end):
    num = start
    while num <= end:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz!")
        elif num % 3 == 0:
            print("Fizz!")
        elif num % 5 == 0:
            print("Buzz!")
        else:
            print(num)
        num += 1

start_number = int(input("Enter the starting number: "))
end_number = int(input("Enter the ending number: "))
fizz_buzz_while(start_number, end_number)
