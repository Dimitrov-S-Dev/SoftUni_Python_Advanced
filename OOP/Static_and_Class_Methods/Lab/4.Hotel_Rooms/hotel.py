from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(stars_count)

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                if room.capacity >= people and not room.is_taken:
                    room.is_taken = True
                    self.guests += room.guests

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                if room.is_taken:
                    room.is_taken = False
                    room.guests = 0

    def status(self):
        output = f"Hotel {self.name} has " \
                 f"{self.guests} total guests\n"
        output += f"Free rooms: {', '.join([str(r.number) for r in self.rooms if not r.is_taken])}\n"
        output += f"Taken rooms: {', '.join([str(r.number) for r in self.rooms if r.is_taken])}"

        return output

