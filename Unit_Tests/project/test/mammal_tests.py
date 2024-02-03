from unittest import TestCase

from Tasks.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal('some_name', 'some_type', 'some_sound')

    # __init__()
    def test_init_works_as_expected(self):
        self.assertEqual('some_type', self.mammal.type)
        self.assertEqual('some_sound', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    # make_sound()
    def test_make_sound_returns_correct_value(self):
        expected = 'some_name makes some_sound'
        self.assertEqual(expected, self.mammal.make_sound())

    # get_kingdom()
    def test_get_kingdom_returns_correct_value(self):
        self.assertEqual(self.mammal.get_kingdom(), self.mammal._Mammal__kingdom)

    # info
    def test_info_returns_correct_value(self):
        expected = "some_name is of type some_type"
        self.assertEqual(expected, self.mammal.info())
