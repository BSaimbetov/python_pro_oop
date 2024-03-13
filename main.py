from models.menu_category import Category, Menu
from models.client import Client
from models.dish import Dish

from logging_config import logger

if __name__ == '__main__':
    try:
        # Створення екземплярів страв та категорій меню
        dish_1 = Dish("Caesar Salad", 10)
        dish_2 = Dish("Vegetable Salad", 8.5)
        dish_3 = Dish("Spaghetti Carbonara", 12)
        dish_4 = Dish("Soup", 10)
        dish_5 = Dish("Cheesecake", 6)
        dish_6 = Dish("Taramisu", 7)

        category1 = Category("Appetizers")
        category2 = Category("Main Dishes")
        category3 = Category("Deserts")

        category1.add_dish(dish_1)
        category1.add_dish(dish_2)
        category2.add_dish(dish_3)
        category2.add_dish(dish_4)
        category3.add_dish(dish_5)
        category3.add_dish(dish_6)


        # print(f"{category1}\n")
        # print(f"{category2}\n")
        # print(f"{category3}\n")

        menu = Menu()
        menu.add_category(category1)
        menu.add_category(category2)
        menu.add_category(category3)

        for category in menu:
            print(category)

        standard = 0
        regular = 0.1
        silver = 0.15
        gold = 0.2

        # Створення клієнта з карткою лояльності
        clients = [
            Client("John", discount_value=gold),
            Client("Alice", discount_value=regular),
            Client("Tom", discount_value=silver)
        ]
        orders = [
            [dish_1, dish_3, dish_5],
            [dish_4, dish_6],
            [dish_2, dish_4, dish_6]
        ]
        for client, order in zip(clients, orders):
            for dish in order:
                client += dish

        # Выводим рахунки
        max_name_length = max(len(client.name) for client in clients)
        print(f"{'\nClient':<{max_name_length + 2}}Total price")
        print('-' * (max_name_length + 14))
        for client in clients:
            print(f"{client.name:<{max_name_length + 2}}${client.get_total_price():.2f}")

        print(f'\n{menu[0]}')

    except Exception as e:
        logger.exception("An unexpected error occurred")
