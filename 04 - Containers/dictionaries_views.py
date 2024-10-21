def main():
    fruits = {
        "apple": "green",
        "orange": "orange",
        "banana": "yellow",
    }

    keys = fruits.keys()
    values = fruits.values()
    items = fruits.items()

    print(keys)
    print(values)
    print(items)

    print()

    keys_list = list(keys)
    print(keys_list)
    print()

    fruits["raspberry"] = "red"

    print(keys)
    print(keys_list)

main()