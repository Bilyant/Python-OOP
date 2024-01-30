from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def __repr__(self):
        ...

    @abstractmethod
    def make_sound(self):
        ...


class Dog(Animal):
    def __init__(self, name: str, age: int, gender: str):
        super().__init__(name, age, gender)

    def __repr__(self):
        return f'This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}'

    def make_sound(self):
        return f'Woof!'


class Cat(Animal):
    def __init__(self, name: str, age: int, gender: str):
        super().__init__(name, age, gender)

    def __repr__(self):
        return f'This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}'

    def make_sound(self):
        return f'Meow meow!'


class Kitten(Cat):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, gender='Female')

    def make_sound(self):
        return f'Meow'


class Tomcat(Cat):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, gender='Male')

    def make_sound(self):
        return f'Hiss'


dog = Dog("Rocky", 3, "Male")
print(dog.make_sound())
print(dog)
tomcat = Tomcat("Tom", 6)
print(tomcat.make_sound())
print(tomcat)

print(30 * '-')

kitten = Kitten("Kiki", 1)
print(kitten.make_sound())
print(kitten)
cat = Cat("Johnny", 7, "Male")
print(cat.make_sound())
print(cat)
