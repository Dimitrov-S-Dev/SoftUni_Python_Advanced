def sorting_cheeses(**kwargs):
    result = ""
    sort_cheese = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    for cheese_name, quantity in sort_cheese:
        result += f"{cheese_name}\n"
        rev_quantities = sorted(quantity, reverse=True)
        for q in rev_quantities:
            result += f"{q}\n"

    return result
