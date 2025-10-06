import random
import string

def gen_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    if length < 8:
        print('Password length should be at least 8 characters!')
        return None
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password
def validate_password(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char in string.punctuation for char in password):
        return False
    return True
def main():
    while True:
        print('1. Generate password')
        print('2. Validate password')
        print('3. Quit')
        choice = input('Enter a choice')
        if choice=='1':
            length= int(input('Enter password length'))
            password=gen_password(length)
            if password:
                print('Generated password:', password)
        if choice=='2':
            password = input('Enter password to validate')
            if validate_password(password):
                print('Password is valid')
                break
            else:
                print('Password is not valid. Ensure it has: ')
                print('At least 8 characters')
                print('At least one digit')
                print('At least one uppercase letter')
                print('At least one lowercase letter')
        if choice == '3':
            break
        else:
            print('invalid option')

if __name__=='__main__':
    main()
print('Bye')






