class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        result = 1
        for x in args:
            result *= x
        return result

    @staticmethod
    def divide(*args):
        result = args[0]
        for x in args[1:]:
            result /= x
        return result

    @staticmethod
    def subtract(*args):
        result = args[0]
        for x in args[1:]:
            result -= x
        return result
