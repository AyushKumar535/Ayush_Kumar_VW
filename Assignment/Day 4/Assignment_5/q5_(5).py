import string
import random

def captcha_functionality():
    characters = string.ascii_letters + string.digits
    captcha = ''.join(random.choice(characters) for _ in range(6))
    
    print(f"Captcha: {captcha}")
    user_input = input("Please enter the captcha: ")
    
    if user_input == captcha:
        print("Captcha verified successfully!")
    else:
        print("Captcha incorrect. Please try again.")

captcha_functionality()
