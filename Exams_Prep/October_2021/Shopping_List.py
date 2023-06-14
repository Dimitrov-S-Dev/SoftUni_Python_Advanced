def shopping_list(budget, **kwargs):
    bought_products = []
    if budget < 100:
        return "You do not have enough budget."
    else:
        for product, info in kwargs.items():
            price = info[0]
            qty = info[1]
            if budget < price * qty:
                continue
            if budget >= price * qty:
                total = price * qty
                budget -= total
                bought_products.append(f"You bought {product} for {total:.2f} leva.")
                if len(bought_products) == 5:
                    break

    output = ""
    for product in bought_products:
        output += f"{product}\n"
    return output
