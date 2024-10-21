def main():
    fruits = {
        "apple": "green",
        "orange": "orange",
        "banana": "yellow",
    }

    for fruit in fruits:
        print(fruit + ": " + fruits[fruit])
    
    print()

    print("apple" in fruits)

    print()

    for (fruit, colour) in fruits.items():
        print(fruit + ", " + colour)

    print()
    
    for fruit in fruits.values():
        print(fruit)

main()

