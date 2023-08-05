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
    def raise_if_lte_zero(value, message: str):
        if value <= 0:
            raise ValueError(message)

    @staticmethod
    def raise_if_value_gt_max_value(value, max_value, message):
        if value > max_value:
            raise ValueError(message)

    @staticmethod
    def raise_if_value_gte_max_value(value, max_value, message):
        if value >= max_value:
            raise ValueError(message)

    @staticmethod
    def raise_if_value_is_lt_min_value(value, min_number, message: str):
        if value < min_number:
            raise ValueError(message)

    @staticmethod
    def raise_if_value_is_lte_min_value(value, min_number, message: str):
        if value <= min_number:
            raise ValueError(message)

    @staticmethod
    def raise_if_value_is_ne_value(value, required_number, message: str):
        if value != required_number:
            raise ValueError(message)

    @staticmethod
    def raise_if_value_not_in_list(value: str, available: List[str], message: str):
        if value not in available:
            raise ValueError(message)

    @staticmethod
    def raise_if_value_in_list(value: str, available: List[str], message: str):
        if value in available:
            raise Exception(message)
