import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pyarrow.parquet as pq
import swifter
from faker import Faker


# aggregated_data = pd.DataFrame()
# chunk_size = 100

# for chunk in pd.read_csv("large_diamonds.csv", chunksize=chunk_size):
#     grouped = chunk.groupby(["cut", "color", "clarity"]).size().reset_index(name="count")
#     aggregated_data = pd.concat([aggregated_data, grouped], ignore_index=True)

# final_results = aggregated_data.groupby(['cut', 'color', 'clarity'])['count'].sum().reset_index()
# print(final_results)

# parquet_file = pq.ParquetFile("large_diamonds.parquet")
# for batch in parquet_file.iter_batches(batch_size=chunk_size):
#     chunk = batch.to_pandas()
#     grouped = chunk.groupby(["cut", "color", "clarity"]).size().reset_index(name="count")
#     aggregated_data = pd.concat([aggregated_data, grouped], ignore_index=True)

# final_results = aggregated_data.groupby(['cut', 'color', 'clarity'])['count'].sum().reset_index()
# print(final_results)

# store = pd.HDFStore('large_diamonds.h5')

# for chunk in store.select('df', chunksize=100):
#     grouped = chunk.groupby(['cut', 'color', 'clarity']).size().reset_index(name='count')
#     aggregated_data = pd.concat([aggregated_data, grouped], ignore_index=True)

# store.close()

# final_results = aggregated_data.groupby(['cut', 'color', 'clarity'])['count'].sum().reset_index()
# print(final_results)

# Використання векторизованих операцій
# data = {
#     'A': np.random.randint(0, 100, size=10000000),
#     'B': np.random.randint(0, 100, size=10000000)
# }
# df = pd.DataFrame(data)
# df['C'] = df['A'] + df['B']
# print(df.head())

# Використання Паралельної Обробки
# Для ще більшої швидкості обробки можна використовувати багатопроцесорність за допомогою бібліотек, таких як swifter, dask, або joblib.
# pip install swifter
# def complex_calculation(x, **kwargs):
#     return x**2 + 3*x + 5

# df['D'] = df['A'].swifter.apply(complex_calculation)
# print(df.head())

# Зменшення розміру даних
# df['Category'] = ['A', 'B', 'C', 'A', 'B'] * 200000
# df['Category'] = df['Category'].astype('category')

# Оптимізація типів даних у Pandas
# data = {
#     'Color': ['Red', 'Blue', 'Green', 'Blue', 'Red', 'Green', 'Red'],
#     'Size': ['S', 'M', 'L', 'M', 'S', 'L', 'XL']
# }
# df = pd.DataFrame(data)
# df['Color'] = df['Color'].astype('category')
# df['Size'] = df['Size'].astype('category')
# print(df.dtypes)

# data = {
#     'Country': ['USA', 'Canada', 'USA', 'Mexico', 'Canada', 'USA', 'Mexico']
# }
# df = pd.DataFrame(data)
# df['Country'] = df['Country'].astype('category')

# data = {
#     'Status': ['active', 'inactive', 'active', 'pending', 'inactive']
# }
# df = pd.DataFrame(data)
# df['Status'] = df['Status'].astype('category')

# downcast='integer' зменшує розрядність цілих чисел до найменшої можливої (int8 замість int64).
# downcast='float' зменшує розрядність дробних чисел до найменшої можливої (float16 замість float64).
# data = {
#     'A': np.random.randint(0, 100, size=1000),
#     'B': np.random.rand(1000)
# }
# df = pd.DataFrame(data)
# df['A'] = pd.to_numeric(df['A'], downcast='integer')
# df['B'] = pd.to_numeric(df['B'], downcast='float')
# print(df.dtypes)

# Преобразування колонок з датами до типу datetime дозволяє ефективніше працювати з датами та виконувати обчислення на основі часу.
# data = {
#     'Date': ['2021-01-01', '2021-02-15', '2021-03-20', '2021-04-25']
# }
# df = pd.DataFrame(data)
# df['Date'] = pd.to_datetime(df['Date'])

# Методи оптимізації типів даних
# dtype_dict = {
#     'PassengerId': 'int32',
#     'Survived': 'int8',
#     'Pclass': 'category',
#     'Sex': 'category',
#     'Age': 'float32',
#     'Fare': 'float32',
#     'Embarked': 'category'
# }
# df = pd.read_csv('large_titanic.csv', dtype=dtype_dict)

# Функція convert_dtypes() автоматично конвертує колонки до найбільш відповідних типів даних.
# data = {
#     'A': [1, 2, 3],
#     'B': ['x', 'y', 'z'],
#     'C': [1.1, 2.2, 3.3],
#     'D': [True, False, True]
# }
# df = pd.DataFrame(data)
# df = df.convert_dtypes()

