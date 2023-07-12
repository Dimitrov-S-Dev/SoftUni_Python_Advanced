class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return f"{self.name} is making "
    
    
class Dog(Animal):
    def make_sound(self):
        return super().make_sound() + " woof-woof"


class Cat(Animal):
    def make_sound(self):
        return super().make_sound() + " meow"


class Chicken(Animal):
    def make_sound(self):
        return super().make_sound() + " cluck"


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Dog("Sharo"), Cat("Lady")]
animal_sound(animals)


# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
"""
class Animal:
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species


def animal_sound(animals: list):
    for animal in animals:
        if animal.species == 'cat':
            print('meow')
        elif animal.species == 'dog':
            print('woof-woof')


animals = [Animal('cat'), Animal('dog')]
animal_sound(animals)
"""