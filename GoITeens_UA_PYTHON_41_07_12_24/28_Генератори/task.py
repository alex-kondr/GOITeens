#  Генераторна функція
# def test_generator():







# Генераторний вираз
# 1. Напишіть генератор, який повертає квадрати чисел від 1 до N.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]






# def countdown(n):








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
