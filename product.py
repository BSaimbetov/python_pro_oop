class Product:

    def __init__(self, name: str, price: int | float):
        if price <= 0:
            raise ValueError("The price of the item must be greater than zero.")
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}: {self.price}'