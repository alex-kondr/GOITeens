# pip install seaborn
# print(sns.__version__)

from turtle import title

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# tips = sns.load_dataset('tips')
# sns.histplot(data=tips, x='total_bill', bins=20, kde=True)
# plt.title('Розподіл Загальних Рахунків')
# plt.show()

# data = {
#     'Date': [
#         '2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03',
#         '2023-01-04', '2023-01-04', '2023-01-05', '2023-01-05', '2023-01-06',
#         '2023-02-01', '2023-02-01', '2023-02-02', '2023-02-02', '2023-02-03',
#         '2023-02-04', '2023-02-04', '2023-02-05', '2023-02-05', '2023-02-06'
#     ],
#     'Product': [
#         'Smartphone', 'Laptop', 'Tablet', 'Headphones', 'Smartwatch',
#         'Smartphone', 'Laptop', 'Tablet', 'Headphones', 'Smartwatch',
#         'Smartphone', 'Laptop', 'Tablet', 'Headphones', 'Smartwatch',
#         'Smartphone', 'Laptop', 'Tablet', 'Headphones', 'Smartwatch'
#     ],
#     'Category': [
#         'Mobile Devices', 'Computers', 'Mobile Devices', 'Accessories', 'Accessories',
#         'Mobile Devices', 'Computers', 'Mobile Devices', 'Accessories', 'Accessories',
#         'Mobile Devices', 'Computers', 'Mobile Devices', 'Accessories', 'Accessories',
#         'Mobile Devices', 'Computers', 'Mobile Devices', 'Accessories', 'Accessories'
#     ],
#     'Region': [
#         'North', 'South', 'East', 'West', 'North',
#         'South', 'East', 'West', 'North', 'South',
#         'East', 'West', 'North', 'South', 'East',
#         'West', 'North', 'South', 'East', 'West'
#     ],
#     'Sales': [
#         50, 30, 20, 100, 40,
#         60, 25, 35, 80, 45,
#         55, 40, 25, 90, 50,
#         65, 35, 30, 100, 55
#     ],
#     'Revenue': [
#         25000, 45000, 10000, 10000, 20000,
#         30000, 37500, 17500, 8000, 22500,
#         27500, 60000, 12500, 9000, 25000,
#         32500, 52500, 15000, 10000, 27500
#     ]
# }

# df = pd.DataFrame(data)
# df['Date'] = pd.to_datetime(df['Date'])

# print(df.head())

# sns.countplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None,
#               orient=None, color=None, palette=None, saturation=0.75, dodge=True, ax=None, **kwargs)
# x, y: Назви змінних у data. Параметри x та y визначають, які дані будуть представлені на горизонтальній (x) та вертикальній (y) осях графіка відповідно.
# hue: Змінна в data, яка визначає колір стовпців. Використовується для групування змінних у рамках інших основних категоріальних змінних.
# data: DataFrame, вектор або список рядків, що є джерелом даних.
# order, hue_order: Послідовність для порядку виведення категорій на графіку.
# orient: Орієнтація графіка. Значення 'v' для вертикальних стовпців (за замовчуванням) та 'h' для горизонтальних.
# color: Колір для всіх елементів графіка.
# palette: Варіанти кольорів для різних категорій, якщо використовується hue.
# saturation: Насиченість кольорів.
# dodge: Чи розділяти стовпці за hue.
# ax: Об'єкт matplotlib axes, на якому малювати графік.
# kwargs: Додаткові аргументи для matplotlib функцій.

# sns.countplot(data=df, x='Category', palette='Set2')
# plt.title('Кількість Продажів за Категоріями Продуктів')
# plt.xlabel('Категорія')
# plt.ylabel('Кількість Продажів')
# plt.show()

# sns.countplot(data=df, x='Category', hue='Region', palette='muted')
# plt.title('Кількість Продажів за Категоріями та Регіонами')
# plt.xlabel('Категорія')
# plt.ylabel('Кількість Продажів')
# plt.legend(title='Регіон')
# plt.show()

# sns.barplot(data=df, x='Category', y='Revenue', palette='pastel')
# plt.title('Середній Дохід за Категоріями Продуктів')
# plt.xlabel('Категорія')
# plt.ylabel('Середній Дохід (USD)')
# plt.show()

# Аргумент estimator
# За замовчуванням, barplot() використовує середнє (mean)
# як агрегатну функцію для числових даних.
# Однак, ви можете змінити цю функцію за допомогою
# аргументу estimator, наприклад, на суму (sum) або медіану (median).
# sns.barplot(data=df, x='Category', y='Revenue', estimator=np.median, hue='Category', palette='coolwarm')
# plt.title('Сумарний Дохід за Категоріями Продуктів')
# plt.xlabel('Категорія')
# plt.ylabel('Сумарний Дохід (USD)')
# plt.show()

