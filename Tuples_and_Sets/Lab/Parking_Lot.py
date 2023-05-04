n = int(input())
plate_number = [input() for _ in range(n)]
parking_lot = set()
COMMAND_IN = "IN"
COMMAND_OUT = "OUT"

for record in plate_number:
    command, plate_num = record.split(", ")

    if command == COMMAND_IN:
        parking_lot.add(plate_num)

    elif command == COMMAND_OUT:
        parking_lot.remove(plate_num)

if parking_lot:
    for num in parking_lot:
        print(num)
else:
    print("Parking lot is Empty")
