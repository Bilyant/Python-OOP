from project.animals.animal import Bird
from project.food import Food


class Owl(Bird):
    allowed_food_types = ['Meat']
    weight_gain = 0.25

    def __init__(self, name: str, weight: float, wing_size: float, food_eaten=0):
        super().__init__(name, weight, wing_size, food_eaten)

    def feed(self, food: Food):
        if food.__class__.__name__ not in self.allowed_food_types:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.weight += self.__class__.weight_gain * food.quantity
        self.food_eaten += food.quantity

    @staticmethod
    def make_sound():
        return 'Hoot Hoot'


class Hen(Bird):
    allowed_food_types = ['Vegetable', 'Fruit', 'Meat']
    weight_gain = 0.35

    def __init__(self, name: str, weight: float, wing_size: float, food_eaten=0):
        super().__init__(name, weight, wing_size, food_eaten)

    def feed(self, food: Food):
        if food.__class__.__name__ not in self.allowed_food_types:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.weight += self.__class__.weight_gain * food.quantity
        self.food_eaten += food.quantity

    @staticmethod
    def make_sound():
        return 'Cluck'
