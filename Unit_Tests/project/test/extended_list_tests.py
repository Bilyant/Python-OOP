from unittest import TestCase

from project.extended_list import IntegerList


class TestExtendedList(TestCase):
    def test_is_init_correctly_without_data_expect_empty_data(self):
        integer = IntegerList()
        self.assertEqual([], integer._IntegerList__data)

    def test_is_init_correctly_with_wrong_data_expect_empty_data(self):
        integer = IntegerList('asd')
        self.assertEqual([], integer._IntegerList__data)

    def test_is_init_correctly_with_correct_data_expect_integers_in_data(self):
        integer = IntegerList(1, 2, 3)
        self.assertEqual([1, 2, 3], integer._IntegerList__data)

    def test_get_data_expect_correct_data(self):
        integer = IntegerList(1, 2, 3)
        self.assertEqual([1, 2, 3], integer._IntegerList__data)
        self.assertEqual([1, 2, 3], integer.get_data())

    def test_add_method_with_wrong_data_expect_raises(self):
        integer = IntegerList()
        with self.assertRaises(ValueError) as ex:
            integer.add('asd')
        expected_error_message = 'Element is not Integer'
        self.assertEqual(expected_error_message, str(ex.exception))

    def test_add_method_with_correct_data_expect_to_append_correctly(self):
        integer = IntegerList(5)
        integer.add(10)
        self.assertEqual([5, 10], integer._IntegerList__data)

    def test_remove_index_when_correct_index_expect_to_remove_element(self):
        integer = IntegerList(5, 10)
        integer.remove_index(0)
        self.assertEqual([10], integer._IntegerList__data)
        integer.remove_index(0)
        self.assertEqual([], integer._IntegerList__data)

    def test_remove_index_when_invalid_index_expect_raises(self):
        integer = IntegerList()
        with self.assertRaises(IndexError) as ex:
            integer.remove_index(0)
        ex_message = 'Index is out of range'
        self.assertEqual(ex_message, str(ex.exception))
        self.assertEqual([], integer._IntegerList__data)

    def test_remove_index_returns_correct_value_when_valid_index(self):
        integer = IntegerList(5, 10, 20)
        result = integer.remove_index(1)
        self.assertEqual(result, 10)

    def test_insert_method_when_invalid_idx_expect_raises(self):
        integer = IntegerList(5, 10)
        with self.assertRaises(IndexError) as ex:
            integer.insert(2, 15)
        message = 'Index is out of range'
        self.assertEqual(message, str(ex.exception))

    def test_insert_method_when_valid_idx_with_invalid_data_type_expect_raises(self):
        integer = IntegerList(5, 10)
        with self.assertRaises(ValueError) as ex:
            integer.insert(1, '15')
        message = 'Element is not Integer'
        self.assertEqual(message, str(ex.exception))

    def test_insert_method_when_valid_idx_and_valid_data_expect_to_add_new_element(self):
        integer = IntegerList(5, 10)
        integer.insert(0, 20)
        self.assertEqual([20, 5, 10], integer._IntegerList__data)

    def test_biggest_expect_biggest_num(self):
        integer = IntegerList(5, 10, 50, 100)
        biggest_n = integer.get_biggest()
        self.assertEqual(biggest_n, integer.get_biggest())

    def test_get_index_expect_correct_index(self):
        integer = IntegerList(5, 10, 50, 100)
        self.assertEqual(0, integer.get_index(5))
        self.assertEqual(3, integer.get_index(100 ))
