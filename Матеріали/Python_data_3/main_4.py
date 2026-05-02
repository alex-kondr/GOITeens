import numpy as np
import pandas as pd
import seaborn as sns


# Метод concat() у Pandas використовується для об'єднання
# кількох DataFrame або Series у один об'єкт.
# Цей метод підтримує об'єднання як по рядках
# (вертикальне об'єднання), так і по стовпцях
# (горизонтальне об'єднання). Він є універсальним
# інструментом, який дозволяє легко комбінувати
# дані з різних джерел або різних частин одного набору даних.
# pd.concat(objs, axis=0, join='outer', ignore_index=False, keys=None, levels=None, names=None, verify_integrity=False, sort=False, copy=True)
# objs: Послідовність або мапа об'єктів Pandas (наприклад, список DataFrame), які потрібно об'єднати.
# axis: Вісь для об'єднання. 0 — по рядках, 1 — по стовпцях.
# join: Тип з'єднання. 'outer' (за замовчуванням) — повне з'єднання, 'inner' — внутрішнє з'єднання.
# ignore_index: Якщо True, ігнорує індекси оригінальних об'єктів і створює новий цілий індекс.
# keys: Множина ключів для створення багаторівневого індексу.
# verify_integrity: Якщо True, перевіряє, чи немає дублюючих індексів після об'єднання.
# sort: Якщо True, сортує незбігаючі стовпці.

# Об'єднання таблиць по рядках (вертикальне об'єднання)
# df1 = pd.DataFrame({
#     'A': ['A0', 'A1', 'A2'],
#     'B': ['B0', 'B1', 'B2']
# })
# df2 = pd.DataFrame({
#     'A': ['A3', 'A4', 'A5'],
#     'B': ['B3', 'B4', 'B5']
# })
# result = pd.concat([df1, df2], axis=0, ignore_index=True)

# df1 = pd.DataFrame({
#     'ProductID': [1, 2, 3],
#     'Category': ['Electronics', 'Home Appliances', 'Electronics'],
#     'Price': [699, 1200, 850]
# })
# df2 = pd.DataFrame({
#     'ProductID': [4, 5],
#     'Category': ['Furniture', 'Electronics'],
#     'Price': [500, 650]
# })
# result = pd.concat([df1, df2], axis=0, ignore_index=True)


# Об'єднання таблиць по стовпцях (горизонтальне об'єднання)
# df1 = pd.DataFrame({
#     'A': ['A0', 'A1', 'A2'],
#     'B': ['B0', 'B1', 'B2']
# })
# df2 = pd.DataFrame({
#     'C': ['C0', 'C1', 'C2'],
#     'D': ['D0', 'D1', 'D2']
# })
# result = pd.concat([df1, df2], axis=1)

# df1 = pd.DataFrame({
#     'ProductID': [1, 2, 3],
#     'Category': ['Electronics', 'Home Appliances', 'Electronics']
# })
# df2 = pd.DataFrame({
#     'Price': [699, 1200, 850],
#     'Availability': ['In Stock', 'Out of Stock', 'In Stock']
# })
# result = pd.concat([df1, df2], axis=1)


# Використання параметра join
# df1 = pd.DataFrame({
#     'ProductID': [1, 2, 3],
#     'Category': ['Electronics', 'Home Appliances', 'Electronics']
# })
# df2 = pd.DataFrame({
#     'ProductID': [4, 5],
#     'Price': [500, 650]
# })
# result_outer = pd.concat([df1, df2], axis=0, join='outer')
# print(result_outer)
# result_inner = pd.concat([df1, df2], axis=0, join='inner')
# print(result_inner)
# Об'єднання з використанням внутрішнього з'єднання
# df1 = pd.DataFrame({
#     'A': ['A0', 'A1', 'A2'],
#     'B': ['B0', 'B1', 'B2']
# })
# df2 = pd.DataFrame({
#     'B': ['B1', 'B2', 'B3'],
#     'C': ['C1', 'C2', 'C3']
# })
# result = pd.concat([df1, df2], axis=0, join='inner')


# Об'єднання таблиць з різними стовпцями
# Метод concat() дозволяє об'єднувати таблиці
# з різними стовпцями. За замовчуванням,
# невідповідні стовпці заповнюються NaN
# df1 = pd.DataFrame({
#     'ProductID': [1, 2, 3],
#     'Category': ['Electronics', 'Home Appliances', 'Electronics'],
#     'Price': [699, 1200, 850]
# })
# df2 = pd.DataFrame({
#     'ProductID': [4, 5],
#     'Category': ['Furniture', 'Electronics'],
#     'Price': [500, 650],
#     'Rating': [4.5, 4.2]
# })
# result = pd.concat([df1, df2], axis=0, ignore_index=True)
# print(result)


