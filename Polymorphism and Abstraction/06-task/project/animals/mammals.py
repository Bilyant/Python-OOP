from project.animals.animal import Mammal
from project.food import Food


class Mouse(Mammal):
    allowed_food_types = ['Vegetable', 'Fruit']
    weight_gain = 0.1

    def __init__(self, name: str, weight: float, living_region: str, food_eaten=0):
        super().__init__(name, weight, living_region, food_eaten)

    def feed(self, food: Food):
        if food.__class__.__name__ not in self.allowed_food_types:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.weight += self.__class__.weight_gain * food.quantity
        self.food_eaten += food.quantity

    @staticmethod
    def make_sound():
        return 'Squeak'


class Dog(Mammal):
    allowed_food_types = ['Meat']
    weight_gain = 0.4

    def __init__(self, name: str, weight: float, living_region: str, food_eaten=0):
        super().__init__(name, weight, living_region, food_eaten)

    def feed(self, food: Food):
        if food.__class__.__name__ not in self.allowed_food_types:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.weight += self.__class__.weight_gain * food.quantity
        self.food_eaten += food.quantity

    @staticmethod
    def make_sound():
        return 'Woof!'


class Cat(Mammal):
    allowed_food_types = ['Vegetable', 'Meat']
    weight_gain = 0.3

    def __init__(self, name: str, weight: float, living_region: str, food_eaten=0):
        super().__init__(name, weight, living_region, food_eaten)

    def feed(self, food: Food):
        if food.__class__.__name__ not in self.allowed_food_types:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.weight += self.__class__.weight_gain * food.quantity
        self.food_eaten += food.quantity

    @staticmethod
    def make_sound():
        return 'Meow'


class Tiger(Mammal):
    allowed_food_types = ['Meat']
    weight_gain = 1

    def __init__(self, name: str, weight: float, living_region: str, food_eaten=0):
        super().__init__(name, weight, living_region, food_eaten)

    def feed(self, food: Food):
        if food.__class__.__name__ not in self.allowed_food_types:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.weight += self.__class__.weight_gain * food.quantity
        self.food_eaten += food.quantity

    @staticmethod
    def make_sound():
        return 'ROAR!!!'

