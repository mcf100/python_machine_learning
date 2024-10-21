def main():
    fruits = {
        "apple": "green",
        "orange": "orange",
        "banana": "yellow",
    }

    colour = fruits.get("mango")

    print(colour)
    print(type(colour))
    print()

    colour = fruits.get("mango", "red")
    print(colour)

    print()

    colour = fruits.get("banana", "red")
    print(colour)


main()