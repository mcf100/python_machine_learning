numbers = {x for x in range(15)}

print(numbers)

numbers.remove(6)
print(numbers)

numbers.discard(20)
print(numbers)

for x in numbers:
    print(x)