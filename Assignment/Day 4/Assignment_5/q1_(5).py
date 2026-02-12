def fizz_buzz_for(start, end):
    for num in range(start, end + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz!")
        elif num % 3 == 0:
            print("Fizz!")
        elif num % 5 == 0:
            print("Buzz!")
        else:
            print(num)

start_number = int(input("Enter the starting number: "))
end_number = int(input("Enter the ending number: "))
fizz_buzz_for(start_number, end_number)
