from project.calendar import months


class DVD:
    def __init__(self, name: str, id_number: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id_number = id_number
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    """
     it should create a new instance using the provided data. The date will be in the format 
     "day.month.year" - all of them should be numbers.
    """

    # 23.12.2020
    # creation_month -> December
    # creation_year -> 2020

    @classmethod
    def from_date(cls, id_number: int, name: str, date: str, age_restriction: int):
        data = date.split('.')
        month = months[int(data[1])]
        year = int(data[2])
        return cls(name, id_number, year, month, age_restriction)

    def __repr__(self):
        rented = 'rented' if self.is_rented else 'not rented'
        return f'{self.id_number}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {rented}'