df = sns.load_dataset('tips')
# print(df)
# sns.countplot(data=df, x='day')
# plt.title('Кількість Спостережень за Днями Тижня')
# plt.xlabel('День Тижня')
# plt.ylabel('Кількість Спостережень')
# plt.show()

# чи впливає статус курців (smoker) на кількість відвідувачів у різні дні тижня
# sns.countplot(data=df, x='day', hue='smoker')
# plt.title('Кількість Спостережень за Днями Тижня та Статусом Курців')
# plt.xlabel('День Тижня')
# plt.ylabel('Кількість Спостережень')
# plt.legend(title='Курець')
# plt.show()

# який середній рахунок у ресторані в різні дні тижня
# sns.barplot(data=df, x='day', y='total_bill', hue='day', palette='pastel')
# plt.title('Середній Рахунок за Днями Тижня')
# plt.xlabel('День Тижня')
# plt.ylabel('Середній Рахунок (USD)')
# plt.show()

# Завдання 4
# Побудувати barplot() для стовпців day, total_bill з розділенням за time.
# Додати заголовок та підписи до осей.
# Додати легенду з назвою 'Час Прийому Їжі'.
# Змінити палітру кольорів на 'deep'.
# Відобразити графік.
# sns.barplot(data=df, x="day", y="total_bill", hue="time", palette="deep")
# plt.legend(title="Час прийому")
# plt.xlabel("День тижня")
# plt.ylabel("Сердній рахунок")
# plt.show()

# Завдання 5
# Імпортувати бібліотеку numpy для використання функції sum.
# Побудувати barplot() для стовпців day та total_bill з використанням estimator=np.sum.
# Додати заголовок та підписи до осей.
# Змінити палітру кольорів на 'coolwarm'
# sns.barplot(data=df, x="day", y="total_bill", estimator=np.sum, palette="coolwarm", hue="time")
# plt.show()

# Завдання 6
# Побудувати barplot() для стовпців day, tip з розділенням за smoker.
# Змінити агрегатну функцію на медіану (np.median) та палітру кольорів на 'Set1'.
# Додати заголовок та підписи до осей.
# Додати легенду з назвою 'Курець'.
# Додати анотації на кожен стовпчик, які відображають медіанні значення чайових.
# sns.barplot(data=df, x="day", y="tip", hue="smoker", estimator=np.median, palette="Set1")
# plt.legend(title="Курець")
# plt.ylabel('Медіанні Чайові (USD)')
# for p in plt.gca().patches:
#     plt.annotate(format(p.get_height(), '.1f'),
#                  (p.get_x() + p.get_width() / 2., p.get_height()),
#                  ha='center', va='center',
#                  xytext=(0, 10),
#                  textcoords='offset points')
# plt.show()

# Завдання 7
# Побудувати barplot() для стовпців day та total_bill з використанням estimator=np.mean та ci='sd' (додамо стандартне відхилення)
# Змінити палітру кольорів на 'viridis'.
# Додати заголовок та підписи до осей.
# Відобразити графік.
# sns.barplot(data=df, x="day", y="total_bill", estimator=np.mean, ci="sd", palette="viridis", hue="time")
# plt.show()


# Використання Готових Палітр
# deep (Палітра deep пропонує насичені кольори, які добре виділяються на графіках)
# muted (Палітра muted містить менш насичені кольори, що робить графіки більш м'якими та приємними для очей)
# pastel (Палітра pastel використовує світлі та ніжні кольори, що робить графіки легкими та елегантними)
# dark (Палітра dark використовує темніші кольори, які добре підходять для графіків з великим контрастом)
# colorblind (Палітра colorblind розроблена з урахуванням людей з дальтонізмом, забезпечуючи хорошу видимість кольорів для всіх категорій)
# df = sns.load_dataset('penguins')
# print(df.head())
# sns.countplot(data=df, x='species', hue="species", palette='colorblind')
# plt.title('Кількість Пінгвінів за Видами (Deep Palette)')
# plt.xlabel('Вид Пінгвіна')
# plt.ylabel('Кількість Спостережень')
# plt.show()

# Створення Власних Палітр
# custom_palette = ['#FF5733', '#33FF57', '#3357FF']
# sns.countplot(data=df, x='species', palette=custom_palette)
# plt.title('Кількість Пінгвінів за Видами (Custom Palette)')
# plt.xlabel('Вид Пінгвіна')
# plt.ylabel('Кількість Спостережень')
# plt.show()

# Функція color_palette() дозволяє створювати різні типи палітр, включаючи градієнти та колірні мапи
# gradient_palette = sns.color_palette("Blues")
# sns.barplot(data=df, x='species', y='body_mass_g', hue="species", palette=gradient_palette)
# plt.title('Середня Маса Тіла за Видами Пінгвінів (Gradient Palette)')
# plt.xlabel('Вид Пінгвіна')
# plt.ylabel('Середня Маса Тіла (г)')
# plt.show()

