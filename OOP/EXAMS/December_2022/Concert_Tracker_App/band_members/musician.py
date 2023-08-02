from abc import ABC, abstractmethod

from OOP.EXAMS.December_2022.Concert_Tracker_App.core.validator import Validator


class Musician(ABC):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.skills = []

    @property
    @abstractmethod
    def skills_available(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_empty_string_or_w_space(
            value,
            "Musician name cannot be empty!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validator.raise_if_value_is_lt_min_value(
            value,
            16,
            "Musicians should be at least 16 years old!")
        self.__age = value

    def learn_new_skill(self, new_skill: str):
        Validator.raise_if_skill_not_in_available(
            new_skill,
            self.skills_available,
            f"{new_skill} is not a needed skill!")
        Validator.raise_if_skill_in_learned_list(
            new_skill,
            self.skills,
            f"{new_skill} is already learned!")
        self.skills.append(new_skill)
        return f"{self.name} learned to {new_skill}."
