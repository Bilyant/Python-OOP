class Customer:
    def __init__(self, name: str, age: int, customer_id: int):
        self.name = name
        self.age = age
        self.id = customer_id
        self.rented_dvds = []

    def __repr__(self):
        dvd_names = []
        for dvd in self.rented_dvds:
            dvd_names.append(dvd.name)
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ({', '.join(dvd_names)})"
