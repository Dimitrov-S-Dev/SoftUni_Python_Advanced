class Validator:

    @staticmethod
    def raise_if_less_then_four_symbols(model: str, message):
        if len(model) < 4:
            raise ValueError(message)

    @staticmethod
    def raise_if_invalid_speed_limit(speed: int, min_speed_limit: int, max_speed_limit: int, message):
        if speed < min_speed_limit or speed > max_speed_limit:
            raise ValueError(message)

    @staticmethod
    def raise_if_empty_or_only_white_spaces(name: str, message):
        if name.strip() == "":
            raise ValueError(message)

    @staticmethod
    def raise_if_empty_string(name: str, message):
        if name == "":
            raise ValueError(message)
