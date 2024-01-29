from math import floor


class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if type(float_value).__name__ != 'float':
            return 'value is not a float'
        return cls(floor(float_value))

    @classmethod
    def from_roman(cls, value):
        ...

    @classmethod
    def from_string(cls, value):
        if type(value).__name__ != 'str':
            return 'wrong type'
        return cls(int(value))
