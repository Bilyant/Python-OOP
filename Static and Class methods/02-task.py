class Shop:
    SMALL_SHOP_CAPACITY = 10

    def __init__(self, name: str, type: str, capacity: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}  # name of an item and its quantity

    @classmethod
    def small_shop(cls, name: str, type: str):
        return cls(name, type, capacity=Shop.SMALL_SHOP_CAPACITY)

    """
    adds 1 to the quantity of the given item. On success, the method should return 
    "{item_name} added to the shop". If the addition is not possible, the following message 
    should be returned "Not enough capacity in the shop"
    """

    def add_item(self, item_name: str):
        # if len(self.items) >= self.capacity:
        if sum(self.items.values()) >= self.capacity:
            return 'Not enough capacity in the shop'
        if item_name not in self.items:
            self.items[item_name] = 0
        self.items[item_name] += 1
        return f'{item_name} added to the shop'

    """
    removes the given amount from the item. On success, it should return 
    "{amount} {item_name} removed from the shop". Otherwise, the method should return 
    "Cannot remove {amount} {item_name}"
    """

    def remove_item(self, item_name: str, amount: int):
        if item_name in self.items:
            if self.items[item_name] >= amount:
                self.items[item_name] -= amount
                return f'{amount} {item_name} removed from the shop'
        return f'Cannot remove {amount} {item_name}'

    def __repr__(self):
        return f'{self.name} of type {self.type} with capacity {self.capacity}'


fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)

print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))

print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