# ПРИКЛАДИ
# df1 = pd.DataFrame({
#     'ProductID': [1, 2, 3],
#     'Category': ['Electronics', 'Home Appliances', 'Electronics'],
#     'Price': [699, 1200, 850]
# })
# df2 = pd.DataFrame({
#     'ProductID': [4, 5],
#     'Category': ['Furniture', 'Electronics'],
#     'Price': [500, 650]
# })
# result = pd.concat([df1, df2], axis=0)
# result = pd.concat([df1, df2], axis=0, ignore_index=True)
# result = pd.concat([df1, df2], axis=0, join='inner')
# result = pd.concat([df1, df2], axis=1)
# result = pd.concat([df1, df2], axis=1, join='inner')
# result = pd.concat([df1, df2], axis=0, keys=['Store1', 'Store2'])
# try:
#     result = pd.concat([df1, df2], axis=0, verify_integrity=True)
# except ValueError as e:
#     print("Integrity Error:", e)
# result = pd.concat([df1, df2], axis=1, keys=['Store1', 'Store2'])
# print(result)


# Завдання 1
# Знайдіть помилку у коді, яка може
# призвести до дублювання індексів після
# об'єднання таблиць, та виправте її, щоб уникнути дублювання індексів.
# sales_q1 = pd.DataFrame({
#     'ProductID': [101, 102, 103],
#     'Sales': [250, 150, 300]
# })
# sales_q2 = pd.DataFrame({
#     'ProductID': [104, 105],
#     'Sales': [200, 350]
# })
# result = pd.concat([sales_q1, sales_q2, axis=0]))

# Завдання 2
# Додайте параметр, щоб об'єднати таблиці
# по рядках, ігноруючи оригінальні індекси
# та створивши новий послідовний індекс
# df1 = pd.DataFrame({
#     'EmployeeID': [1, 2, 3],
#     'Name': ['Alice', 'Bob', 'Charlie']
# })
# df2 = pd.DataFrame({
#     'EmployeeID': [4, 5],
#     'Name': ['David', 'Eva']
# })
# result = pd.concat([df1, df2], axis=0)

# Завдання 3
# Змініть код, щоб об'єднати таблиці
# по стовпцях, не змінюючи індекси.
# df1 = pd.DataFrame({
#     'EmployeeID': [1, 2, 3],
#     'Name': ['Alice', 'Bob', 'Charlie']
# })
# df2 = pd.DataFrame({
#     'Department': ['HR', 'Engineering', 'Marketing']
# })
# result = pd.concat([df1, df2])

# Завдання 4
# Змініть код, щоб об'єднати таблиці
# df1 та df2 по стовпцях з внутрішнім
# з'єднанням, включаючи тільки спільні стовпці.
# df1 = pd.DataFrame({
#     'EmployeeID': [1, 2, 3],
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Department': ['HR', 'Engineering', 'Marketing']
# })
# df2 = pd.DataFrame({
#     'EmployeeID': [2, 3, 4],
#     'Salary': [70000, 80000, 60000]
# })
# result = pd.concat([df1, df2], axis=1, join='inner')

# Завдання 5
# Додайте параметр verify_integrity,
# щоб перевірити відсутність дублюючих
# індексів при об'єднанні таблиць df1 та df2 по рядках
# df1 = pd.DataFrame({
#     'ProductID': [101, 102, 103],
#     'Category': ['Electronics', 'Furniture', 'Toys'],
#     'Sales': [500, 300, 150]
# }, index=[0, 1, 2])
# df2 = pd.DataFrame({
#     'ProductID': [104, 105],
#     'Category': ['Electronics', 'Toys'],
#     'Sales': [200, 250]
# }, index=[2, 3])
# result = pd.concat([df1, df2], axis=0)


# ЩО ТАКЕ ІНДЕКСИ В PANDAS?

# Використання методу set_index() для призначення одного або декількох стовпців як індексу.
# df = df.set_index('ProductID')

# df = pd.DataFrame({
#     'ProductID': [101, 102, 103],
#     'Category': ['Electronics', 'Furniture', 'Toys'],
#     'Price': [500, 300, 150]
# })
# df = df.set_index('ProductID')

# Використання методу reset_index() для повернення індексу до стандартного числового значення.
# df = df.reset_index()

