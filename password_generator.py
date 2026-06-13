import secrets
import string

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    
    return ''.join(secrets.choice(chars) for _ in range(length))
while True:
    try:
        length = int(input("Enter password length (minimum 8): "))

        if length < 8:
            print("Password length should be at least 8 characters.")
            continue

        print("Generated Password:", generate_password(length))
        print("Password generated successfully!")
        break

    except ValueError:
        print("Please enter a valid number.")
