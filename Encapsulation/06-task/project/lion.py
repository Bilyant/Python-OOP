from project.animal import Animal


class Lion(Animal):
    lions_care_money = 50

    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, money_for_care=Lion.lions_care_money)
