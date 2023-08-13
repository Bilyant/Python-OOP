from horse_specification.horse import Horse


class Thoroughbred (Horse):
    MAX_SPEED = 140  # km/h
    SPEED_INCREASE = 3

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        self.speed = max(self.speed * self.__class__.SPEED_INCREASE, self.MAX_SPEED)
