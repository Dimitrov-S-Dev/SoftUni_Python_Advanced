class Customer:
    def __init__(self, name: str, age: int, c_id: int):
        self.name = name
        self.age = age
        self.id = c_id
        self.rented_dvds = []

    def __repr__(self):
        rented_dvd = ', '.join(d.name for d in self.rented_dvds)
        return f"{self.id}: {self.name} of age {self.age} has " \
               f"{len(self.rented_dvds)} rented DVD's ({rented_dvd})"
