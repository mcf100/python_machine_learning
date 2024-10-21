animals1 = ("dog", "cat", "mouse")
animals2 = ("lion", "tiger", "elepant")

fruits1 = ["apple", "orange"]
fruits2 = ["strawberry", "melon", "grape"]

print(id(animals1))
animals1 += animals2
print(animals1)
print(id(animals1))

print()

print(id(fruits1))
fruits1 += fruits2
print(fruits1)
print(id(fruits1))
