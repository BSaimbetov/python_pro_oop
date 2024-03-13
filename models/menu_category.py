from models.dish import Dish

from logging_config import logger


class Category:
    def __init__(self, name: str):
        self.name = name
        self.__dishes = []
        logger.info(f"New category created: {self.name}")

    def add_dish(self, dish: Dish):
        self.__dishes.append(dish)
        logger.info(f"Dish '{dish.name}' added to category {self.name}")

    def __str__(self):
        return f'{self.name}:\n     ' + '\n     '.join(map(str, self.__dishes))


class Menu:
    def __init__(self):
        self.__categories = []
        logger.info("New menu created")

    def add_category(self, category: Category):
        self.__categories.append(category)
        logger.info(f"Category '{category.name}' added to menu")

    def __iter__(self):
        return iter(self.__categories)

    def __getitem__(self, index):
        return self.__categories[index]

    def __str__(self):
        return '\n'.join(map(str, self.__categories))
