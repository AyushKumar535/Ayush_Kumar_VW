def classify_numbers(numbers):
    result = {'EVEN': [], 'ODD': []}
    for num in numbers:
        if num % 2 == 0:
            result['EVEN'].append(num)
        else:
            result['ODD'].append(num)
    return result

numbers = [8, 1, 10, 5, 64, 9]
print(classify_numbers(numbers))
