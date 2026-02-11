people = {'Arham': 'Blue', 'Lisa': 'Yellow', 'Vinod': 'Purple', 'Jenny': 'Pink'}

print("A) Number of students:", len(people))

people['Lisa'] = 'Green'
print("B) Updated Lisa's colour:", people['Lisa'])

people.pop('Jenny')
print("C) After removing Jenny:", people)

print("D) Sorted dictionary:")
for key in sorted(people):
    print(key, ":", people[key])