# Sparse
# Для специфічних потреб можна використовувати спеціалізовані типи даних,
# такі як Sparse типи для колонок з великою кількістю нульових значень.
# data = {
#     'Sparse_Column': [0, 0, 1, 0, 2, 0, 0, 3]
# }
# df = pd.DataFrame(data)
# df['Sparse_Column'] = pd.arrays.SparseArray(df['Sparse_Column'])
# print(df.dtypes)

# Приклад 1
# Використовуємо seaborn для завантаження датасету titanic.
# Перетворюємо текстові колонки на category для економії пам'яті.
# Downcasting числових колонок для зменшення розрядності.
# titanic = sns.load_dataset('titanic')

# print(titanic.dtypes)
# print(titanic.memory_usage(deep=True))

# titanic['sex'] = titanic['sex'].astype('category')
# titanic['class'] = titanic['class'].astype('category')
# titanic['embarked'] = titanic['embarked'].astype('category')
# titanic['alive'] = titanic['alive'].astype('category')
# titanic['alone'] = titanic['alone'].astype('bool')

# titanic['age'] = pd.to_numeric(titanic['age'], downcast='float')
# titanic['fare'] = pd.to_numeric(titanic['fare'], downcast='float')

# # print(titanic.dtypes)
# print(titanic.memory_usage(deep=True))

# Приклад 2
# Створюємо словник dtype_dict для оптимізації типів даних колонок під час зчитування.
# Використовуємо цикл для читання файла частинами (chunksize=10000).
# Групуємо дані по необхідних категоріях та підраховуємо кількість записів.
# dtype_dict = {
#     'PassengerId': 'int32',
#     'Survived': 'int8',
#     'Pclass': 'category',
#     'Sex': 'category',
#     'Age': 'float32',
#     'Fare': 'float32',
#     'Embarked': 'category'
# }
# aggregated_data = pd.DataFrame()
# chunksize = 10000

# for chunk in pd.read_csv('large_titanic.csv', chunksize=chunksize, dtype=dtype_dict):
#     grouped = chunk.groupby(['Pclass', 'Sex', 'Embarked']).size().reset_index(name='count')
#     aggregated_data = pd.concat([aggregated_data, grouped], ignore_index=True)
# final_results = aggregated_data.groupby(['Pclass', 'Sex', 'Embarked'])['count'].sum().reset_index()

# Оптимізація типів даних у Pandas
# data = {
#     'A': np.random.randint(0, 100, size=1000),
#     'B': np.random.rand(1000)
# }
# df = pd.DataFrame(data)
# df['A'] = pd.to_numeric(df['A'], downcast='integer')
# df['B'] = pd.to_numeric(df['B'], downcast='float')

# data = {
#     'Country': ['USA', 'Canada', 'USA', 'Mexico', 'Canada', 'USA', 'Mexico']
# }
# df = pd.DataFrame(data)
# df['Country'] = df['Country'].astype('category')

# data = {
#     'Date': ['2021-01-01', '2021-02-15', '2021-03-20', '2021-04-25']
# }
# df = pd.DataFrame(data)
# df['Date'] = pd.to_datetime(df['Date'])

# data = {
#     'Status': ['active', 'inactive', 'active', 'pending', 'inactive']
# }
# df = pd.DataFrame(data)
# df['Status'] = df['Status'].astype('category')

# Методи оптимізації типів даних
# dtype_dict = {
#     'PassengerId': 'int32',
#     'Survived': 'int8',
#     'Pclass': 'category',
#     'Sex': 'category',
#     'Age': 'float32',
#     'Fare': 'float32',
#     'Embarked': 'category'
# }
# df = pd.read_csv('large_titanic.csv', dtype=dtype_dict)

# Функція convert_dtypes() автоматично конвертує колонки до найбільш відповідних типів даних.
# data = {
#     'A': [1, 2, 3],
#     'B': ['x', 'y', 'z'],
#     'C': [1.1, 2.2, 3.3],
#     'D': [True, False, True]
# }
# df = pd.DataFrame(data)
# df = df.convert_dtypes()

# Для специфічних потреб можна використовувати спеціалізовані типи даних,
# такі як Sparse типи для колонок з великою кількістю нульових значень.
# data = {
#     'Sparse_Column': [0, 0, 1, 0, 2, 0, 0, 3]
# }
# df = pd.DataFrame(data)
# df['Sparse_Column'] = pd.arrays.SparseArray(df['Sparse_Column'])
# print(df.dtypes)

