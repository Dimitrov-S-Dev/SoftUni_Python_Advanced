class Validator:
    @staticmethod
    def raise_if_empty_string_or_w_spaces(value: str, message: str):
        if value.strip() == "":
            raise ValueError(message)
