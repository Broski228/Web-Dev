class Animal:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def speak(self):
        return ". . ."

    def describe(self):
        return f"{self.name} is {self.age} years old and is {self.color}"

    def __str__(self):
        return f"{self.name}({self.__class__.__name__})"

class Dog(Animal):
    def __init__(self, name, color, age, breed):
        super().__init__(name, color, age)
        self.breed = breed

    def speak(self):
        return "WOof!"
    def fetch(self):
        return f"{self.name} fetches the ball"


class Cat(Animal):
    def __init__(self, name, color, age, indoor):
        super().__init__(name, color, age)
        self.indoor = indoor

    def speak(self):
        return "Meow!"

    def purr(self):
        return f"{self.name} is purring..."