import logging


class Discount:
    def __init__(self, value):
        if not isinstance(value, float | int):
            logging.error("Invalid discount value type")
            raise TypeError("value must be a float or an integer")
        if not 0 <= value <= 1:
            logging.error("Discount value out of range")
            raise ValueError("value must be between 0 and 1")
        self.__value = value

    def discount(self):
        logging.warning("Calling abstract method discount() in Discount class")
        raise NotImplementedError("Subclass must implement this method")

    def get_value(self):
        return self.__value


class RegularDiscount(Discount):
    def __init__(self, value=0.1):
        super().__init__(value)

    def discount(self):
        return self.get_value()


class SilverDiscount(Discount):
    def __init__(self, value=0.15):
        super().__init__(value)

    def discount(self):
        return self.get_value()


class GoldDiscount(Discount):
    def __init__(self, value=0.2):
        super().__init__(value)

    def discount(self):
        return self.get_value()