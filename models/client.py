import uuid

from models.dish import Dish
from models.exception import InvalidDiscountValue
from models.discount import Discount, RegularDiscount, SilverDiscount, GoldDiscount

from logging_config import logger


class Client:
    def __init__(self, name, discount_value: float = 0):
        try:
            if discount_value not in [0, 0.1, 0.15, 0.2]:
                raise InvalidDiscountValue("Invalid discount value")
        except InvalidDiscountValue as e:
            logger.error(f"Invalid discount value for client {name}: {discount_value}")
            raise e

        if discount_value == 0:
            self.discount = Discount(0)
        elif discount_value == 0.1:
            self.discount = RegularDiscount()
        elif discount_value == 0.15:
            self.discount = SilverDiscount()
        else:
            self.discount = GoldDiscount()

        self.id = uuid.uuid4()
        self.name = name
        self.order = {}
        logger.info(f"New client created: {self.name}, ID: {self.id}")

    def add_dish(self, dish: Dish, quantity: int = 1):
        if not isinstance(dish, Dish):
            logger.error(f"Invalid dish type: {type(dish)}")
            raise TypeError("Dish must be an instance of Dish class")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be a number")
        if quantity <= 0:
            logger.error(f"Invalid quantity value: {quantity}")
            raise ValueError("Quantity must be a positive integer")

        if dish in self.order:
            self.order[dish] += quantity
        else:
            self.order[dish] = quantity
        logger.info(f"{quantity}x {dish.name} added to order of client {self.name}")

    def get_total_price(self):
        total = sum(dish.price * quantity for dish, quantity in self.order.items())
        discount_percentage = self.discount.discount()
        return total * (1 - discount_percentage)

    def __str__(self):
        items = [f'{dish.name}x{quantity}={dish.price * quantity}' for dish, quantity in self.order.items()]
        return '\n'.join(items)

    def __iadd__(self, dish):
        self.add_dish(dish)
        return self

