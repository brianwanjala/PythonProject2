import secrets
import string
import random
from colorama import Fore, Style, init

# Initialize colorama (required on Windows)
init(autoreset=True)


def gen_password(length: int) -> str:
    """
    Securely generate a random password with the given length.
    Ensures at least one uppercase, one lowercase, one digit, and one special character.
    """
    if length < 8:
        raise ValueError("Password length must be at least 8 characters!")

    # Character groups
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    punctuation = string.punctuation

    # Ensure at least one from each category
    password_chars = [
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(digits),
        secrets.choice(punctuation)
    ]

    # Fill the remaining characters randomly from all sets
    all_characters = uppercase + lowercase + digits + punctuation
    remaining_length = length - len(password_chars)
    password_chars += [secrets.choice(all_characters) for _ in range(remaining_length)]

    # Shuffle to avoid predictable positions
    random.SystemRandom().shuffle(password_chars)

    return ''.join(password_chars)


def validate_password(password: str) -> bool:
    """
    Validate that a password meets complexity requirements:
    - At least 8 characters
    - Contains at least one digit
    - Contains both uppercase and lowercase letters
    - Contains at least one special character
    """
    if len(password) < 8:
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c in string.punctuation for c in password):
        return False
    return True


def main():
    """
    Main menu loop for password generation and validation.
    """
    while True:
        print(f"\n{Fore.CYAN}=== Password Utility ==={Style.RESET_ALL}")
        print("1. Generate password")
        print("2. Validate password")
        print("3. Quit")

        choice = input("Enter a choice (1-3): ").strip()

        if choice == '1':
            try:
                length = int(input("Enter desired password length: "))
                password = gen_password(length)
                print(f"\n{Fore.GREEN}✅ Generated Password:{Style.RESET_ALL} {password}")

                if validate_password(password):
                    print(f"{Fore.GREEN}🔒 This password meets all security requirements.{Style.RESET_ALL}")
                else:
                    print(f"{Fore.YELLOW}⚠️ Generated password does not meet validation rules (rare). Try again.{Style.RESET_ALL}")

            except ValueError as e:
                print(f"{Fore.RED}⚠️  {e}{Style.RESET_ALL}")

        elif choice == '2':
            password = input("Enter password to validate: ")
            if validate_password(password):
                print(f"{Fore.GREEN}✅ Password is strong.{Style.RESET_ALL}")
            else:
                print(f"\n{Fore.RED}❌ Password is weak. Requirements:{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}- At least 8 characters")
                print("- At least one digit (0-9)")
                print("- At least one uppercase letter (A-Z)")
                print("- At least one lowercase letter (a-z)")
                print("- At least one special character (!, @, #, etc.)")

        elif choice == '3':
            print(f"{Fore.CYAN}👋 Bye!{Style.RESET_ALL}")
            break

        else:
            print(f"{Fore.RED}⚠️ Invalid option. Please choose 1, 2, or 3.{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
