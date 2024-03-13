import logging
from product import Product
from cart import Cart

logging.basicConfig(level=logging.INFO, format='%(message)s')

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


if __name__ == '__main__':

    product1 = Product('Milk', 25)
    product2 = Product("Bread", 10)
    product3 = Product("Eggs", 20)
    product4 = Product("Cheese", 30)
    product5 = Product("Potato", 10)

    cart1 = Cart()
    cart2 = Cart()

    try:
        quantity1 = int(input(f"Enter the quantity of '{product1.name}': "))
        quantity2 = int(input(f"Enter the quantity of '{product2.name}': "))
        quantity3 = int(input(f"Enter the quantity of '{product3.name}': "))
        quantity4 = int(input(f"Enter the quantity of '{product4.name}': "))
        quantity5 = int(input(f"Enter the quantity of '{product5.name}': "))

        cart1.add_product(product1, quantity1)
        cart1.add_product(product2, quantity2)
        cart1.add_product(product3, quantity3)

        cart2.add_product(product4, quantity4)
        cart2.add_product(product5, quantity5)

        cart1 += cart2
        print()
        logging.info("")

    except ValueError:
        print("Error: Please enter a valid quantity of the product.")

    print(cart1)