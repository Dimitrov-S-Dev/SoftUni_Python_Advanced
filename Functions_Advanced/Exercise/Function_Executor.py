def func_executor(*args):
    result = []
    for func, nums in args:
        result.append(f"{func.__name__} - {func(*nums)}")

    return "\n".join(result)
