from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def refuel(self, quantity):
        ...

    @abstractmethod
    def drive(self, distance):
        ...


"""
Car and Truck both receive fuel_quantity and fuel_consumption in liters per km upon initialization. 
They both can be driven a given distance: drive(distance) and refueled with a given amount of fuel: refuel(fuel). 
It is summer, so both vehicles use air conditioners, and their fuel consumption per km when driving is increased 
by 0.9 liters for the car and 1.6 liters for the truck. 
Also, the Truck has a tiny hole in its tank, and when it is refueled, it keeps only 95% of the given fuel. 
The car has no problems and adds all the given fuel to its tank. 
If a vehicle cannot travel the given distance, its fuel does not change.
"""


class Car(Vehicle):
    air_conditioner = 0.9

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        super().__init__(fuel_quantity, fuel_consumption)
        self.fuel_consumption += Car.air_conditioner

    def refuel(self, quantity):
        self.fuel_quantity += quantity

    def drive(self, distance):
        required_fuel = distance * self.fuel_consumption
        if required_fuel <= self.fuel_quantity:
            self.fuel_quantity -= required_fuel


class Truck(Vehicle):
    air_conditioner = 1.6

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        super().__init__(fuel_quantity, fuel_consumption)
        self.fuel_consumption += Truck.air_conditioner

    def refuel(self, quantity):
        self.fuel_quantity += quantity * 0.95

    def drive(self, distance):
        required_fuel = distance * self.fuel_consumption
        if required_fuel <= self.fuel_quantity:
            self.fuel_quantity -= required_fuel


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
