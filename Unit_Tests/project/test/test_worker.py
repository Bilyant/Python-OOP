from unittest import TestCase, main

from project.worker import Worker


class TestWorker(TestCase):
    NAME = 'Worker'
    SALARY = 100
    ENERGY = 1
    MONEY = 0
    ENERGY_DECREASE = 1
    ENERGY_INCREASE = 1

    def setUp(self) -> None:
        self.worker = Worker(self.NAME, self.SALARY, self.ENERGY)

    def test_init__expect_valid_values(self):
        self.assertEqual(self.worker.name, self.NAME)
        self.assertEqual(self.worker.salary, self.SALARY)
        self.assertEqual(self.worker.energy, self.ENERGY)
        self.assertEqual(self.worker.money, self.MONEY)

    def test_work__when_no_energy__expect_to_raise(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as context:
            self.worker.work()

        self.assertIsNotNone(context.exception)
        self.assertEqual('Not enough energy.', str(context.exception))
        self.assertEqual(0, self.worker.energy)

    def test_work__when_has_energy__expect_energy_decrease_and_money_increase(self):
        self.worker.work()
        self.assertEqual(self.worker.money, self.MONEY + self.SALARY)
        self.assertEqual(self.worker.energy, self.ENERGY - self.ENERGY_DECREASE)

    def test_rest__expect_energy_increase(self):
        self.worker.rest()
        self.assertEqual(self.worker.energy, self.ENERGY + self.ENERGY_INCREASE)

    def test_get_info__expect_correct_info(self):
        expected = f'{self.NAME} has saved {self.MONEY} money.'
        self.assertEqual(self.worker.get_info(), expected)


if __name__ == '__main__':
    main()
