import logging

# Отримуємо логгер
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Форматування для повідомлень
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

# Обробник для запису в файл
file_handler = logging.FileHandler('main.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

# Обробник для виводу в консоль
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)

# Додаємо обробники до логгера
logger.addHandler(file_handler)
logger.addHandler(console_handler)
