from abc import ABC

from supply.supply import Supply


class Drink(Supply):
    ENERGY_UNITS = 15

    def __init__(self, name: str, energy=ENERGY_UNITS):
        super().__init__(name, energy)

    def details(self):
        return f"{self.__class__.__name__}: {self.name}, {self.energy}"
