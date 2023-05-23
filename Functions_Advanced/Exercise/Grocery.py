def grocery_store(**kwargs):
    result = ""
    sorted_dict = dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
    for k, v in sorted_dict.items():
        result += f"{k}: {v}\n"

    return result