# Функція sns.set_palette() дозволяє встановити
# глобальну палітру кольорів для всіх графіків у
# поточній сесії. Це зручно, якщо ви хочете,
# щоб всі ваші графіки мали однакову кольорову схему.
# sns.set_palette('pastel')
# sns.countplot(data=df, x='species')
# plt.title('Кількість Пінгвінів за Видами (Global Pastel Palette)')
# plt.xlabel('Вид Пінгвіна')
# plt.ylabel('Кількість Спостережень')
# plt.show()
# sns.barplot(data=df, x='species', y='body_mass_g')
# plt.title('Середня Маса Тіла за Видами Пінгвінів (Global Pastel Palette)')
# plt.xlabel('Вид Пінгвіна')
# plt.ylabel('Середня Маса Тіла (г)')
# plt.show()

# Seaborn дозволяє створювати власні палітри за допомогою функції sns.color_palette()
# custom_palette = sns.color_palette(['#FF69B4', '#8A2BE2', '#00CED1'])  # HotPink, BlueViolet, DarkTurquoise
# sns.set_palette(custom_palette)
# sns.countplot(data=df, x='species')
# plt.title('Кількість Пінгвінів за Видами (Custom Color Palette)')
# plt.xlabel('Вид Пінгвіна')
# plt.ylabel('Кількість Спостережень')
# plt.show()

# Зміна розмірів графіку
# plt.figure(figsize=(width, height))
# df = sns.load_dataset('penguins')
# sns.set_style('whitegrid')
# plt.figure(figsize=(12, 6))
# sns.barplot(data=df, x='species', y='body_mass_g', palette='pastel')
# plt.title('Середня Маса Тіла за Видами Пінгвінів (Збільшений Розмір)')
# plt.xlabel('Вид Пінгвіна')
# plt.ylabel('Середня Маса Тіла (г)')
# plt.show()


# Практичні завдання
df = sns.load_dataset('penguins')
print(df.head())

# Завдання 1
# Ми хочемо зрозуміти, який вид пінгвінів
# найпоширеніший у датасеті. Для цього побудуємо
# графік типу countplot(), який покаже кількість
# спостережень для кожного виду пінгвінів.
# sns.countplot(data=df, x='speciеs')
# plt.title('Кількість Пінгвінів за Видами')
# plt.xlabel('Вид Пінгвіна')
# plt.ylabel('Кількість Спостережень')
# plt.show()

# Завдання 2
# Ми хочемо дізнатися, чи є різниця у
# кількості самців та самок серед
# різних видів пінгвінів. Для цього
# використаємо аргумент hue, який
# дозволяє розділити дані за додатковою категорією.
# sns.countplot(data=df, x='species', hue='sex')
# plt.title('Кількість Пінгвінів за Видами та Статтю')
# plt.xlabel('Вид Пінгвіна')
# plt.ylabel('Кількість Спостережень')
# plt.legend(title='Стать')
# plt.show()

# Завдання 3
# Ми хочемо порівняти, який вид пінгвінів
# має найвище середнє значення маси тіла.
# Для цього скористаємося функцією barplot(),
# яка автоматично обчислює середнє значення для кожної категорії.
# sns.barplot(data=df, x='species', y='body_mass_g')
# plt.title('Середня Маса Тіла за Видами Пінгвінів')
# plt.xlabel('Вид Пінгвіна')
# plt.ylabel('Середня Маса Тіла (г)')
# plt.show()

# Завдання 4
# Ми хочемо порівняти середні маси тіла між
# різними видами пінгвінів та залежно від статі.
# Використаємо аргумент hue для розділення даних за статтю
# sns.barplot(data=df, x="species", y="body_mass_g", hue="sex")#, legend=False)
# plt.show()

# Завдання 5
# Ми хочемо порівняти загальну масу тіла пінгвінів
# різних видів. Для цього змінемо агрегатну функцію з
# середнього (mean) на суму (sum) за допомогою аргументу estimator
# sns.barplot(data=df, x="species", y="body_mass_g", hue="sex", estimator=np.sum)
# plt.show()

# Завдання 6
# Ми хочемо порівняти середні показники
# маси тіла між різними видами пінгвінів
# та залежно від статі. Додамо анотації,
# які відображатимуть точні значення на кожному стовпчику
# sns.barplot(data=df, x='species', y='body_mass_g', hue='sex', estimator=np.sum, palette='Set1')
# plt.title('Медіанні Масси Тіла за Видами Пінгвінів та Статтю')
# plt.xlabel('Вид Пінгвіна')
# plt.ylabel('Медіанні Маса Тіла (г)')
# plt.legend(title='Стать')
# for p in plt.gca().patches:
#     plt.annotate(format(p.get_height(), '1f'),
#                  (p.get_x() + p.get_width() / 2, p.get_height()),
#                  ha='center', va='center',
#                  xytext=(0, 0),
#                  textcoords='offset points')
# plt.show()