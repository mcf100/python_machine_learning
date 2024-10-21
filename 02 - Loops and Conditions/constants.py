#A constant is usually captured in uppercase to demonstrate it is a variable
WELCOME_MESSAGE = "Hello, your name is "

name = input("Please enter your name: ")


if name == "Max":
    print(f"{WELCOME_MESSAGE}{name}")
else:
    print("Your name is not Max")
    
print("Program finished.")