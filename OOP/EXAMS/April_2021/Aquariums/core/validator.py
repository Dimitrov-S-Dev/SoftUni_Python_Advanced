class Validator:
    @staticmethod
    def raise_if_empty_string(value: str, message: str):
        if value == "":
            raise ValueError(message)

    @staticmethod
    def raise_if_lte_to_zero(value: float, message):
        if value <= 0:
            raise ValueError(message)
