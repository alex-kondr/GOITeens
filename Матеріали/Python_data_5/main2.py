import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pyarrow.parquet as pq
import swifter


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