import logging
from product import Product
from cart import Cart

logging.basicConfig(level=logging.INFO, format='%(message)s')

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
    print()
    for item in cart1:
        print(item)