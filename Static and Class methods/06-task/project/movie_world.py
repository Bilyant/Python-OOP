from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    """
    If the customer has already rented that DVD return "{customer_name} has already rented {dvd_name}"
    If the DVD is rented by someone else, return "DVD is already rented"
    If the customer is not allowed to rent the DVD, return 
    "{customer_name} should be at least {dvd_age_restriction} to rent this movie"
    Otherwise, the rent is successful (the DVD is rented and added to the customer's DVDs). Return 
    "{customer_name} has successfully rented {dvd_name}"
    """
    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = [c for c in self.customers if c.id_number == customer_id][0]
        dvd = [d for d in self.dvds if d.id_number == dvd_id][0]
        if dvd in customer.rented_dvds:
            return f'{customer.name} has already rented {dvd.name}'
        if dvd.is_rented:
            return 'DVD is already rented'
        if customer.age < dvd.age_restriction:
            return f'{customer.name} should be at least {dvd.age_restriction} to rent this movie'
        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f'{customer.name} has successfully rented {dvd.name}'

    """
    if the DVD is in the customer, he/she should return it and the method should return the message 
    "{customer_name} has successfully returned {dvd_name}". Otherwise, return 
    "{customer_name} does not have that DVD" 
    """
    def return_dvd(self, customer_id, dvd_id):
        customer = [c for c in self.customers if c.id_number == customer_id][0]
        dvd = [d for d in self.dvds if d.id_number == dvd_id][0]
        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f'{customer.name} has successfully returned {dvd.name}'
        return f'{customer.name} does not have that DVD'

    def __repr__(self):
        result = [repr(c) for c in self.customers] + [repr(d) for d in self.dvds]
        return '\n'.join(result)
