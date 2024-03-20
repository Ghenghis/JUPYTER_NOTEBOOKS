# import re

# def is_strong_password(password):
#     # Check if password has at least one uppercase character
#     if not re.search(r'[A-Z]', password):
#         return False

#     # Check if password has at least one number
#     if not re.search(r'\d', password):
#         return False

#     # Check if password has at least one special symbol
#     if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
#         return False

#     # Password meets all the criteria for a strong password
#     return True

# # Example usage
# password = input("Enter a password: ")
# print(is_strong_password(password))

def is_strong_password(password):
    """
    A strong password has at least one uppercase character,
    at least one number, and at least one special symbol.
    Return True if the password is a strong password, False if not.
    """
    return any(char.isupper() for char in password) and \
        any(char.isdigit() for char in password) and \
        any(not char.isalnum() for char in password)

# Example usage
pw = input("Enter a password: ")
print(is_strong_password(pw))  # False