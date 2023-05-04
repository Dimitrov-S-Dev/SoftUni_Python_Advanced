def get_guests():
    guests = []
    while True:
        data = input()
        if data == "End":
            break
        guests.append(data)
    return guests


def print_func(not_arrived_data):
    print(len(not_arrived_data))
    for guest_num in sorted(not_arrived_data):
        print(guest_num)


n = int(input())
reservation_codes = [input() for _ in range(n)]
arrived_guests = get_guests()
not_arrived_guests = set(reservation_codes).difference(arrived_guests)
print_func(not_arrived_guests)



