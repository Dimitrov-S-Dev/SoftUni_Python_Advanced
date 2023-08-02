from typing import List


class Validator:
    @staticmethod
    def raise_if_empty_string_or_w_space(value: str, message: str):
        if value.strip() == "":
            raise ValueError(message)

    @staticmethod
    def raise_if_lt_zero(value, message: str):
        if value < 0:
            raise ValueError(message)

    @staticmethod
    def raise_if_value_is_lt_min_value(value, min_number, message: str):
        if value < min_number:
            raise ValueError(message)

    @staticmethod
    def raise_if_skill_not_in_available(skill: str, available: List[str], message: str):
        if skill not in available:
            raise ValueError(message)

    @staticmethod
    def raise_if_skill_in_learned_list(skill: str, available: List[str], message: str):
        if skill in available:
            raise Exception(message)

