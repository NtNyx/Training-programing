import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4!")
        return None


    characters = string.ascii_letters + string.digits + string.punctuation

   
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Random Password Generator")
    try:
        length = int(input("Enter the desired length of your password: "))
        password = generate_password(length)
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
