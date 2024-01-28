from project.animal import Animal


class Cheetah(Animal):
    cheetah_care_money = 60

    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, money_for_care=Cheetah.cheetah_care_money)