# Практичні приклади оптимізації типів даних
# titanic = sns.load_dataset('titanic')
# print(titanic.dtypes)
# titanic['sex'] = titanic['sex'].astype('category')
# titanic['class'] = titanic['class'].astype('category')
# titanic['embarked'] = titanic['embarked'].astype('category')
# titanic['alive'] = titanic['alive'].astype('category')
# titanic['alone'] = titanic['alone'].astype('bool')
# titanic['age'] = pd.to_numeric(titanic['age'], downcast='float')
# titanic['fare'] = pd.to_numeric(titanic['fare'], downcast='float')
# print(titanic.dtypes)
# print(titanic.memory_usage(deep=True))

# Приклад 2
# dtype_dict = {
#     'PassengerId': 'int32',
#     'Survived': 'int8',
#     'Pclass': 'category',
#     'Sex': 'category',
#     'Age': 'float32',
#     'Fare': 'float32',
#     'Embarked': 'category'
# }
# aggregated_data = pd.DataFrame()
# chunksize = 10000
# for chunk in pd.read_csv('large_titanic.csv', chunksize=chunksize, dtype=dtype_dict):
#     grouped = chunk.groupby(['Pclass', 'Sex', 'Embarked']).size().reset_index(name='count')
#     aggregated_data = pd.concat([aggregated_data, grouped], ignore_index=True)
# final_results = aggregated_data.groupby(['Pclass', 'Sex', 'Embarked'])['count'].sum().reset_index()

# Функція memory_usage() дозволяє оцінити споживання пам'яті різними колонками DataFrame.
# data = {
#     'A': range(1000),
#     'B': ['category1'] * 500 + ['category2'] * 500,
#     'C': [1.1] * 1000
# }
# df = pd.DataFrame(data)
# df['B'] = df['B'].astype('category')
# df['C'] = pd.to_numeric(df['C'], downcast='float')
# print(df.memory_usage(deep=True))

# В Pandas тип Int64 дозволяє зберігати цілі числа
# з можливістю пропуску (NaN), що є корисним при роботі з реальними даним
# data = {
#     'A': [1, 2, np.nan, 4, 5]
# }
# df = pd.DataFrame(data)
# df['A'] = df['A'].astype('Int64')
# print(df.memory_usage(deep=True))
# print(df)

# Практичні приклади
# titanic = sns.load_dataset('titanic')
# print(f"Початковий розмір датасету: {titanic.shape}")
# repeat_times = 1000
# large_titanic = pd.concat([titanic] * repeat_times, ignore_index=True)
# print(f"Розмір великого датасету: {large_titanic.shape}")
# large_titanic.to_csv('large_titanic_test.csv', index=False)

# Ініціалізуємо об'єкт Faker, який дозволить нам створювати реалістичні фейкові дані для різних потреб.
# fake = Faker()
# def create_fake_data(num_records):
#     data = {
#         'Name': [],
#         'Address': [],
#         'Email': [],
#         'Job': [],
#         'Age': [],
#         'Salary': []
#     }
#     for _ in range(num_records):
#         data['Name'].append(fake.name())
#         data['Address'].append(fake.address().replace('\\n', ', '))
#         data['Email'].append(fake.email())
#         data['Job'].append(fake.job())
#         data['Age'].append(fake.random_int(min=18, max=70))
#         data['Salary'].append(fake.random_number(digits=5))
#     return pd.DataFrame(data)

# num_records = 500000
# large_fake_data = create_fake_data(num_records)
# print(f"Розмір фейкового датасету: {large_fake_data.shape}")
# large_fake_data.to_csv('large_fake_data.csv', index=False)

# Робота з великим файлом
# chunksize = 10000
# aggregated_data = pd.DataFrame()
# dtype_dict = {
#     'pclass': 'category',
#     'sex': 'category',
#     'embarked': 'category',
#     'age': 'float32',
#     'fare': 'float32'
# }
# for chunk in pd.read_csv('large_titanic.csv', chunksize=chunksize, dtype=dtype_dict, usecols=['pclass', 'sex', 'embarked', 'age', 'fare']):
#     grouped = chunk.groupby(['pclass', 'sex', 'embarked']).agg(
#         total_passengers=pd.NamedAgg(column='fare', aggfunc='count'),
#         average_age=pd.NamedAgg(column='age', aggfunc='mean'),
#         average_fare=pd.NamedAgg(column='fare', aggfunc='mean')
#     ).reset_index()

#     aggregated_data = pd.concat([aggregated_data, grouped], ignore_index=True)

# final_results = aggregated_data.groupby(['pclass', 'sex', 'embarked']).agg(
#     total_passengers=pd.NamedAgg(column='total_passengers', aggfunc='sum'),
#     average_age=pd.NamedAgg(column='average_age', aggfunc='mean'),
#     average_fare=pd.NamedAgg(column='average_fare', aggfunc='mean')
# ).reset_index()
# print(final_results)

