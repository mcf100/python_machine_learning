def main():
    animals = ("dog", "cat", "tiger", "wolf")
    
    number_animals = len(animals)
    
    print(number_animals)

    print(animals[0])
    
    print()
    
    for animal in animals:
        print(animal)

    print()

    for i in range(0, len(animals)):
        print(animals[i])

main()