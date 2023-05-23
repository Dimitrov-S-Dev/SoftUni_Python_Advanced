def grocery_store(**kwargs):
    result = ""
    sorted_product = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    for product, quantity in sorted_product:
        result += f"{product}: {quantity}\n"

    return result
