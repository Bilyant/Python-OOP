from project.animals.animal import Bird


class Owl(Bird):
    @property
    def weight_increase(self):
        return 0.25

    @property
    def allowed_food(self):
        return ["Meat"]

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)


class Hen(Bird):
    @property
    def weight_increase(self):
        return 0.35

    @property
    def allowed_food(self):
        return ["Vegetable", "Fruit", "Meat", "Seed"]

    @staticmethod
    def make_sound():
        return "Cluck"

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)
