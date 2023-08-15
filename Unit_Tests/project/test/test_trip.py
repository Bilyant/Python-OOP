from project.trip import Trip

from unittest import TestCase, main


class TestTrip(TestCase):
    BUDGET = 1000
    TRAVELERS = 5
    IS_FAMILY = True
    BOOKED_DESTINATIONS_PAID_AMOUNT = {}

    def setUp(self) -> None:
        self.travellers = Trip(self.BUDGET, self.TRAVELERS, self.IS_FAMILY)

    def test_destination_prices_per_person_expect_correct_values(self):
        self.assertEqual(self.travellers.DESTINATION_PRICES_PER_PERSON.get('New Zealand'), 7500)
        self.assertEqual(self.travellers.DESTINATION_PRICES_PER_PERSON.get('Australia'), 5700)
        self.assertEqual(self.travellers.DESTINATION_PRICES_PER_PERSON.get('Brazil'), 6200)
        self.assertEqual(self.travellers.DESTINATION_PRICES_PER_PERSON.get('Bulgaria'), 500)

        for country in self.travellers.DESTINATION_PRICES_PER_PERSON.keys():
            self.assertEqual(country, country)

    def test_init(self):
        self.assertEqual(self.travellers.budget, self.BUDGET)
        self.assertEqual(self.travellers.travelers, self.TRAVELERS)
        self.assertEqual(self.travellers.is_family, self.IS_FAMILY)
        self.assertEqual(self.travellers.booked_destinations_paid_amounts, self.BOOKED_DESTINATIONS_PAID_AMOUNT)

    def test_travellers_getter_when_no_travellers_expect_value_error(self):

        with self.assertRaises(ValueError) as context:
            self.travellers = Trip(self.BUDGET, is_family=self.IS_FAMILY, travelers_number=0)

        self.assertIsNotNone(context.exception)
        self.assertEqual('At least one traveler is required!', str(context.exception))

    def test_is_family_setter_when_less_than_2_expect_is_family_false(self):
        self.travellers = Trip(self.BUDGET, is_family=self.IS_FAMILY, travelers_number=1)

        self.assertEqual(self.travellers.is_family, False)

    def test_book_a_trip_when_destinations_invalid__expect_invalid_destination_message(self):
        result = self.travellers.book_a_trip('Romania')

        self.assertEqual(result, 'This destination is not in our offers, please choose a new one!')

    def test_book_a_trip_when_destinations_valid_when_is_family_true_and_when_enough_budget(self):
        self.travellers = Trip(budget=20000, is_family=self.IS_FAMILY, travelers_number=3)
        result = self.travellers.book_a_trip('Brazil')
        budget_left = 3260

        self.assertEqual(self.travellers.booked_destinations_paid_amounts['Brazil'], 16740)
        self.assertEqual(self.travellers.budget, 3260)
        self.assertEqual(result, f'Successfully booked destination Brazil! Your budget left is {budget_left:.2f}')

    def test_book_a_trip_when_destinations_valid_when_is_family_true_and_when_not_enough_budget(self):
        self.travellers = Trip(budget=15000, is_family=self.IS_FAMILY, travelers_number=3)
        result = self.travellers.book_a_trip('Brazil')

        self.assertIsNone(self.travellers.booked_destinations_paid_amounts.get('Brazil'))
        self.assertEqual(result, 'Your budget is not enough!')

    def test_book_a_trip_when_destinations_valid_when_is_family_false_and_when_enough_budget(self):
        self.travellers = Trip(budget=20000, is_family=self.IS_FAMILY, travelers_number=1)
        result = self.travellers.book_a_trip('Brazil')
        budget_left = 13800

        self.assertEqual(self.travellers.booked_destinations_paid_amounts['Brazil'], 6200)
        self.assertEqual(self.travellers.budget, 13800)
        self.assertEqual(result, f'Successfully booked destination Brazil! Your budget left is {budget_left:.2f}')

    def test_book_a_trip_when_destinations_valid_when_is_family_false_and_when_not_enough_budget(self):
        self.travellers = Trip(budget=2000, is_family=False, travelers_number=1)
        result = self.travellers.book_a_trip('Brazil')

        self.assertEqual(self.travellers.budget, 2000)
        self.assertEqual(self.travellers.booked_destinations_paid_amounts, {})
        self.assertEqual(result, 'Your budget is not enough!')

    def test_booking_status__when_no_bookings__expect_empty_dict(self):
        result = self.travellers.booking_status()

        self.assertEqual(result, 'No bookings yet. Budget: 1000.00')

    def test_booking_status__when_bookings__expect_sorted_output_message_with_bookings_made(self):
        self.travellers = Trip(budget=50000, is_family=True, travelers_number=3)
        self.travellers.book_a_trip('Brazil')
        self.travellers.book_a_trip('Australia')
        output = ['Booked Destination: Australia', 'Paid Amount: 15390.00', 'Booked Destination: Brazil',
                  'Paid Amount: 16740.00', 'Number of Travelers: 3', 'Budget Left: 17870.00']
        output = '\n'.join(output)

        result = self.travellers.booking_status()

        self.assertEqual(result, output)


if __name__ == '__main__':
    main()
