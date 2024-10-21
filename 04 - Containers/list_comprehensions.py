animals1 = ["dog", "goat", "sloth", "tiger"]

animals2 = animals1

del animals2[1]

print(animals1)
print(animals2)
print()

animals3 = animals1.copy()
del animals3[1]

print(animals1)
print(animals3)
print()

animals4 = [animal.upper() for animal in animals1]
print(animals4)

lengths = [len(text) for text in animals1]
print(lengths)
print()

numbers1 = [3, 6, 3, 8, 5]
print(numbers1)
numbers2 = [x*x for x in numbers1]
print(numbers2)

zero_to_one_hundred = [x for x in range(1,101)]
print(zero_to_one_hundred)