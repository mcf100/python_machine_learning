fruits = ["apple", "orange", "strawberry", "banana"]
print(fruits)

fruits.append("lychee")
print(fruits)

print(fruits[2])

fruits[2] = "blackberry"

print(fruits[2])

print(fruits[1:4])

fruits[1:4] = ["lime"]
print(fruits)

fruits[2:] = ["kiwi"]
print(fruits)

fruits[:2] = ["lemon", "redcurrent", "gooseberry"]
print(fruits)