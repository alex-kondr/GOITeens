def out_func(x):
    def in_func(y):
        return x + y
    return in_func


# plus_5 = out_func(5)
# print(plus_5(50))



def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner


# my_counter = counter()
# my_counter()
# print(my_counter())

# my_counter()
# my_counter()
# my_counter()

# print(my_counter())

def bank(init_balance):
    balance = init_balance
    def get_balance():
        return balance
    def add_funds(amount):
        nonlocal balance
        balance += amount
    return get_balance, add_funds


import time


def timer():
    start = time.time()
    def end():
        return time.time() - start
    return end


# my_timer = timer()
# time.sleep(5)
# print(my_timer())


def my_logger(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"Старт програми: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Час виконання: {time.time() - start}")
        return result
    return wrapper


@my_logger
def say_hello(a, b):
    print("Hello")


say_hello(1, 2)