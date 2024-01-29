class Customer:
    def __init__(self, name: str, age: int, id_number: int):
        self.name = name
        self.age = age
        self.id_number = id_number
        self.rented_dvds = []

    def __repr__(self):
        dvds = ', '.join([d.name for d in self.rented_dvds])
        return f'{self.id_number}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD\'s ({dvds})'
