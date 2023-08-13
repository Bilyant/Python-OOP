from abc import ABC, abstractmethod
from user import User


class Movie(ABC):
    YEAR_MIN_VALUE = 1888

    def __init__(self, title: str, year: int, owner: object, age_restriction: int):
        self.title = title
        self.year = year
        self.owner = owner  # A user object that represents the one who made the movie
        self.age_restriction = age_restriction
        self.likes = 0

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if value == "":
            raise ValueError("The title cannot be empty string!")
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if value < Movie.YEAR_MIN_VALUE:
            raise ValueError("Movies weren't made before 1888!")
        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if value.__class__.__name__ != 'User':
            raise ValueError("The owner must be an object of type User!")
        self.__owner = value

    @abstractmethod
    def details(self):
        pass


"""

•	age_restriction: int
o	The movie is unsuitable for people under the given age. The age restriction value depends on the movie genre. 

Methods

details()
It returns a string with information about the movie by its type.

"""
