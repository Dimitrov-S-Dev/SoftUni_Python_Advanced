def shopping_cart(*args):
    cart = {
        "Soup": [],
        "Pizza": [],
        "Dessert": [],
    }

    for data in args:
        if data == "Stop":
            break

        meal, product = data
        if meal == "Soup" and len(cart["Soup"]) == 3:
            continue
        elif meal == "Pizza" and len(cart["Pizza"]) == 4:
            continue
        elif meal == "Dessert" and len(cart["Dessert"]) == 2:
            continue

        if product not in cart[meal]:
            cart[meal].append(product)

    for value in cart.values():
        if len(value) > 0:
            break

    else:
        return "No products in the cart!"

    sort_cart = sorted(cart.items(), key=lambda x: (-len(x[1]), x[0]))

    output = ""
    for meal, products in sort_cart:
        output += f"{meal}:\n"
        for product in sorted(products):
            output += f" - {product}\n"

    return output
