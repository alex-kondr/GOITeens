# Стиснення даних

# ПЕРЕВАГИ
# Зменшення обсягу файлів дозволяє оптимізувати використання пам'яті та зменшити витрати на зберігання.
# Компактні дані передаються швидше, що особливо важливо для роботи з великими обсягами інформації в мережах.
# Стиснення допомагає знизити вимоги до пропускної здатності та зменшити час завантаження файлів.

# ПРИКЛАДИ ЗАСТОСУВАННЯ
# Стиснення зображень, відео та аудіо для швидшого завантаження та зменшення трафіку.
# Зменшення розміру таблиць і оптимізація зберігання великих обсягів даних.
# Збереження історичних даних та резервних копій в компактному форматі для економії місця.

# import gzip

# original_text = (
#     "Стиснення без втрат дозволяє відновити оригінальні дані без будь-яких змін. "
#     "Цей приклад демонструє, як можна використовувати модуль gzip у Python для "
#     "стискання та подальшого розпаковування тексту. " * 5
# )
# data = original_text.encode('utf-8')
# compressed_data = gzip.compress(data)
# decompressed_data = gzip.decompress(compressed_data)
# decompressed_text = decompressed_data.decode('utf-8')
# print("Оригінальний розмір (байти):", len(data))
# print("Стиснутий розмір (байти):", len(compressed_data))
# print("Відновлений текст рівний оригіналу:", decompressed_text == original_text)


# ПРАКТИЧНЕ ЗАВДАННЯ 1
# Реалізуйте функцію compress_file(input_path, output_path),
# яка зчитує вміст текстового файлу за шляхом input_path і
# зберігає стиснений варіант у файл output_path за допомогою модуля gzip.
# Функція має повертати розмір стиснутого файлу.
# Проведіть тестування функції, використовуючи приклад текстового файлу.

import gzip
import os

def compress_file(input_path, output_path):
    # Відкрийте вхідний файл для читання у текстовому режимі
    # Зчитайте вміст файлу
    # Відкрийте вихідний файл через gzip для запису
    # Запишіть вміст та поверніть розмір стиснутого файлу
    pass

input_file = "test.txt"
output_file = "test.txt.gz"
compressed_size = compress_file(input_file, output_file)
print("Розмір стиснутого файлу:", compressed_size, "байт")

# Правильний код
import gzip
import os

def compress_file(input_path, output_path):
    with open(input_path, 'rb') as f_in:
        content = f_in.read()
    with gzip.open(output_path, 'wb') as f_out:
        f_out.write(content)
    return os.path.getsize(output_path)

input_file = "test.txt"
output_file = "test.txt.gz"
compressed_size = compress_file(input_file, output_file)
print("Розмір стиснутого файлу:", compressed_size, "байт")


# ПРАКТИЧНЕ ЗАВДАННЯ 2
# Реалізуйте функцію compress_text(text), яка приймає
# рядок text і повертає стиснений варіант даних за допомогою модуля zlib.
# Додатково реалізуйте функцію decompress_text(compressed),
# яка відновлює оригінальний текст із стиснутих даних.
# Проведіть тестування, перевіривши, що після декомпресії
# текст збігається з оригіналом.

import zlib

def compress_text(text):
    # Стисніть рядок text за допомогою zlib.compress і поверніть результат
    pass

def decompress_text(compressed):
    # Відновіть текст за допомогою zlib.decompress та поверніть його як рядок
    pass

compressed_data = compress_text(original_text)
decompressed_text = decompress_text(compressed_data)
print("Оригінальний текст:", original_text)
print("Декомпресований текст:", decompressed_text)


# Правильний код
import zlib

def compress_text(text):
    # Перетворюємо рядок у байти та стискаємо
    compressed = zlib.compress(text.encode('utf-8'))
    return compressed

def decompress_text(compressed):
    # Декомпресуємо дані та повертаємо рядок
    decompressed = zlib.decompress(compressed).decode('utf-8')
    return decompressed

compressed_data = compress_text(original_text)
decompressed_text = decompress_text(compressed_data)
print("Оригінальний текст:", original_text)
print("Декомпресований текст:", decompressed_text)


# ПРАКТИЧНЕ ЗАВДАННЯ 3
# Реалізуйте клас ZipCompressor, який дозволяє стиснути
# всі файли з певного каталогу в один ZIP-архів.
# Реалізуйте метод compress_folder(folder_path, output_zip),
# який знаходить усі файли у каталозі folder_path і додає їх у архів output_zip.
# Проведіть тестування, використовуючи тестовий каталог із кількома файлами.


import zipfile
import os

class ZipCompressor:
    def compress_folder(self, folder_path, output_zip):
        # Створіть ZIP-файл для запису
        # Переберіть усі файли у folder_path та додайте їх до ZIP-архіву
        # Закрийте архів та поверніть ім'я файлу архіву
        pass

compressor = ZipCompressor()
zip_filename = compressor.compress_folder("test_folder", "archive.zip")
print("Створено архів:", zip_filename)

# Правильний код
import zipfile
import os

class ZipCompressor:
    def compress_folder(self, folder_path, output_zip):
        with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, folder_path)
                    zipf.write(file_path, arcname)
        return output_zip

compressor = ZipCompressor()
zip_filename = compressor.compress_folder("test_folder", "archive.zip")
print("Створено архів:", zip_filename)



# РЕАЛІЗАЦІЯ СТИСНЕННЯ ЗІ ВТРАТАМИ
# img = Image.open(input_path)
# img.save(output_path, "JPEG", quality=quality)
# input_path = "goiteens.png"
# output_path = "goiteens_comp.jpg"
# compress_image(input_path, output_path, quality=30)
# print("Зображення успішно стиснуте та збережене як", output_path)

# from PIL import Image
# import os

# def compress_image(input_path, output_path, quality):
#     img = Image.open(input_path)
#     img = img.convert("RGB")
#     img.save(output_path, "JPEG", quality=quality)
#     return os.path.getsize(output_path)

# input_image = "goiteens.png"
# output_image = "goiteens_compressed.jpg"
# quality = 50
# compressed_size = compress_image(input_image, output_image, quality)
# print("Розмір стиснутого файлу:", compressed_size, "байт")


# RLE (Run-Length Encoding) — це алгоритм стиснення даних,
# який зменшує розмір файлу за рахунок заміни послідовних
# повторюваних символів або груп даних одним символом та
# числом, яке вказує на кількість повторень.
# Основна ідея полягає в тому, що для даних, де певний елемент
# або послідовність елементів повторюються багато разів підряд,
# можна замість зберігання кожного повторення зберігати лише
# сам елемент і кількість його повторень.

# Наприклад, рядок:
# AAAABBBCCDAA
# можна закодувати як:

# 4A3B2C1D2A