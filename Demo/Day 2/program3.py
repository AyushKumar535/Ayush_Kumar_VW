sentence = 'python is a simple language'

print(sentence.capitalize())
print(sentence.count('a'))
print(sentence.endswith('\n'))
print(sentence.startswith('p'))
# print(sentence.index('q'))    #Value Error

print(sentence.find('i'))
if(sentence.find('q') == -1):
    print(f"'q' is not present in {sentence}")

print(sentence.upper())
print(sentence.replace('simple', 'easy'))
print(sentence.title())

word = '  hello  '
wd = "*"
print(f"{wd}{word}{wd}")
print(f"{wd}{word.rsplit()}{wd}")
print(f"{wd}{word.lstrip()}{wd}")
print(f"{wd}{word.strip()}{wd}")


print("{} {} {}".format('python','css','react'))