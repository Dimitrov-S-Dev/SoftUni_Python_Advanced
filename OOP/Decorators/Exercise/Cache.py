def cache(func):
    log = {}

    def wrapper(argument):
        if argument in log:
            return log[argument]

        result = func(argument)
        log[argument] = result
        return result
    wrapper.log = log
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


fibonacci(3)
print(fibonacci.log)
