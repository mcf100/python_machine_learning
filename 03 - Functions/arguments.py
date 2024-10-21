def greet(username, how_old):
    print("Hello " + username + ", you are " + how_old + " years old.")

def main():
    name = input("What is your name?: ")
    age = input("How old are you?: ")
    greet(name, age)

main()
