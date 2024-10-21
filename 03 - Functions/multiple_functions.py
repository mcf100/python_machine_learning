"""
Part 1: Asks the user to enter a password
Part 2: If they enter correct password it will print access granted
Part 3: Otherwise will print access denied

"""
PASSWORD = "root"

def greeting():
    print("Welcome, no unauthorised users!")

def check_password():
    password = input("Please enter your password: ")

    if PASSWORD == password:
        print("Access granted.")
    else:
        print("Access denied.")

def main():
    greeting()
    check_password()

main()