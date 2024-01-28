from project.dough import Dough
from project.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, toppings_capacity: int):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = {}  # topping type as a key and the topping's weight as a value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError('The name cannot be an empty string')
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if not value:
            raise ValueError('You should add dough to the pizza')
        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value <= 0:
            raise ValueError('The topping\'s capacity cannot be less or equal to zero')
        self.__toppings_capacity = value

    """ 
    Add a new topping to the dictionary
    If there is no space left for a new topping, raise a ValueError: 
    "Not enough space for another topping"
    If the topping is already in the dictionary, increase the value of its weight.
    """
    def add_topping(self, topping: Topping):
        if len(self.toppings) >= self.toppings_capacity:
            raise ValueError('Not enough space for another topping')
        if topping not in self.toppings:
            self.toppings[topping] = 0
        self.toppings[topping] += topping.weight

    def calculate_total_weight(self):
        return self.dough.weight + sum([t.weight for t in self.toppings])
