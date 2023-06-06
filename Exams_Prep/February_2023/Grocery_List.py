def shop_from_grocery_list(budget, grocery_lst, *args):
    purchased_items = set()
    is_ok = True
    for name, price in args:

        if name in purchased_items:
            continue
        if name not in grocery_lst:
            continue

        if budget >= price:
            budget -= price
            purchased_items.add(name)
        else:
            is_ok = False
            break

    if purchased_items.symmetric_difference(grocery_lst) or not is_ok:
        return f"You did not buy all the products. Missing products: " \
               f"{', '.join(purchased_items.symmetric_difference(grocery_lst))}."
    else:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
