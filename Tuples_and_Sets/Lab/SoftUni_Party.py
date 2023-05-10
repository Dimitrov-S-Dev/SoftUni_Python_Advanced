# def get_guests():
#     guests = []
#     while True:
#         data = input()
#         if data == "End":
#             break
#         guests.append(data)
#     return guests
#
#
# def print_func(not_arrived_data):
#     print(len(not_arrived_data))
#     for guest_num in sorted(not_arrived_data):
#         print(guest_num)
#
#
# n = int(input())
# reservation_codes = [input() for _ in range(n)]
# arrived_guests = get_guests()
# not_arrived_guests = set(reservation_codes).difference(arrived_guests)
# print_func(not_arrived_guests)

def is_vip(guest):
    return guest[0].isdigit()


n = int(input())

vip_guests = set()
regular_guests = set()

for _ in range(n):
    reservation = input()
    if is_vip(reservation):
        vip_guests.add(reservation)
    else:
        regular_guests.add(reservation)

while True:
    guest = input()
    if guest == "END":
        break
    if is_vip(guest):
        vip_guests.remove(guest)
    else:
        regular_guests.remove(guest)

print(len(vip_guests) + len(regular_guests))
[print(guest) for guest in sorted(vip_guests)]
[print(guest) for guest in sorted(regular_guests)]
