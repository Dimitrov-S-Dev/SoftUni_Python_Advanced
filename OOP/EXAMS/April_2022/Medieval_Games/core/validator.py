from typing import List


class Validator:
    @staticmethod
    def raise_if_empty_string(text: str, message: str):
        if text == "":
            raise ValueError(message)

    @staticmethod
    def raise_if_number_not_in_range(number: int, number_range, message):
        if number < number_range:
            raise ValueError(message)

    @staticmethod
    def raise_if_name_exist(name: str, names_lst: List, message):
        if name in names_lst:
            raise Exception(message)

    @staticmethod
    def raise_if_stamina_not_in_range(number: int, min_number: int, max_number: int, message):
        if number < min_number or number > max_number:
            raise ValueError(message)
