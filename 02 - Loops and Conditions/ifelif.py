WORKER1 = "Rosie"
WORKER2 = "Bella"
TEACHER = "Charlotte"
WELCOME_MESSAGE = "Hello, your name is "

name = input("Please enter your name: ")


if name == WORKER1:
    print(f"{WELCOME_MESSAGE}{WORKER1}")
elif name == WORKER2:
    print(f"{WELCOME_MESSAGE}{WORKER2}")
elif name == TEACHER:
    print(f"{WELCOME_MESSAGE}{TEACHER}")
else:
    print("Name not recognised")
    
