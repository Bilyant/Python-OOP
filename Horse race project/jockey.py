class Jockey:
    AGE_RESTRICTION = 18

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.horse = None

    # Keep in mind that one jockey can ride only one horse.

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name should contain at least one character!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < Jockey.AGE_RESTRICTION:
            raise ValueError("Jockeys must be at least 18 to participate in the race!")
        self.__age = value
