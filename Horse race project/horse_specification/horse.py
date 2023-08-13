from abc import ABC, abstractmethod


class Horse(ABC):
    NAME_MIN_LENGTH = 4
    MAX_SPEED = 0
    SPEED_INCREASE = 0

    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False
        # Keep in mind that one horse can have only one rider.

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < Horse.NAME_MIN_LENGTH:
            raise ValueError("Horse name {value} is less than 4 symbols!")
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > self.__class__.MAX_SPEED:
            raise ValueError("Horse speed is too high!")
        self.__speed = value

    @abstractmethod
    def train(self):
        self.speed = max(self.speed * self.__class__.SPEED_INCREASE, self.MAX_SPEED)
