import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters.")
        return ""

    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all character sets
    all_chars = lowercase + uppercase + digits + symbols

    # Make sure the password includes at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols),
    ]

    # Fill the remaining length of the password
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the list to avoid predictable sequences
    random.shuffle(password)

    # Join the list into a string
    return ''.join(password)

# Get user input
try:
    user_length = int(input("Enter desired password length: "))
    password = generate_password(user_length)
    if password:
        print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number.")

