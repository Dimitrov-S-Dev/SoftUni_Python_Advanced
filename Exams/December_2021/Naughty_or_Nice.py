def naughty_or_nice_list(santa_list, *args, **kwargs):
    nice_list = []
    naughty_list = []
    not_found_list = []

    for count, name in santa_list:
        count_occurrences = sum(1 for c, _ in santa_list if c == count)
        name_occurrences = sum(1 for _, n in santa_list if n == name)

        if f'{count}-Naughty' in args and count_occurrences == 1:
            naughty_list.append(name)
            santa_list = [(c, n) for c, n in santa_list if n != name]
        elif f'{count}-Nice' in args and count_occurrences == 1:
            nice_list.append(name)
            santa_list = [(c, n) for c, n in santa_list if n != name]
        elif name in kwargs and name_occurrences == 1:
            if kwargs[name] == 'Naughty':
                naughty_list.append(name)
                santa_list = [(c, n) for c, n in santa_list if n != name]
            elif kwargs[name] == 'Nice':
                nice_list.append(name)
                santa_list = [(c, n) for c, n in santa_list if n != name]
        else:
            not_found_list.append(name)

    nice_output = "Nice: " + ", ".join(nice_list) if nice_list else ""
    naughty_output = "Naughty: " + ", ".join(naughty_list) if naughty_list else ""
    not_found_output = "Not found: " + ", ".join(not_found_list) if not_found_list else ""

    output = nice_output + "\n" + naughty_output + "\n" + not_found_output

    return output
