from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(name=f'{stars_count} stars Hotel')

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        current_room = [r for r in self.rooms if r.number == room_number][0]
        current_room.take_room(people)

    def free_room(self, room_number):
        current_room = [r for r in self.rooms if r.number == room_number][0]
        current_room.free_room()

    def status(self):
        free_rooms = [r.number for r in self.rooms if not r.is_taken]
        taken_rooms = [r.number for r in self.rooms if r.is_taken]
        total_guests = sum([r.guests for r in self.rooms if r.is_taken])
        result = [
            f'Hotel {self.name} has {total_guests} total guests',
            f'Free rooms: {", ".join([str(r) for r in free_rooms])}',
            f'Taken rooms: {", ".join([str(r) for r in taken_rooms])}',
                  ]
        return '\n'.join(result)
