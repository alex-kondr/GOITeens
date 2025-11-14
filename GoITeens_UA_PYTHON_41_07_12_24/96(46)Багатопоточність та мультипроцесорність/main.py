import concurrent.futures
import logging
from random import randint
from time import sleep

# Налаштування логування для демонстрації роботи потоків
logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')

def greeting(name):
    logging.debug(f'привітання для: {name}')
    sleep_count = randint(3, 10)
    sleep(sleep_count) # Імітація IO-bound роботи (наприклад, мережевий запит)
    logging.debug(f'{sleep_count = }')
    return f"Привіт {name}"

arguments = (
    "Білл",
    "Джилл",
    "Тілл",
    "Сем",
    "Том",
    "Джон",
)

if __name__ == '__main__':
    logging.debug('Початок програми')
    # Створення ThreadPoolExecutor з максимум 2 робочими потоками
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        # Використання map для паралельного виконання функції greeting для кожного аргументу
        results = list(executor.map(greeting, arguments))
        logging.debug(f'Результати: {results}')
    logging.debug('Завершення програми')