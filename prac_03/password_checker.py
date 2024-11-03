"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
IS_SPECIAL_CHARACTER_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    length = len(password)
    if length < MIN_LENGTH or length > MAX_LENGTH:
        return False

    """Determine if the provided password is valid."""
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    for character in password:
        if character == '0':
            return False
        elif character.islower():
            has_lower = True
        elif character.isupper():
            has_upper = True
        elif character.isdigit():
            has_digit = True

    if IS_SPECIAL_CHARACTER_REQUIRED:
        for character in password:
            if character in SPECIAL_CHARACTERS:
                has_special = True
                break
    else:
        has_special = True

    if has_lower and has_upper and has_digit and has_special:
        return True
    else:
        return False

main()