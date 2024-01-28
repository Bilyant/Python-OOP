from project.animal import Animal


class Tiger(Animal):
    tigers_care_money = 45

    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, money_for_care=Tiger.tigers_care_money)
