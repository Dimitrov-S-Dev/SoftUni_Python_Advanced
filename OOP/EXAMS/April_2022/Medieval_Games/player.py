from OOP.EXAMS.April_2022.Medieval_Games.core.validator import Validator


class Player:
    NAMES = []
    MIN_VALUE = 0
    MAX_VALUE = 100

    def __init__(self, name: str, age: int, stamina: int = 100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def need_sustenance(self):
        return self.stamina < self.MAX_VALUE

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_empty_string(value, "Name not valid!")
        Validator.raise_if_name_exist(value, self.NAMES, f"Name {value} is already used!")
        self.__name = value
        self.NAMES.append(self.name)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validator.raise_if_number_not_in_range(value, 12, "The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        Validator.raise_if_stamina_not_in_range(value, self.MIN_VALUE, self.MAX_VALUE, "Stamina not valid!")
        self.__stamina = value

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
