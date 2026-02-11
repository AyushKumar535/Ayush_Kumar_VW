marks_dict = {}

for _ in range(3):
    subject = input("Enter subject name: ")
    marks = float(input(f"Enter marks for {subject}: "))
    marks_dict[subject] = marks

print("Marks Dictionary:", marks_dict)
