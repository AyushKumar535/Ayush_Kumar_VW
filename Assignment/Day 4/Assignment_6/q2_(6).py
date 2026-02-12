def count_frequency(lst):
    frequency = {}
    for num in lst:
        frequency[num] = frequency.get(num, 0) + 1
    return frequency

List1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 6, 2, 4, 2, 5, 23, 6, 4]
print(count_frequency(List1))
