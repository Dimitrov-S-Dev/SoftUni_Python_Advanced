text = input()
symbols_dict = {}

for elem in text:
    if elem not in symbols_dict.keys():
        symbols_dict[elem] = 0
    symbols_dict[elem] += 1

for k, v in sorted(symbols_dict.items()):
    print(f"{k}: {v} time\s")
