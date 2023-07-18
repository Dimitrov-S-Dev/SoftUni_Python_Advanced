def type_check(kind):
    def decorator(func):
        def wrapper(argument):
            if not isinstance(argument, kind):
                return "Bad Type"

            result = func(argument)
            return result

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))
