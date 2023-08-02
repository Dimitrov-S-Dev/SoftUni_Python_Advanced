class Validator:
    @staticmethod
    def raise_if_empty_string_or_w_space(value: str, message: str):
        if value.strip() == "":
            raise ValueError(message)

    @staticmethod
    def raise_if_lt_zero(value: float, message):
        if value < 0:
            raise ValueError(message)

    @staticmethod
    def raise_if_value_is_lt_min_value(value: float, min_number: float, message: str):
        if value < min_number:
            raise ValueError(message)