# Приклад 2
# chunksize = 10000
# aggregated_salary = pd.DataFrame()
# dtype_dict = {
#     'Job': 'category',
#     'Salary': 'float32'
# }
# for chunk in pd.read_csv('large_fake_data.csv', chunksize=chunksize, dtype=dtype_dict, usecols=['Job', 'Salary']):
#     grouped = chunk.groupby('Job')['Salary'].sum().reset_index()
#     aggregated_salary = pd.concat([aggregated_salary, grouped], ignore_index=True)

# final_salary = aggregated_salary.groupby('Job')['Salary'].sum().reset_index()
# final_salary = final_salary.sort_values(by='Salary', ascending=False)
# print(final_salary.head(10))

# Parquet — це колоночний формат файлів, який оптимізований для зберігання та швидкого читання великих наборів даних.
# chunksize = 10000
# titanic = pd.read_csv('large_titanic.csv')
# titanic.to_parquet('large_titanic.parquet', index=False)
# for chunk in pd.read_parquet('large_titanic.parquet', engine='pyarrow', chunksize=chunksize):
#     grouped = chunk.groupby(['pclass', 'sex', 'embarked']).agg(
#         total_passengers=pd.NamedAgg(column='fare', aggfunc='count'),
#         average_age=pd.NamedAgg(column='age', aggfunc='mean'),
#         average_fare=pd.NamedAgg(column='fare', aggfunc='mean')
#     ).reset_index()
#     aggregated_data_parquet = pd.concat([aggregated_data_parquet, grouped], ignore_index=True)

# final_results_parquet = aggregated_data_parquet.groupby(['pclass', 'sex', 'embarked']).agg(
#     total_passengers=pd.NamedAgg(column='total_passengers', aggfunc='sum'),
#     average_age=pd.NamedAgg(column='average_age', aggfunc='mean'),
#     average_fare=pd.NamedAgg(column='average_fare', aggfunc='mean')
# ).reset_index()
# print(final_results_parquet)

# HDF5 — це гібридний формат файлів, який підтримує як
# колоночні, так і рядкові структури даних.
# Він також підтримує стиснення та можливість доступу до частин файлу без завантаження всього в пам'ять.
# titanic = pd.read_csv('large_titanic.csv')
# titanic.to_hdf('large_titanic.h5', key='df', mode='w', format='table')
# chunksize = 100000
# aggregated_data_hdf5 = pd.DataFrame()
# store = pd.HDFStore('large_titanic.h5')
# for chunk in store.select('df', chunksize=chunksize):
#     grouped = chunk.groupby(['pclass', 'sex', 'embarked']).agg(
#         total_passengers=pd.NamedAgg(column='fare', aggfunc='count'),
#         average_age=pd.NamedAgg(column='age', aggfunc='mean'),
#         average_fare=pd.NamedAgg(column='fare', aggfunc='mean')
#     ).reset_index()
#     aggregated_data_hdf5 = pd.concat([aggregated_data_hdf5, grouped], ignore_index=True)

# store.close()
# final_results_hdf5 = aggregated_data_hdf5.groupby(['pclass', 'sex', 'embarked']).agg(
#     total_passengers=pd.NamedAgg(column='total_passengers', aggfunc='sum'),
#     average_age=pd.NamedAgg(column='average_age', aggfunc='mean'),
#     average_fare=pd.NamedAgg(column='average_fare', aggfunc='mean')
# ).reset_index()
# print(final_results_hdf5)


# usecols
# Якщо вам потрібні лише певні колонки з великого файлу,
# параметр usecols дозволяє читати лише необхідні дані,
# зменшуючи обсяг завантажених даних та прискорюючи процес імпорту.
# columns_to_use = ['PassengerId', 'Survived', 'Pclass', 'Sex', 'Age', 'Fare']
# df = pd.read_csv('titanic.csv', usecols=columns_to_use)

# memory_map
# Параметр memory_map=True у функції read_csv() дозволяє використовувати
# меморі-карту для читання файлу, що може прискорити процес імпорту на деяких системах.
# df = pd.read_csv('large_dataset.csv', memory_map=True)

# nrows
# Перед імпортом великого файлу корисно протестувати код на невеликій частині
# даних за допомогою параметра nrows. Це дозволяє переконатися в коректності типів
# даних та логіки обробки без необхідності завантажувати весь файл
# df_sample = pd.read_csv('large_dataset.csv', nrows=1000)

# Vaex — це високопродуктивна бібліотека для обробки великих наборів даних,
# яка дозволяє працювати з даними, що не вміщуються в пам'ять, за допомогою векторизованих обчислень.
# df = vaex.from_csv('large_dataset.csv', convert=True, chunk_size=5_000_000)
# result = df.groupby(['Category', 'Subcategory'], agg={'count': vaex.agg.count()})
# print(result)