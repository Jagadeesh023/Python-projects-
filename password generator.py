import random
import string

def generate_password(length):
    """
    Generates a secure random password.
    
    :param length: Length of the password
    :return: Generated password
    """
    if length < 4:
        raise ValueError("Password length should be at least 4 for a secure password.")

    # Define character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Ensure the password has at least one of each type of character
    all_characters = lowercase + uppercase + digits + special_chars
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars),
    ]

    # Fill the rest of the password length with random choices
    password += random.choices(all_characters, k=length - 4)

    # Shuffle to ensure randomness
    random.shuffle(password)

    return ''.join(password)

# Main program
if __name__ == "__main__":
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired password length (minimum 4): "))
        generated_password = generate_password(length)
        print(f"Your generated password is: {generated_password}")
    except ValueError as e:
        print(f"Error: {e}")
