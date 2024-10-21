numbers = [1, 2, 3, 1]

print(numbers)

numbers = (1, 2, 3, 1)

print(numbers)

numbers = {1, 2, 3, 1}

print(numbers)

for number in numbers:
    print(number)

print(3 in numbers)
print(4 in numbers)

numbers_list = [2, 3, 3, 2, 5, 6]
numbers_list = set(numbers_list)
print(numbers_list)

"""
list: ordered, "in" is slow, mutable
tuple: ordered, "in" is slow, immutable
set: not ordered, "in" is fast, mutable

"""