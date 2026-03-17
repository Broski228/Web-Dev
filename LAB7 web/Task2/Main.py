from Models import Animal, Dog, Cat

dog1 = Dog("Rex", "green", 4, "Labrador")
cat1 = Cat("BOB", "blue", 5, True)

animals = [dog1, cat1]

for i in animals:
    print(i)

for i in animals:
    print(i.describe())

for i in animals:
    print(f"{i.name} says: {i.speak()}")

print(dog1.fetch())
print(cat1.purr())