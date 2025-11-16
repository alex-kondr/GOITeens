import  concurrent.futures
import time
import logging
from random import randint
import math


logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')


# numbers = list(range(1, 101))
# logging.debug(f"{numbers = }")


def get_number(id: int):
    logging.debug(f"Беремо число під номером '{id}'")
    time_sleep = randint(0, 3)
    logging.debug(f"{time_sleep = }")
    time.sleep(time_sleep)
    return f"Повернули чисто '{id}'"


PRIMES = [
    1122725350952933541,
    1125827059421714511,
    1122725350952937811,
    1152800951907739811,
    1157978480770991422,
    10997268992854190033
]

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":

    # with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        logging.debug("Починаємо перебирати числа")
        # result = list(executor.map(get_number, numbers))
        # logging.debug(result)
        for number, result in zip(PRIMES, executor.map(is_prime, PRIMES)):
            logging.debug(f"Число '{number}' просте: {result}")

    logging.debug("The end!!!")
