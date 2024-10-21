"""
Print all the cubic numbers up to and including 729
Print all the square numbers up to and including 729

Which cubic numbers are also square numbers?
Which cubic numbers are not square numbers?
"""

def main():
    numbers_to_square = [x for x in range(0,730) if x * x < 730]
    numbers_to_cube = [x for x in range(0, 729) if x * x * x <730]

    square_numbers = [x * x for x in numbers_to_square]
    cubic_numbers = [x * x * x for x in numbers_to_cube]
    print(square_numbers)
    print(cubic_numbers)

    square_numbers_set = set(square_numbers)
    cubic_numbers_set = set(cubic_numbers)

    print(cubic_numbers_set.intersection(square_numbers_set))
    print(cubic_numbers_set.difference(square_numbers_set))

main()