def main():
    elements = (True, 3.2, 7, "goat")

    (is_raining, weight, volume, animal) = elements
    print(is_raining)
    print(weight)
    print(volume)
    print(animal)

    print()

    fruits = ("apple", "orange", "banana", "strawberry", "pear")
    (fruit1, fruit2, fruit3, *morefruits) = fruits
    print(fruit1)
    print(fruit2)
    print(fruit3)
    print(morefruits)


main()