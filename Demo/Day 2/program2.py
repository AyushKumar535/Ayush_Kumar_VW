# Sequence of characters and strings are immutable
# Index start with "0" ...also support "-ve" indexing.

# -5,-4,-3,-2,-1 :- "-ve" indexing
# str = "Hello"
# print(str[0])
# print(len(str))
# print(str[-5])
# print(str[-6])  #Index Error


# ============================================================

sentence = "Lets learn Python"
# for ch in sentence:
#     print(ch)

# String Slicing :
s1 = sentence[0:4]
print(s1)

print(sentence)

s2 = sentence[4:]
print(s2)

s3 = sentence[:9]
print(s3)


#  -ve Indexing
s4 = sentence[:-9]
print(s4)


# Membership Operators
word = 'Python'
print('h' in word)
print('a' in word)

ch = 'a'
if (ch in word):
    print(f"{ch} is present in word: {word}")
else:
    print(f"{ch} is not present in word: {word}")


# for ch in word:
#     if(ch == 'h'):
#         print(f"{ch} is present in word: {word}")
#     else:
#          print(f"{ch} is not present in word: {word}")