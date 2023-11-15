# login_validator.py
import re
import sys

def is_password_strong(password):
    # Check if the password is at least 12 characters long
    if len(password) < 12:
        print("Password must be at least 12 characters long.")
        sys.exit(1)
    
    # Check if the password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
        sys.exit(1)
    
    # Check if the password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        print("Password must contain at least one lowercase letter.")
        sys.exit(1)
    
    # Check if the password contains at least one digit
    if not any(char.isdigit() for char in password):
        print("Password must contain at least one digit.")
        sys.exit(1)
    
    # Check if the password contains at least one special character
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>/?"
    if not any(char in special_characters for char in password):
        print("Password must contain at least one special character.")
        sys.exit(1)
    
    # Check if the password does not contain common words or patterns
    common_patterns = ["password", "123456", "qwerty"]
    if any(pattern in password.lower() for pattern in common_patterns):
        print("Password must not contain common words or patterns.")
        sys.exit(1)
    
    # All checks passed, the password is strong
    print("Password is strong.")
    sys.exit(0)

if __name__ == "__main__":
    # Get the password from the command line arguments
    if len(sys.argv) != 2:
        print("Usage: python login_validator.py <password>")
        sys.exit(1)

    input_password = sys.argv[1]

    # Check the strength of the password
    is_password_strong(input_password)
