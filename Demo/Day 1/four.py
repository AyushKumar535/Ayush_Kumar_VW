data = [10,20,30,40,50]

# for ele in data:
#     print(ele)

# print(dir(data))

# x=data.__iter__()
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

# iter_object = iter(data)
# for item in iter_object:
#     print(item)
# print(next(iter_object))
# print(next(iter_object))
# print(next(iter_object))
# print(next(iter_object))
# print(next(iter_object))


def my_for_loop(iterable):
    iterator = iter(iterable)
    try:
        while True:
            print(next(iterator))
    except StopIteration:
        pass

my_for_loop(data)

