def main():
    fruits = {
        "apple": "green",
        "orange": "orange",
        "banana": "yellow",
    }

    print(fruits)
    print()

    del fruits["apple"]

    print(fruits)
    print()

    colour = fruits.pop("banana")
    
    print(fruits)
    print(colour)

main()