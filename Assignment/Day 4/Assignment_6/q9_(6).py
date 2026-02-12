def string_menu(text):
    print("Select an option:")
    print("A. Display characters from even position")
    print("B. Display characters from odd position")
    print("C. Display length of a string")
    print("D. Add 'a' at the end of string length times")
    
    choice = input("Enter choice: ").upper()
    
    if choice == 'A':
        print("Characters at even positions:", text[::2])
    elif choice == 'B':
        print("Characters at odd positions:", text[1::2])
    elif choice == 'C':
        print("Length of the string:", len(text))
    elif choice == 'D':
        print("String after adding 'a':", text + 'a' * len(text))
    else:
        print("Invalid choice!")

string_menu("hello")
