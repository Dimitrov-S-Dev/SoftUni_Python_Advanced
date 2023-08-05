from abc import ABC, abstractmethod

from project.core.validator import Validator


class BaseClient(ABC):
    def __init__(self, name: str, client_id: str, income: float, interest: float):
        self.name = name
        self.client_id = client_id
        self.income = income
        self.interest = interest
        self.loans = []

    @property
    @abstractmethod
    def increase_interest_percent(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_empty_string_or_w_space(
            value,
            "Client name cannot be empty!")
        self.__name = value

    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, value):
        Validator.raise_if_value_is_ne_value(
            len(value),
            10,
            "Client ID should be 10 symbols long!")
        self.__client_id = value

    @property
    def income(self):
        return self.__income

    @income.setter
    def income(self, value):
        Validator.raise_if_lte_zero(
            value,
            "Income must be greater than zero!")
        self.__income = value

    def increase_clients_interest(self):
        self.interest += self.increase_interest_percent
