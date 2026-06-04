import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import dask.dataframe as dd
import random


# data = {
#     'Category': [random.choice(['A', 'B', 'C', 'D']) for _ in range(100000)],
#     'Value1': [random.randint(1, 100) for _ in range(100000)],
#     'Value2': [random.uniform(10.0, 50.0) for _ in range(100000)]
# }

# df = pd.DataFrame(data)
# # Зберігаємо саме під тією назвою, яка в конспекті
# df.to_csv('large_dataset.csv', index=False)


# head(): Повертає перші N рядків.
# tail(): Повертає останні N рядків.
# describe(): Повертає описову статистику.
# info(): Показує інформацію про DataFrame.
# ddf = dd.read_csv('large_diamonds.csv')
# print(ddf.head())
# print(ddf.tail())
# print(ddf.describe())
# ddf.info()

# pdf = pd.DataFrame({
#     'A': range(1000),
#     'B': ['Category1'] * 500 + ['Category2'] * 500
# })
# ddf = dd.from_pandas(pdf, npartitions=10)
# print(ddf.head())


# ЧИТАННЯ ТА ЗАПИС ДАНИХ З ВИКОРИСТАННЯМ DASK
# ddf = dd.read_csv('large_dataset.csv', dtype={'column1': 'int32', 'column2': 'category'})
# ddf = dd.read_parquet('dataset.parquet')
# Використання * дозволяє створювати кілька файлів з відповідними частинами даних.
# ddf.to_csv('output_folder/output-*.csv', index=False)
# ddf.to_parquet('output_folder/')

# ОБЧИСЛЕННЯ ТА АГРЕГАЦІЯ ДАНИХ
# ddf = dd.read_csv('large_diamonds.csv')
# # grouped = ddf.groupby(['cut', 'color']).size().reset_index().rename(columns={0: 'count'})
# grouped = ddf.groupby(['cut', 'color']).agg(count=('cut', 'count')).reset_index()
# # filtered = ddf[ddf['Age'] > 30]
# # ddf['Total'] = ddf['A'] + ddf['B']
# result = grouped.compute()
# print(result)

# ПАРАЛЕЛІЗМ ТА МАСШТАБОВАНІСТЬ
# from dask.distributed import Client
# client = Client()

# Dask інтегрується зі Scikit-learn для створення
# масштабованих моделей машинного навчання
# (розглянемо більш детально на наступних уроках).

# Приклад 1
dtype_dict = {
    'survived': 'int64',
    'pclass': 'int64',
    'sex': 'object',
    'age': 'float64',
    'sibsp': 'int64',
    'parch': 'int64',
    'fare': 'float64',
    'embarked': 'object',
    'class': 'object',
    'who': 'object',
    'adult_male': 'bool',
    'deck': 'object',
    'embark_town': 'object',
    'alive': 'object',
    'alone': 'bool'
}
# ddf = dd.read_csv('large_titanic.csv', dtype=dtype_dict, usecols=['pclass', 'sex', 'embarked'])
# # print(ddf.head())
# grouped = ddf.groupby(['pclass', 'sex', 'embarked']).agg(count=('pclass', 'count')).reset_index()
# result = grouped.compute()
# print(result)

# Приклад 2
# from dask.distributed import Client
# import dask.dataframe as dd


# if __name__ == "__main__":
#     client = Client(n_workers=4, threads_per_worker=1, memory_limit='1GB')
    # print(client)

    # ddf = dd.read_csv('large_dataset.csv', dtype={'Value1': 'float64'})
    # grouped = ddf.groupby('Category').mean(numeric_only=True) # пам'ятаємо про numeric_only!
    # result = grouped.compute()
    # print(result)
    
    # ddf = dd.read_csv('large_titanic.csv')
    # grouped = ddf.groupby('sex').mean(numeric_only=True) 
    # result = grouped.compute()
    # print(result)
    
# Приклад 3
# import dask.dataframe as dd
# from dask.distributed import Client
# from dask_ml.linear_model import LogisticRegression
# from dask_ml.model_selection import train_test_split


# dtype_dict = {
#     'survived': 'int64', 'pclass': 'int64', 'sex': 'object', 'age': 'float64',
#     'sibsp': 'int64', 'parch': 'int64', 'fare': 'float64', 'embarked': 'object',
#     'class': 'object', 'who': 'object', 'adult_male': 'bool', 'deck': 'object',
#     'embark_town': 'object', 'alive': 'object', 'alone': 'bool'
# }

# if __name__ == "__main__":
#     client = Client(n_workers=4, threads_per_worker=1, memory_limit='1GB')
#     print("Dask Client запущено:", client)
#     ddf = dd.read_csv('large_titanic.csv', dtype=dtype_dict)
#     feature_cols = ['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked', 'adult_male', 'alone']
#     ddf = ddf[feature_cols]
#     ddf['age'] = ddf['age'].fillna(ddf['age'].mean())
#     ddf['pclass'] = ddf['pclass'].astype(str)
#     categorical_cols = ['sex', 'embarked', 'pclass', 'adult_male', 'alone']
#     ddf = ddf.categorize(columns=categorical_cols)
#     ddf = dd.get_dummies(ddf, columns=categorical_cols)
#     X = ddf.drop(['survived'], axis=1)
#     X = X.astype(float)
#     y = ddf['survived']
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True)
#     X_train_array = X_train.to_dask_array(lengths=True)
#     X_test_array = X_test.to_dask_array(lengths=True)
#     y_train_array = y_train.to_dask_array(lengths=True)
#     y_test_array = y_test.to_dask_array(lengths=True)
#     model = LogisticRegression()
#     model.fit(X_train_array, y_train_array)
#     score = model.score(X_test_array, y_test_array)
#     # Оскільки score повертає Dask-об'єкт (Lazy), викликаємо .compute(), щоб отримати число
#     print(f"Model Accuracy: {score.compute()}")

# Практика
from faker import Faker
import random

fake = Faker()

# num_records = 1000000 
# data = {
#     'TransactionId': range(1, num_records + 1),
#     'CustomerId': [fake.uuid4() for _ in range(num_records)],
#     'ProductId': [f"P{random.randint(1000, 9999)}" for _ in range(num_records)],
#     'Quantity': [random.randint(1, 10) for _ in range(num_records)],
#     'Price': [round(random.uniform(5.0, 500.0), 2) for _ in range(num_records)],
#     'Date': [fake.date_between(start_date='-2y', end_date='today') for _ in range(num_records)],
#     'Country': [fake.country() for _ in range(num_records)]
# }
# df_sales = pd.DataFrame(data)
# df_sales.to_csv('large_sales_data.csv', index=False)

num_records = 500000
data = {
    'CustomerId': [fake.uuid4() for _ in range(num_records)],
    'Name': [fake.name() for _ in range(num_records)],
    'Age': [random.randint(18, 80) for _ in range(num_records)],
    'Email': [fake.email() for _ in range(num_records)],
    'Country': [fake.country() for _ in range(num_records)],
    'SignupDate': [fake.date_between(start_date='-3y', end_date='today') for _ in range(num_records)],
    'MembershipType': [random.choice(['Basic', 'Silver', 'Gold', 'Platinum']) for _ in range(num_records)]
}
df_customers = pd.DataFrame(data)
df_customers.to_csv('large_customer_data.csv', index=False)