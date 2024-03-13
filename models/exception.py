class InvalidDiscountValue(Exception):
    def __init__(self, name, discount_value):
        print(f"Invalid discount value for client {name}: {discount_value}")