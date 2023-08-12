class Player:
    STAMINA_DEFAULT = 100
    MIN_AGE = 12
    STAMINA_MIN_VALUE = 0
    STAMINA_MAX_VALUE = 100

    def __init__(self, name: str, age: int, stamina=STAMINA_DEFAULT):
        self.player_names = []
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name not valid!")
        elif value in self.player_names:
            raise ValueError(f"Name {value} is already used!")

        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < Player.MIN_AGE:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value < Player.STAMINA_MIN_VALUE or value > Player.STAMINA_MAX_VALUE:
            raise ValueError("Stamina not valid!")
        self.__stamina = value

    @property
    def need_sustenance(self):
        return self.stamina < Player.STAMINA_MAX_VALUE

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
