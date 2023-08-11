class Equipment:
    Equipment_ID = 1

    def __init__(self, name: str):
        self.name = name
        self.id = self.Equipment_ID
        Equipment.Equipment_ID += 1

    @staticmethod
    def get_next_id():
        return Equipment.Equipment_ID

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
