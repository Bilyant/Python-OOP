from Inheritance.Shop.product import Product


class Food(Product):
    def __init__(self, name: str):
        super().__init__(name, quantity=15)


"""
In the food.py file, the Food class should be implemented. The class should inherit from the Product class. 
An instance of the Food class will have a name and a quantity of 15.
"""