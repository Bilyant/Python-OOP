class Customer:
    CUSTOMER_ID = 1

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = self.CUSTOMER_ID
        Customer.CUSTOMER_ID += 1

    @staticmethod
    def get_next_id():
        return Customer.CUSTOMER_ID

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
