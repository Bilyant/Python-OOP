from Inheritance.Shop.drink import Drink
from Inheritance.Shop.food import Food
from Inheritance.Shop.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def get_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        product = self.get_product(product_name)
        if product is not None:
            return product

    def remove(self, product_name):
        product = self.get_product(product_name)
        if product is not None:
            if product in self.products:
                self.products.remove(product)

    def __repr__(self):
        output = []
        for product in self.products:
            output.append(f"{product.name}: {product.quantity}")
        return '\n'.join(output)


food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)
