import random
import string

def generate_password(length):
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")
    
    all_letters = random.choice(string.ascii_letters)
    all_digits = random.choice(string.digits)
    all_specials = random.choice(string.punctuation)  # Random special character

    remaining_chars = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length - 3))
    password = all_letters + all_digits + all_specials + remaining_chars

    return ''.join(random.sample(password, len(password)))  # Shuffle for randomness

try:
    length = int(input("Enter the desired password length: "))
    password = generate_password(length)
    print("Generated Password:", password)
except ValueError as e:
    print(f"Error: {e}")
