from horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120  # km/h
    SPEED_INCREASE = 2

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        self.speed = max(self.speed * self.__class__.SPEED_INCREASE, self.MAX_SPEED)
