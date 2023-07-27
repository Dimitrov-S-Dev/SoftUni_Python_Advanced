class Validator:

    @staticmethod
    def raise_if_string_is_empty_or_white_space(string: str, message):
        if string.strip() == "":
            raise ValueError(message)

    @staticmethod
    def raise_if_number_is_less_or_equal_to_zero(number: float, message):
        if number <= 0:
            raise ValueError(message)

    @staticmethod
    def raise_if_number_is_not_in_range(number: int, min_number: int, max_number: int, message: str):
        if number < min_number or number > max_number:
            raise ValueError(message)
