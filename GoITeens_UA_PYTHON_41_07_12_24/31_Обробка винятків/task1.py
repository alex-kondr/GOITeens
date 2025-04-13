# Приклад 1
# Припустимо, що ви розробляєте програму, яка потребує
# введення числових значень. Якщо користувач помилково
# вводить текст замість числа, виникає виняток ValueError.
# Обробимо цю ситуацію, щоб програма не завершилася з помилкою.

# number = input("Введіть ціле число: ")

# try:
#     number = int(number)
#     print(number - 9)

# # except:
# #     pass

# except ValueError as e:
#     print("Ви ввели невірне число", e)










# Приклад 2
# Розглянемо ситуацію, коли вам потрібно відкрити
# файл для читання. Якщо файл не існує, Python викличе
# виняток FileNotFoundError. Використаємо try-except,
# щоб обробити цю ситуацію.

# try:
#     file = open("test.txt")
#     txt = file.read()

# except FileNotFoundError as e:
#     print("Файл не знайдено!")

# finally:
#     try:
#         file.close()
#         print("Файл успішно закритий.")

#     except NameError:
#         print("Немає що закривати")

# print("Hello")

# try:
#     with open("test.txt") as file:
#         txt = file.read()

# except FileNotFoundError:
#     print("Файл не знайдено!")











# Приклад 3
# Іноді одна частина коду може викликати кілька
# різних винятків. Ви можете обробляти їх окремо,
# використовуючи кілька блоків except. Це дозволяє
# вам надавати різні повідомлення або виконувати різні
# дії залежно від типу помилки.(розглянемо це більш детально далі)

# try:
#     value = int(input("Введіть ціле число: "))
#     print(f" 5 / {value} = {5 / value}")

# except ValueError as e:
#     print("Ви ввели невірне число. Введіть ціле число")

# except ZeroDivisionError as e:
#     print("На нуль ділити неможна")










# Розглянемо інший приклад, розробник 1
# розробляє програму, яка відкриває файл,
# читає з нього дані та ділить одне число з
# файлу на інше. Тут можуть виникати різні
# помилки, наприклад, файл може не існувати,
# або може бути спроба ділення на нуль.

# try:
#     with open("number.txt") as file:
#         number = file.read()

#     number = int(number)

#     print(8 / number)

# except FileNotFoundError:
#     print("Файл 'number.txt' не знайдено.")
# except ValueError:
#     print("Помилка: вміст файлу не є числом.")
# except ZeroDivisionError:
#     print("Помилка: не можна ділити на нуль.")








# Інший поширений сценарій виникнення різних
# помилок - робота зі списками. Якщо ви намагаєтеся
# отримати доступ до елементу за індексом,
# який виходить за межі списку, виникає помилка
# IndexError. Крім того, можуть виникати інші
# винятки, які потрібно обробити окремо.

# my_list = [5, 6, 8, -7]
# index = int(input("Введіть індекс для відображення -> "))
# print(my_list[index])

# try:
#     index = int(input("Введіть індекс: "))
#     print(my_list[index])
# except IndexError:
#     print("Індекс недопустимий")
# except ValueError:
#     print("Введіть число")








# ValueError виникає, коли функція отримує правильний
# тип аргументу, але аргумент має недопустиме значення.
# Наприклад, при спробі перетворити рядок, який не містить
# чисел, на ціле число виникне ValueError.












# TypeError виникає, коли операція або
# функція застосовується до об'єкта неприпустимого
# типу. Наприклад, спроба скласти число і рядок
# викликає TypeError.

# number = input("Введіть число: ")

# print(5 - number)









# IndexError виникає, коли намагаються
# отримати доступ до елемента списку за
# індексом, що виходить за межі списку.

# index = 10

# try:
#     my_list = list(range(5))
#     print(my_list[index])
#     print("Ця частина виконається коли правильний індекс")

# except IndexError:
#     try:
#         print(my_list[index-1])
#     except:
#         print("Ви ввели занадто великий індекс")
#         print("Введіть індекс у діапазоні 0 - 4")

# else:
#     print("Програма нормально завершилась")

# finally:
#     print("Цей блок виконується завжди")











# KeyError виникає, коли спроба отримати доступ
# до ключа у словнику, якого немає в цьому словнику.
# Це може статися, коли розробник 1 передбачає
# наявність ключа, але забуває перевірити його наявність перед доступом.

# users = {
#     "alex": {
#         "name": "Alex",
#         "city": "Odesa"
#     },
#     "volodumur": {
#         "name": "Volodumur",
#         "city": "Kyiv"
#     }
# }

# try:
#     print(users["ababbabubu"])
# except KeyError:
#     print("У базі даних немає такого користувача")


# class UserNotFoundError(Exception):
#     def __init__(self, message="У базі даних немає такого користувача"):
#         self.message = message
#         super().__init__(message)


# raise UserNotFoundError("Інше повідомлення про помилку")
# raise Exception("Якась помилка")

# class NotIntegerError(Exception):
#     def __init__(self, message="Даний тип даний неможливо перетворити в ціле число"):
#         self.message = message
#         super().__init__(message)



# try:
#     number = int(number)
# except ValueError as e:
#     raise NotIntegerError()
# else:

# number = input("Введіть ціле число: ")
# if not number.isdigit():
#     raise NotIntegerError()

# print("Передаю дані в базу даних")








# ZeroDivisionError виникає, коли є спроба ділення на нуль.


# finally
# обов'язкове закриття файлу

# try:
#     file = open("file.txt")
# except FileNotFoundError:
#     print("Файл не знайдено")
# finally:
#     try:
#         file.close()
#     except NameError:
#         pass
# import io

# try:
#     file = open("file.txt", "r")
#     file.write("Хочу записати текст")
# except io.UnsupportedOperation as e:
#     print("Файл відкритий на читання")
# finally:
#     try:
#         file.close()
#         print("Робота з файлом завершена")
#     except NameError:
#         print("Файл не існує")





import logging


logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s", filename="log_file.txt", encoding="utf-8")


def read_file(file_name):
    try:
        with open(file_name, 'r') as f:
            logging.info(f"Читання файлу: {file_name}")
            return f.write()
    except FileNotFoundError as e:
        logging.error(f"Файл не знайдено: {file_name}", exc_info=True)
    except Exception as e:
        logging.critical("Невідома помилка!", exc_info=True)


read_file("file.txt")












# Підняття винятків (raise)






# Завдання 1
# Розробіть функцію, яка намагається відкрити
# файл для читання. Якщо файл не існує, підніміть
# виняток FileNotFoundError і обробіть його, вивівши
# повідомлення про помилку. Якщо файл існує,
# прочитайте його вміст і виведіть на екран.
# Незалежно від того, чи виникла помилка,
# переконайтеся, що файл буде закритий.










# Завдання 2
# Розробіть функцію, яка приймає два числа як
# аргументи та виконує їх ділення. Якщо друге
# число дорівнює нулю, підніміть виняток ZeroDivisionError
# і обробіть його, вивівши повідомлення про помилку.
# Якщо один із аргументів не є числом, підніміть виняток
# TypeError і також обробіть його.








# Завдання за бажанням 3(додаткове)
# Розробіть функцію, яка перевіряє пароль на
# відповідність певним критеріям. Якщо пароль
# не відповідає вимогам (наприклад, менше 8 символів,
# немає цифр), підніміть відповідний виняток.
# Обробіть кожен тип помилки окремо, щоб повідомити
# користувача про конкретну проблему.

