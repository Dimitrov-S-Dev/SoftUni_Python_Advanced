from functools import wraps


def even_parameters(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for elem in args:
            if isinstance(elem, int):
                if elem % 2 == 0:
                    continue
            return "Please use only even numbers!"
        result = func(*args, **kwargs)
        return result
    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))
