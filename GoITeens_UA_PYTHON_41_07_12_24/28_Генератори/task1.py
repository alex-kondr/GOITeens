# generator = iter(range(5))
# next(generator)
# print(next(generator))
#  Генераторна функція
# def test_generator():
#     yield 5
#     yield 6
#     yield 7


# generator = test_generator()
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))

# for number in test_generator():
#     print(number)



# Генераторний вираз
# 1. Напишіть генератор, який повертає квадрати чисел від 1 до N.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# generator = (number ** 2 for number in numbers)

# print(next(generator))

# # 
# # 
# # 
# print(next(generator))








# def countdown(n):
#     count = n
#     while count >= 0:
#         yield count
#         count -= 1

# def generator(n):
#     count = n
#     while True:
#         yield count
#         if count == 0:
#             break
#         count -= 1


# my_generator = generator(10)


# for number in my_generator:
#     print(number)



# h

def prime_generator():
    prime_number = 2
    while True:
        for i in range(2, prime_number):
            if prime_number % i == 0:
                prime_number += 1
                break
        else:
            yield prime_number
            prime_number += 1


prime_number = prime_generator()

for i in prime_number:
    print(i)

# print(next(prime_number))
# print(next(prime_number))
# print(next(prime_number))
# print(next(prime_number))
# print(next(prime_number))
# print(next(prime_number))


# Генерувати нескінченну послідовність починаючи з певного числа








# Обчислення суми усіх парних чисел у списку









# Виведення всіх унікальних слів з тексту у верхньому регістрі










# def simple_generator():
#     message = yield "Ready"
#     yield f"Received: {message}"


# gen = simple_generator()
# print(next(gen))
# print(gen.send("Hello"))








# def generator_with_exception():
#     try:
#         yield "Doing fine"
#         raise Exception("Something went wrong")
#     except Exception as e:
#         yield f"Handling exception: {e}"


# gen = generator_with_exception()
# print(next(gen))
# print(next(gen))










# def infinite_generator():
#     try:
#         while True:
#             yield "Running..."
#     except GeneratorExit:
#         yield "Closing..."


# gen = infinite_generator()
# print(next(gen))
# gen.close()
# try:
#     print(next(gen))
# except StopIteration as e:
#     print("Generator is closed") # Generator is closed






# Напишіть генератор, що виробляє числа Фібоначчі.
# Генератор має повертати послідовність чисел Фібоначчі від першого до N-го.









# Створіть генератор, який для заданого
# списку чисел повертає квадрат кожного числа.











# Створіть генератор, що виробляє нескінченну
# послідовність парних чисел, починаючи з нуля.








# Напишіть генератор, який приймає список і зміщення,
# і повертає кожен елемент списку, збільшений на вказане зміщення.







# Генерація випадкових чисел у заданому діапазон.
# Використовуючи модуль random, створіть генератор,
# що виробляє випадкові числа в заданому діапазоні (від min до max) до N-го числа.
