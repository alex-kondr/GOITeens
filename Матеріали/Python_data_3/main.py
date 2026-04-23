# pip install seaborn
# print(sns.__version__)

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
sns.barplot(data=df, x='day', y='total_bill', hue='day', palette='pastel')
plt.title('Середній Рахунок за Днями Тижня')
plt.xlabel('День Тижня')
plt.ylabel('Середній Рахунок (USD)')
plt.show()