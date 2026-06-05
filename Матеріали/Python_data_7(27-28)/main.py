import folium
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import dask.dataframe as dd
import random
# import vaex


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
# dtype_dict = {
#     'survived': 'int64',
#     'pclass': 'int64',
#     'sex': 'object',
#     'age': 'float64',
#     'sibsp': 'int64',
#     'parch': 'int64',
#     'fare': 'float64',
#     'embarked': 'object',
#     'class': 'object',
#     'who': 'object',
#     'adult_male': 'bool',
#     'deck': 'object',
#     'embark_town': 'object',
#     'alive': 'object',
#     'alone': 'bool'
# }
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
# from faker import Faker
# import random

# fake = Faker()

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

# num_records = 500000
# data = {
#     'CustomerId': [fake.uuid4() for _ in range(num_records)],
#     'Name': [fake.name() for _ in range(num_records)],
#     'Age': [random.randint(18, 80) for _ in range(num_records)],
#     'Email': [fake.email() for _ in range(num_records)],
#     'Country': [fake.country() for _ in range(num_records)],
#     'SignupDate': [fake.date_between(start_date='-3y', end_date='today') for _ in range(num_records)],
#     'MembershipType': [random.choice(['Basic', 'Silver', 'Gold', 'Platinum']) for _ in range(num_records)]
# }
# df_customers = pd.DataFrame(data)
# df_customers.to_csv('large_customer_data.csv', index=False)

# Завдання
# Завантажте файл large_sales_data.csv за допомогою Dask.
# ddf_sales = dd.read_csv('large_sales_data.csv')
# # Виведіть перші 5 рядків датасету.
# print(ddf_sales.head(5))
# # Встановити типи даних за допомогою словника, зазначивши, що колонка CustomerId має тип category, а Price — float32.
# dtype_dict = {
#     'TransactionId': 'int64',
#     'CustomerId': 'category',
#     'ProductId': 'category',
#     'Quantity': 'int64',
#     'Price': 'float32',
#     'Date': 'object',
#     'Country': 'category'
# }
# ddf_sales = dd.read_csv('large_sales_data.csv', dtype=dtype_dict)
# # Додайте один рядок коду для встановлення 'ProductId' як індекс перед групуванням
# ddf_sales = ddf_sales.set_index('ProductId')
# # Виконайте групування даних за колонкою 'ProductId' та обчисліть суму продажів (Quantity * Price) для кожного продукту.
# ddf_sales['Total'] = ddf_sales['Quantity'] * ddf_sales['Price']
# grouped_sales = ddf_sales.groupby('ProductId')['Total'].sum().reset_index()
# # Виведіть перші 5 рядків групованого датасету.
# print(grouped_sales.head(5))
# # Додайте параметр usecols, щоб імпортувати лише необхідні колонки 'MembershipType' та 'Age'.
# ddf_customers = dd.read_csv('large_customer_data.csv', usecols=['MembershipType', 'Age'])
# # Додайте один рядок коду для збереження змін у новий файл large_sales_data_with_total.csv
# grouped_sales.to_csv('large_sales_data_with_total.csv', index=False)
# # Додайте один рядок коду для визначення типів даних колонок 'Age' як int8 та 'MembershipType' як category під час імпорту.
# dtype_dict_customers = {
#     'MembershipType': 'category',
#     'Age': 'int8'
# }
# ddf_customers = dd.read_csv('large_customer_data.csv', dtype=dtype_dict_customers)
# # Додайте один рядок коду для встановлення 'Country' як індекс перед групуванням.
# ddf_customers = ddf_customers.set_index('Country')
# # Додайте параметр usecols, щоб імпортувати лише колонки 'Country' та 'CustomerId'.
# ddf_customers = dd.read_csv('large_customer_data.csv', usecols=['Country', 'CustomerId'])
# # Додайте один рядок коду для встановлення 'ProductId' як індекс перед групуванням.
# ddf_sales = ddf_sales.set_index('ProductId')
# # Додайте один рядок коду для встановлення типу даних 'MembershipType' як category під час імпорту.
# ddf_customers = dd.read_csv('large_customer_data.csv', dtype={'MembershipType': 'category'})
# # Додайте один рядок коду для фільтрації даних, залишаючи лише продажі з 'Quantity' більше 5.
# filtered_sales = ddf_sales[ddf_sales['Quantity'] > 5]
# # Додайте один рядок коду для встановлення типу даних 'Country' як category під час імпорту.
# ddf_customers = dd.read_csv('large_customer_data.csv', dtype={'Country': 'category'})



