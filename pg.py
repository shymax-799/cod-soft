import random
import string
def generate_password(length=12):

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    character_pool = lowercase + uppercase + digits + special_characters


    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]
    password += random.choices(character_pool, k=length - len(password))
    random.shuffle(password)
    return ''.join(password)
def get_user_input():
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length < 8: 
                print("Password length should be at least 8 characters for security reasons.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer for the password length.")
    return length
def main():
    print("Welcome to the Password Generator!")
    length = get_user_input()
    password = generate_password(length)
    print("\nGenerated Password:", password)

