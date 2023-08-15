from unittest import TestCase, main

from project.cat import Cat


class TestCar(TestCase):
    NAME = 'CAT'
    FED = False
    SLEEPY = False
    SIZE = 0

    def setUp(self) -> None:
        self.cat = Cat(self.NAME)

    def test_init__expect_valid_values(self):
        self.assertEqual(self.cat.name, self.NAME)
        self.assertEqual(self.cat.fed, self.FED)
        self.assertEqual(self.cat.sleepy, self.SLEEPY)
        self.assertEqual(self.cat.size, self.SIZE)

    def test_eat__when_fed_is_true__expect_to_raise(self):
        self.cat.fed = True
        expected_error_message = 'Already fed.'

        with self.assertRaises(Exception) as context:
            self.cat.eat()

        self.assertIsNotNone(context.exception)
        self.assertEqual(str(context.exception), expected_error_message)

    def test_eat__when_fed_is_false__expect_fed_and_sleepy_true_and_size_increase(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(self.cat.size, self.cat.size)

    def test_sleep__when_fed_is_false__expect_to_raise(self):
        expected_error_message = 'Cannot sleep while hungry'

        with self.assertRaises(Exception) as context:
            self.cat.sleep()

        self.assertIsNotNone(context.exception)
        self.assertEqual(str(context.exception), expected_error_message)

    def test_sleep__when_fed_is_true__expect_sleepy_false(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__name__':
    main()
