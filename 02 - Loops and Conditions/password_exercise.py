
"""

Write a program that asks the user to enter a password and compares it to a hard coded password.

If the password is correct, the program prints "Greetings Professor Falcon" and exits.

If the password is incorrect, the program prints "Access denied" and the asks for the password again.

The program will ask for the password three times if nexessary.

After that it exits

"""

PASSWORD = "root"

for _ in range(1,4):
    attempts_left = 3 - int(_)
    password = input("Please enter password: ")
    if password == PASSWORD:
        print("Greetings Professor Falcon")
        break
    else: 
        print(f"Access denied on attempt {_}, {attempts_left} attempts left")

if password != PASSWORD:
    print("You are out of attempts. Wiping Hard drive.")