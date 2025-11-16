import concurrent.futures
import math

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419
]

def is_prime(n):
    """
    Функція для перевірки, чи є число простим.
    Це CPU-bound завдання.
    """
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

if __name__ == '__main__':
    print("Початок перевірки чисел на простоту...")
    # Створення ProcessPoolExecutor з 4 робочими процесами
    with concurrent.futures.ProcessPoolExecutor(4) as executor:
        # Використання map для паралельного виконання is_prime для кожного числа
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print(f'{number} є простим: {prime}')
    print("Завершення перевірки.")