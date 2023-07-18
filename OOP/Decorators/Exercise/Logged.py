from functools import wraps


def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"you called {func.__name__}{args}\nit returned {result}"
    return wrapper


@logged
def func(*args):
    return 3 + len(args)


@logged
def sum_func(a, b):
    return a + b


print(func(4, 4, 4))
print(sum_func(1, 4))