# Ігнорування оригінальних індексів при вертикальному
# об'єднанні таблиць і створення нового послідовного індексу.
# result = pd.concat([df1, df2], axis=0, ignore_index=True)

# Використання параметра keys у concat() для створення MultiIndex.
# result = pd.concat([df1, df2], axis=0, keys=['Store1', 'Store2'])


# ЩО ТАКЕ МЕТОД MERGE()?
# pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,
#          left_index=False, right_index=False, sort=False,
#          suffixes=('_x', '_y'), copy=True, indicator=False,
#          validate=None)
# left: Лівий DataFrame.
# right: Правий DataFrame.
# how: Тип з'єднання ('left', 'right', 'outer', 'inner'). За замовчуванням 'inner'.
# on: Стовпець(ці) для об'єднання, які мають бути присутні у обох таблицях.
# left_on: Стовпець(ці) у лівому DataFrame для об'єднання.
# right_on: Стовпець(ці) у правому DataFrame для об'єднання.
# left_index: Якщо True, використовує індекс лівого DataFrame для об'єднання.
# right_index: Якщо True, використовує індекс правого DataFrame для об'єднання.
# sort: Якщо True, сортує результуючий DataFrame за ключами.
# suffixes: Суфікси для стовпців з однаковими назвами, що не входять до ключів.
# indicator: Якщо True, додає стовпець _merge, що вказує джерело рядка.
# validate: Перевірка типу з'єднання (наприклад, 'one_to_one', 'one_to_many' тощо).


# ТИПИ З'ЄДНАНЬ У MERGE()
# Inner Join (how='inner')
# Включає тільки ті рядки, які мають спільні ключі в обох таблицях.
# result = pd.merge(df1, df2, on='ProductID', how='inner')

# Left Join (how='left')
# Включає всі рядки з лівого DataFrame та
# відповідні рядки з правого DataFrame.
# Якщо немає відповідних рядків, заповнює NaN.
# result = pd.merge(df1, df2, on='ProductID', how='left')

# Right Join (how='right')
# Включає всі рядки з правого DataFrame та
# відповідні рядки з лівого DataFrame.
# Якщо немає відповідних рядків, заповнює NaN
# result = pd.merge(df1, df2, on='ProductID', how='right')

# Outer Join (how='outer')
# Включає всі рядки з обох DataFrame,
# заповнюючи NaN там, де немає відповідностей.
# result = pd.merge(df1, df2, on='ProductID', how='outer')

# Inner Join на основі спільного стовпця
# df_orders = pd.DataFrame({
#     'OrderID': [1, 2, 3, 4],
#     'ProductID': [101, 102, 103, 104],
#     'Quantity': [2, 1, 5, 3]
# })
# df_products = pd.DataFrame({
#     'ProductID': [101, 102, 103, 105],
#     'ProductName': ['Laptop', 'Smartphone', 'Tablet', 'Monitor'],
#     'Price': [700, 500, 300, 200]
# })
# result = pd.merge(df_orders, df_products, on='ProductID', how='inner')
# result = pd.merge(df_orders, df_products, on='ProductID', how='left')
# result = pd.merge(df_orders, df_products, on='ProductID', how='outer')

# Злиття таблиць з різними іменами ключових стовпців
# df_customers = pd.DataFrame({
#     'CustomerID': [1, 2, 3],
#     'CustomerName': ['Alice', 'Bob', 'Charlie']
# })
# df_orders = pd.DataFrame({
#     'OrderID': [101, 102, 103],
#     'CustID': [1, 2, 4],
#     'Amount': [250, 150, 300]
# })
# result = pd.merge(df_customers, df_orders, left_on='CustomerID', right_on='CustID', how='inner')

# Злиття таблиць за індексом
# df_a = pd.DataFrame({
#     'Product': ['Laptop', 'Smartphone', 'Tablet'],
#     'Price': [700, 500, 300]
# }, index=[101, 102, 103])
# df_b = pd.DataFrame({
#     'Stock': [50, 150, 200]
# }, index=[101, 102, 104])
# result = pd.merge(df_a, df_b, left_index=True, right_index=True, how='outer')

# Використання параметра indicator для діагностики злиття
# df1 = pd.DataFrame({
#     'EmployeeID': [1, 2, 3],
#     'Name': ['Alice', 'Bob', 'Charlie']
# })
# df2 = pd.DataFrame({
#     'EmployeeID': [3, 4],
#     'Department': ['HR', 'Engineering']
# })
# result = pd.merge(df1, df2, on='EmployeeID', how='outer', indicator=True)

# ТИПИ ЗЛИТТЯ У МЕТОДІ MERGE()