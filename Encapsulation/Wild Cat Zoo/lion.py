from Animal import Animal


class Lion(Animal):
    MONEY_FOR_CARE = 50

    def __init__(self, name, gender: str, age: int):
        super().__init__(name, gender, age, money_for_care=Lion.MONEY_FOR_CARE)
