def naughty_or_nice_list(kids_lst, *args, **kwargs):
    nice = []
    naughty = []
    not_found = []

    for number, name in kids_lst:
        number_count = sum(1 for num, _ in kids_lst if num == number)
        name_count = sum(1 for _, n in kids_lst if n == name)

        if f'{number}-Naughty' in args and number_count == 1:
            naughty.append(name)

        elif f'{number}-Nice' in args and number_count == 1:
            nice.append(name)

        elif name in kwargs and name_count == 1:

            if kwargs[name] == 'Naughty':
                naughty.append(name)

            elif kwargs[name] == 'Nice':
                nice.append(name)

        else:
            not_found.append(name)

    nice_output = f"{', '.join(nice)}"
    naughty_output = f"{', '.join(naughty)}"
    not_found_output = f"{', '.join(not_found)}"

    output = ""
    if nice_output:
        output += f"Nice: {nice_output}\n"
    if naughty_output:
        output += f"Naughty: {naughty_output}\n"
    if not_found:
        output += f"Not found: {not_found_output}\n"

    return output

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))

