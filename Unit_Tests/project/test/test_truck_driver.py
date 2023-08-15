from typing import Dict
from unittest import TestCase, main

from project.truck_driver import TruckDriver


class TestTruckDriver(TestCase):
    NAME: str = 'Person'
    MONEY_PER_MILE: float = 10
    AVAILABLE_CARGOS: Dict[str, int] = {}
    EARNED_MONEY: float = 0
    MILES: int = 0

    def setUp(self) -> None:
        self.truck_driver = TruckDriver(self.NAME, self.MONEY_PER_MILE)

    def test_init__expect_correct_values(self):
        self.assertEqual(self.truck_driver.name, self.NAME)
        self.assertEqual(self.truck_driver.money_per_mile, self.MONEY_PER_MILE)
        self.assertEqual(self.truck_driver.available_cargos, self.AVAILABLE_CARGOS)
        self.assertEqual(self.truck_driver.earned_money, self.EARNED_MONEY)
        self.assertEqual(self.truck_driver.miles, self.MILES)

    # def test_earned_money__when_correct__expect_valid_value(self):
    #     self.truck_driver.earned_money = 100
    #
    #     self.assertEqual(self.truck_driver.earned_money, 100)

    def test_earned_money__when_negative__expect_raises(self):
        expected_error_message = f"{self.truck_driver.name} went bankrupt."
        with self.assertRaises(ValueError) as context:
            self.truck_driver.earned_money = -1

        self.assertIsNotNone(context.exception)
        self.assertEqual(str(context.exception), expected_error_message)

    def test_add_cargo_offer__when_cargo_not_added__expect_new_item_in_cargo_offer(self):
        # self.AVAILABLE_CARGOS['Location'] = 100
        expected_result = "Cargo for 100 to Location was added as an offer."
        result = self.truck_driver.add_cargo_offer(cargo_location='Location', cargo_miles=100)

        self.assertEqual(self.truck_driver.available_cargos, {'Location': 100})
        self.assertEqual(result, expected_result)

    def test_add_cargo_offer__when_cargo_already_added__expect_raises(self):
        self.truck_driver.add_cargo_offer(cargo_location='Location', cargo_miles=100)
        expected_error_message = "Cargo offer is already added."

        with self.assertRaises(Exception) as context:
            self.truck_driver.add_cargo_offer(cargo_location='Location', cargo_miles=100)

        self.assertIsNotNone(context.exception)
        self.assertEqual(str(context.exception), expected_error_message)

    def test_drive_best_cargo_offer__when_no_offers__expect_raises(self):
        expected_error_message = "There are no offers available."
        result = self.truck_driver.drive_best_cargo_offer()

        self.assertEqual(result, expected_error_message)

    def test_drive_best_cargo_offer__when_offer_available__expect_valid_result(self):
        self.truck_driver.add_cargo_offer('Location', 100)
        self.truck_driver.add_cargo_offer('Location2', 200)
        result = self.truck_driver.drive_best_cargo_offer()
        expected_result_message = "Person is driving 200 to Location2."

        self.assertEqual(self.truck_driver.earned_money, 2000)
        self.assertEqual(self.truck_driver.miles, 200)
        self.assertEqual(result, expected_result_message)

    def test_eat(self):
        self.truck_driver.earned_money = 100
        self.truck_driver.eat(250)
        expected_money = 80
        self.assertEqual(self.truck_driver.earned_money, expected_money)

    def test_sleep(self):
        self.truck_driver.earned_money = 100
        self.truck_driver.sleep(1000)
        expected_money = 55
        self.assertEqual(self.truck_driver.earned_money, expected_money)

    def test_pump_gas(self):
        self.truck_driver.earned_money = 1000
        self.truck_driver.pump_gas(1500)
        expected_money = 500
        self.assertEqual(self.truck_driver.earned_money, expected_money)

    def test_repair_truck(self):
        self.truck_driver.earned_money = 10000
        self.truck_driver.repair_truck(10000)
        expected_money = 2500
        self.assertEqual(self.truck_driver.earned_money, expected_money)

    def test_repr_(self):
        actual_result = str(self.truck_driver)
        actual_result2 = repr(self.truck_driver)
        expected_result = f"{self.NAME} has {self.MILES} miles behind his back."

        self.assertEqual(actual_result, expected_result)
        self.assertEqual(actual_result2, expected_result)

    def test_check_for_activities(self):
        pass


if __name__ == '__main__':
    main()
