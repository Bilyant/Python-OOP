from project.animals.animal import Mammal


class Mouse(Mammal):
    @property
    def weight_increase(self):
        return 0.1

    @property
    def allowed_food(self):
        return ["Vegetable", "Fruit"]

    @staticmethod
    def make_sound():
        return "Squeak"

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)


class Dog(Mammal):
    @property
    def weight_increase(self):
        return 0.4

    @property
    def allowed_food(self):
        return ["Meat"]

    @staticmethod
    def make_sound():
        return "Woof!"

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)


class Cat(Mammal):
    @property
    def weight_increase(self):
        return 0.3

    @property
    def allowed_food(self):
        return ["Vegetable", "Meat"]

    @staticmethod
    def make_sound():
        return "Meow"

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)


class Tiger(Mammal):
    @property
    def weight_increase(self):
        return 1

    @property
    def allowed_food(self):
        return ["Meat"]

    @staticmethod
    def make_sound():
        return "ROAR!!!"

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
