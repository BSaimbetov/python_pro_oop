import logging
from product import Product


class Cart:
    def __init__(self):
        self.__products = []
        self.__quantity = []
        self.__index = 0

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index < len(self.__products):
            product = self.__products[self.__index]
            quantity = self.__quantity[self.__index]
            self.__index += 1
            return f"{product.name} x {quantity}"
        else:
            raise StopIteration

    def __iadd__(self, other):
        if isinstance(other, Cart):
            self.__products.extend(other.__products)
            self.__quantity.extend(other.__quantity)
            return self
        else:
            raise TypeError(f"Unsupported operand type(s) for +=: 'Cart' and {type(other)}")

    def add_product(self, product: Product, quantity: int | float = 1):
        if quantity < 0:
            raise ValueError("The quantity of the product must be greater than zero.")

        self.__products.append(product)
        self.__quantity.append(quantity)
        logging.info(f"Product '{product.name}' added in quantity of {quantity} pieces.")

    def remove_product(self, product: Product, quantity: int | float = 1):

        if product in self.__products:
            index = self.__products.index(product)
            self.__quantity[index] -= quantity
            if self.__quantity[index] <= 0:
                del self.__products[index]
                del self.__quantity[index]
        logging.info(f"Product '{product.name}' removed from the cart.")

    def total(self):
        total = 0
        for product, quantity in zip(self.__products, self.__quantity):
            total += product.price * quantity
        return total

    def __str__(self):
        if not self.__products:
            return 'Cart is empty'
        return '\n'.join(map(lambda item: f'{item[0]} x {item[1]} = {item[0].price * item[1]} UAH',
                             zip(self.__products, self.__quantity))) + f'\nTotal: {self.total()} UAH'
