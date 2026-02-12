import random
import string

def generate_password(length=12):
    if length < 8:
        print("Password length should be at least 8 characters.")
        return
    
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    while not (any(c.islower() for c in password) and 
               any(c.isupper() for c in password) and 
               any(c.isdigit() for c in password) and 
               any(c in string.punctuation for c in password)):
        password = ''.join(random.choice(all_characters) for _ in range(length))
    
    print(f"Generated Password: {password}")

password_length = int(input("Enter desired password length (8-12): "))
generate_password(password_length)
