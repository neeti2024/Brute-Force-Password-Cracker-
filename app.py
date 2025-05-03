import os
import string

def receive_password():
    file_path = "password.txt"
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            password = file.read().strip()  # read the password from the file
            print(f"Password received: {password}")
            return password
    else:
        print("No password file found.")
        
def bruteforce(target_password):
    characters = string.ascii_letters + string.digits + '!@?#%'
    password_length = 1 # start with a password length of 1
    found = False

    while not found:
        for guess in generate_guesses(characters, password_length):
            print(f"Trying password: {guess}")
            if guess == target_password:
                print(f"Password found: {guess}")
                found = True
                break
        password_length += 1

def generate_guesses(characters, length): # generate all possible combinations of characters
    if length == 1:
        return characters
    
    prev = generate_guesses(characters, length - 1)
    return [p + c for p in prev for c in characters]

def main():
    password = receive_password() 
    bruteforce(password)
    
if __name__ == "__main__":
    main()
