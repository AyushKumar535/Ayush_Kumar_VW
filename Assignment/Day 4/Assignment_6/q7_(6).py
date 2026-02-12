def convert_to_strings(lst, tpl):
    return list(map(str, lst)), list(map(str, tpl))

lst = [1, 2, 3]
tpl = (4, 5, 6)
list_str, tuple_str = convert_to_strings(lst, tpl)
print(list_str)
print(tuple_str)
