from unittest import TestCase

from Tasks.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.fuel_consumption = 1.25
        self.fuel = 125
        self.capacity = self.fuel
        self.horse_power = 260
        self.vehicle = Vehicle(self.fuel, self.horse_power)

    # __init__()
    def test_init_expect_correct_values(self):
        self.assertEqual(self.fuel, self.vehicle.fuel)
        self.assertEqual(self.capacity, self.vehicle.capacity)
        self.assertEqual(self.horse_power, self.vehicle.horse_power)
        self.assertEqual(self.fuel_consumption, self.vehicle.fuel_consumption)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    # drive()
    def test_drive_when_enough_fuel(self):
        kilometers = 10
        expected_fuel = self.fuel - kilometers * self.fuel_consumption
        self.vehicle.drive(kilometers)
        self.assertEqual(expected_fuel, self.vehicle.fuel)

        kilometers = 90
        self.vehicle.drive(kilometers)
        expected_fuel = expected_fuel - kilometers * self.fuel_consumption
        self.assertEqual(expected_fuel, self.vehicle.fuel)

    def test_drive_when_not_enough_fuel_expect_raises(self):
        kilometers = 101
        message = 'Not enough fuel'
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(kilometers)
        self.assertEqual(message, str(ex.exception))

    # refuel()
    def test_refuel_when_valid_quantity_is_provided(self):
        # fuel quantity before refuel()
        self.assertEqual(self.fuel, self.vehicle.fuel)
        distance = 10
        refuel = 10
        self.vehicle.drive(distance)
        self.vehicle.refuel(refuel)
        expected = self.fuel - (self.fuel_consumption * distance) + refuel
        # fuel quantity after refuel()
        self.assertEqual(expected, self.vehicle.fuel)

    def test_refuel_when_quantity_is_invalid_expect_raises(self):
        quantity = 100
        message = 'Too much fuel'
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(quantity)
        self.assertEqual(message, str(ex.exception))

    # __str__()
    def test_str_method_expect_correct_values(self):
        expected = f"The vehicle has {self.horse_power} horse power with {self.fuel} fuel left and {self.fuel_consumption} fuel consumption"
        self.assertEqual(expected, str(self.vehicle))
