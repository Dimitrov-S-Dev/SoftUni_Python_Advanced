def age_assignment(*args, **kwargs):
    result = ""
    for name in sorted(args):
        result += f"{name} is {kwargs[name[0]]} years old.\n"

    return result
