from functools import wraps


def multiply(n):
    def decorator(func):
        @wraps(n)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return n * result

        return wrapper
    return decorator


@multiply(5)
def add_ten(number):
    return number + 10


print(add_ten(6))
