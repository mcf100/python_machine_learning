def main():

    numbers1 = [x for x in range(0, 10)]
    print(numbers1)

    numbers2 = [x for x in numbers1 if x > 5]
    print(numbers2)

    # Mod operator
    print(13 % 5)

    print(13 % 2 == 0)

    numbers3 = [x for x in numbers1 if x % 2 == 0]
    print(numbers3)

    numbers4 = [x for x in range(0, 21) if x % 2 == 1]
    print(numbers4)

main()