# VAEX
# Vaex — це відкритий фреймворк для обробки великих
# наборів даних у Python, розроблений з метою
# забезпечення високої продуктивності та ефективного використання пам'яті.

# import vaex
# from sklearn.linear_model import LogisticRegression

# df = vaex.open('large_titanic.parquet')
# X = df[['pclass', 'sex', 'age', 'fare']].values
# y = df['survived'].values
# model = LogisticRegression()
# model.fit(X, y)
# print(f"Model Accuracy: {model.score(X, y)}")

# РОБОТА З КАРТАМИ З ВИКОРИСТАННЯМ FOLIUM
# import folium
# Створення основної карти
# location = [50.4501, 30.5234]
# m = folium.Map(location=location, zoom_start=10)
# m.save('map.html')

# Додавання маркера
# folium.Marker(
#     location=[50.4501, 30.5234],
#     popup='Центр Києва',
#     icon=folium.Icon(icon='info-sign')
# ).add_to(m)
# m.save('map_with_marker.html')

# Додавання полігону
# polygon = [
#     [50.4547, 30.5238],
#     [50.4547, 30.5338],
#     [50.4447, 30.5338],
#     [50.4447, 30.5238],
#     [50.4547, 30.5238]
# ]
# folium.Polygon(
#     locations=polygon,
#     color='blue',
#     fill=True,
#     fill_color='cyan'
# ).add_to(m)
# m.save('map_with_polygon.html')

# Створення теплової карти
# import folium
# from folium.plugins import HeatMap
# data = [
#     [50.4501, 30.5234],
#     [50.4502, 30.5235],
#     [50.4503, 30.5236]
# ]
# m = folium.Map(location=[50.4501, 30.5234], zoom_start=10)
# HeatMap(data).add_to(m)
# m.save('map_with_heatmap.html')


# GEOPY
# Geopy — це бібліотека Python для геокодування та оберненого
# геокодування, яка дозволяє перетворювати адреси в координати та навпаки.
# from geopy.geocoders import Nominatim
# geolocator = Nominatim(user_agent="my_geocoder")
# location = geolocator.geocode("1600 Amphitheatre Parkway, Mountain View, CA")
# print((location.latitude, location.longitude))
# За допомогою зворотного геокодування ми можемо отримати адресу на основі географічних координат
# location = geolocator.reverse("37.4223096, -122.0846244")
# print(location.address)

# Обчислення Відстані між Точками
# from geopy.distance import geodesic
# point1 = (37.7749, -122.4194)  # Сан-Франциско
# point2 = (34.0522, -118.2437)  # Лос-Анджелес
# distance = geodesic(point1, point2).miles
# print(f"Відстань: {distance:.2f} миль")
# distance = geodesic(point1, point2).km
# print(f"Відстань: {distance:.2f} км")


# Інтеграція Folium та Geopy
# from geopy.geocoders import Nominatim
# geolocator = Nominatim(user_agent="geo_app")
# addresses = [
#     "1600 Amphitheatre Parkway, Mountain View, CA",
#     "1 Infinite Loop, Cupertino, CA",
#     "350 Fifth Avenue, New York, NY"
# ]
# locations = []
# for address in addresses:
#     location = geolocator.geocode(address)
#     if location:
#         locations.append((location.latitude, location.longitude))
#     else:
#         print(f"Не вдалося геокодувати адресу: {address}")
# # print(locations)

# m = folium.Map(location=[37.4221, -122.0841], zoom_start=5)
# for loc, address in zip(locations, addresses):
#     folium.Marker(location=loc, popup=address).add_to(m)
# m.save('map_with_geocoded_addresses.html')