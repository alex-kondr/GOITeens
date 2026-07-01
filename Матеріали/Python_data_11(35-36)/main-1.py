# Лінійна регресія — це метод машинного навчання
# для прогнозування числових значень. Вона шукає
# лінійну залежність між вхідними даними (ознаками)
# та результатом, який ми хочемо передбачити.


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import kagglehub
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.datasets import fetch_california_housing
from statsmodels.stats.outliers_influence import variance_inflation_factor
import statsmodels.api as sm


# path = kagglehub.dataset_download("shivam2503/diamonds")
# path_to_csv = os.path.join(path, "diamonds.csv")
# df = pd.read_csv(path_to_csv)
# # print(df)
# X = df[['carat', 'depth', 'table', 'x', 'y', 'z']]
# y = df['price']
# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.3)
# model = LinearRegression()
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)
# print("Mean Squared Error:", mse)
# print("R² Score:", r2)
# plt.scatter(y_test, y_pred, color='blue')
# plt.xlabel('Фактична ціна')
# plt.ylabel('Прогнозована ціна')
# plt.title('Фактична vs Прогнозована ціна алмазів')
# # plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
# plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'g--')
# plt.show()

# wine = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv',sep=';')
# X = wine[['alcohol']]
# y = wine['quality']
# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.3)
# model = LinearRegression()
# model.fit(X_train, y_train)
# print(model.intercept_)
# print(model.coef_)
# y_pred = model.predict(X_test)
# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)
# print("Mean Squared Error:", mse)
# print("R² Score:", r2)
# plt.figure(figsize=(10,6))
# plt.scatter(y_test, y_pred, color='green')
# plt.xlabel('Фактична якість')
# plt.ylabel('Прогнозована якість')
# plt.title('Проста лінійна регресія: Алкоголь vs Якість')
# plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
# plt.show()

# path = kagglehub.dataset_download("nikhil7280/student-performance-multiple-linear-regression")
# path_to_csv = os.path.join(path, "student_performance.csv")
# student = pd.read_csv(path_to_csv)
# X = student[['Hours Studied']]
# y = student['Previous Scores']
# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.3)
# model = LinearRegression()
# model.fit(X_train, y_train)
# print(model.intercept_)
# print(model.coef_)
# y_pred = model.predict(X_test)
# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)
# print("Mean Squared Error:", mse)
# print("R² Score:", r2)
# plt.figure(figsize=(10,6))
# plt.scatter(y_test, y_pred, color='green')
# plt.xlabel('Фактична оцінка')
# plt.ylabel('Прогнозована оцінка')
# plt.title('Проста лінійна регресія: Години навчання vs Попередні оцінки')
# plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
# plt.show()


# ЛЕГКЕ ЗАВДАННЯ 1
# np.random.seed(0)
# data = {
#     'Square_Feet': np.random.randint(1000, 4500, size=150),
#     'Bedrooms': np.random.randint(1, 5, size=150),
#     'Bathrooms': np.random.randint(1, 4, size=150),
#     'Price': np.random.randint(200000, 750000, size=150)
# }
# Створити DataFrame з даних.
# Розділити дані на ознаки (X) та цільову змінну (y).
# Розділити дані на навчальний (70%) та тестовий (30%) набори.
# Навчити модель лінійної регресії на тренувальних даних.
# Прогнозувати ціни на тестових даних.
# Оцінити модель за допомогою MSE та R².
# Візуалізувати фактичні та прогнозовані ціни.

# df = pd.DataFrame(data)
# X = df.drop("Price", axis=1)
# y = df["Price"]
# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=16, test_size=0.3)
# model = LinearRegression()
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)
# print("Mean Squared Error:", mse)
# print("R² Score:", r2)
# plt.figure(figsize=(10,6))
# plt.scatter(y_test, y_pred, color='green')
# plt.xlabel('Фактична ціна')
# plt.ylabel('Прогнозована ціна')
# plt.title('Прогнозування ціни будинку: Фактичні vs Прогнозовані значення')
# plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
# plt.show()


# ЛЕГКЕ ЗАВДАННЯ 2
# np.random.seed(0)
# data = {
#     'Hours_Studied': np.random.randint(1, 15, size=100),
#     'Previous_Score': np.random.randint(50, 100, size=100),
#     'Final_Score': np.random.randint(50, 100, size=100)
# }
# Створити DataFrame з даних.
# Розділити дані на ознаки (X) та цільову змінну (y).
# Розділити дані на навчальний (80%) та тестовий (20%) набори.
# Навчити модель лінійної регресії на тренувальних даних.
# Прогнозувати фінальні бали на тестових даних.
# Оцінити модель за допомогою MSE та R².
# Візуалізувати фактичні та прогнозовані фінальні бали.

# df = pd.DataFrame(data)
# X = df.drop("Final_Score", axis=1)
# y = df["Final_Score"]
# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=16, test_size=0.3)
# model = LinearRegression()
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)
# print("Mean Squared Error:", mse)
# print("R² Score:", r2)
# plt.figure(figsize=(10,6))
# plt.scatter(y_test, y_pred, color='green')
# plt.xlabel('Фактична оцінка')
# plt.ylabel('Прогнозована оцінка')
# plt.title('Прогнозування оцінки студента: Фактичні vs Прогнозовані значення')
# plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
# plt.show()


# СЕРЕДНЄ ЗАВДАННЯ 1
# np.random.seed(0)
# data = {
#     'Carat': np.random.uniform(0.2, 5.0, size=200),
#     'Cut': np.random.choice(['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'], size=200),
#     'Color': np.random.choice(['D', 'E', 'F', 'G', 'H', 'I', 'J'], size=200),
#     'Clarity': np.random.choice(['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'], size=200),
#     'Depth': np.random.uniform(55, 70, size=200),
#     'Table': np.random.uniform(50, 65, size=200),
#     'Price': np.random.randint(500, 20000, size=200)
# }
# Створити DataFrame з даних.
# Розділити дані на ознаки (X) та цільову змінну (y).
# Закодувати категоріальні змінні за допомогою OneHotEncoder.
# Розділити дані на навчальний (75%) та тестовий (25%) набори.
# Навчити модель лінійної регресії на тренувальних даних.
# Прогнозувати ціни на тестових даних.
# Оцінити модель за допомогою MSE та R².
# Візуалізувати фактичні та прогнозовані ціни.

# df = pd.DataFrame(data)
# X = df.drop("Price", axis=1)
# y = df["Price"]
# encoder = OneHotEncoder()
# X_encoded = encoder.fit_transform(X)
# X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, random_state=16, test_size=0.3)
# model = LinearRegression()
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)
# print("Mean Squared Error:", mse)
# print("R² Score:", r2)
# plt.figure(figsize=(10,6))
# plt.scatter(y_test, y_pred, color='green')
# plt.xlabel('Фактична ціна')
# plt.ylabel('Прогнозована ціна')
# plt.title('Прогнозування ціни будинку: Фактичні vs Прогнозовані значення')
# plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
# plt.show()


# СЕРЕДНЄ ЗАВДАННЯ 2
# np.random.seed(0)
# data = {
#     'Advertising_Spend': np.random.uniform(1000, 10000, size=150),
#     'Store_Size': np.random.randint(500, 5000, size=150),
#     'Location': np.random.choice(['Urban', 'Suburban', 'Rural'], size=150),
#     'Sales': np.random.randint(20000, 150000, size=150)
# }
# Створити DataFrame з даних.
# Розділити дані на ознаки (X) та цільову змінну (y).
# Закодувати категоріальну змінну Location за допомогою OneHotEncoder.
# Масштабувати числові ознаки за допомогою StandardScaler.
# Розділити дані на навчальний (80%) та тестовий (20%) набори.
# Навчити модель лінійної регресії на тренувальних даних.
# Прогнозувати продажі на тестових даних.
# Оцінити модель за допомогою MAE та R².
# Візуалізувати фактичні та прогнозовані продажі.

# df = pd.DataFrame(data)
# X = df.drop("Sales", axis=1)
# y = df["Sales"]
# encoder = OneHotEncoder(sparse_output=False)
# X_encoded = encoder.fit_transform(X[["Location"]])
# # print(X_encoded)
# X_encoded_df = pd.DataFrame(X_encoded, columns=encoder.get_feature_names_out(["Location"]))
# X = pd.concat([X, X_encoded_df], axis=1)
# X = X.drop("Location", axis=1)
# print(X)
# scaler = StandardScaler()
# X = scaler.fit_transform(X)
# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=16, test_size=0.3)
# model = LinearRegression()
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
# print("R² Score:", r2_score(y_test, y_pred))
# plt.figure(figsize=(10,6))
# plt.scatter(y_test, y_pred, color='green')
# plt.xlabel('Фактичні продажі')
# plt.ylabel('Прогнозовані продажі')
# plt.title('Прогнозування продажів: Фактичні vs Прогнозовані значення')
# plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
# plt.show()


# СКЛАДНЕ ЗАВДАННЯ 1
# np.random.seed(0)
# data = {
#     'Temperature': np.random.uniform(-10, 40, size=300),
#     'Humidity': np.random.uniform(20, 100, size=300),
#     'Wind_Speed': np.random.uniform(0, 15, size=300),
#     'Energy_Consumption': np.random.randint(100, 1000, size=300)
# }
# Створити DataFrame з даних.
# Розділити дані на ознаки (X) та цільову змінну (y).
# Масштабувати числові ознаки за допомогою StandardScaler.
# Розділити дані на навчальний (70%) та тестовий (30%) набори.
# Навчити модель Ridge регресії з альфа=1.0 на тренувальних даних.
# Ridge (Регресія Ріджа / L2-регуляризація)
# Прогнозувати споживання енергії на тестових даних.
# Оцінити модель за допомогою MSE та R².
# Візуалізувати фактичні та прогнозовані значення споживання енергії.
# df = pd.DataFrame(data)
# X = df.drop("Energy_Consumption", axis=1)
# y = df["Energy_Consumption"]
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)
# X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, random_state=16, test_size=0.3)
# model = Ridge(alpha=1.0)
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)
# print("Mean Squared Error:", mse)
# print("R² Score:", r2)
# plt.figure(figsize=(10,6))
# plt.scatter(y_test, y_pred, color='green')
# plt.xlabel('Фактичне споживання енергії')
# plt.ylabel('Прогнозоване споживання енергії')
# plt.title('Прогнозування споживання енергії: Фактичні vs Прогнозовані значення')
# plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
# plt.show()


# Методи оцінки та інтерпретації коефіцієнтів
# data = fetch_california_housing()
# X = data.data
# y = data.target
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)
# X_train, X_test, y_train, y_test = train_test_split(
#     X_scaled, y, test_size=0.3, random_state=42
# )
# model = LinearRegression()
# model.fit(X_train, y_train)
# coefficients = pd.DataFrame({
#     'Feature': data.feature_names,
#     'Coefficient': model.coef_
# })
# print(coefficients)
#1. Дохід населення (MedInc: +0.85) — найсильніший фактор.
# Чим вищий медіанний дохід у регіоні, тим дорожче житло.
# Це логічно: заможніші люди можуть дозволити собі дорожчі будинки.
# 2. Географія має значення. Широта (Latitude: -0.89) та
# довгота (Longitude: -0.87) суттєво впливають на ціну.
# Рух на північ або на захід Каліфорнії пов'язаний із
# нижчими цінами — ймовірно, через клімат та економічні особливості регіонів.
# 3. Кількість спалень (AveBedrms: +0.37) — більше спалень означає більший будинок, а отже — вищу ціну.
# 4. Кількість кімнат (AveRooms: -0.30) — цікаво, що цей коефіцієнт негативний.
# Можливе пояснення: райони з великими будинками часто розташовані
# далі від центру, де ціни нижчі.
# 5. Вік будинку (HouseAge: +0.12) — старіші будинки трохи дорожчі.
# Це може бути пов'язано з їхнім розташуванням у престижних історичних районах.
# 6. Населення (Population: -0.001) та
# кількість мешканців на будинок (AveOccup: -0.04) майже не впливають на ціну.
# Хоча перенаселеність може бути ознакою менш престижних районів, цей
# вплив незначний.


# кількість кімнат і кількість спалень пов'язані
# Для виявлення цієї проблеми використовують показник VIF (Variance Inflation Factor)
# Якщо значення VIF > 10, це є ознакою сильної мультиколінеарності
data = fetch_california_housing()
X = data.data
y = data.target
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)
# vif_data = pd.DataFrame()
# vif_data["Feature"] = data.feature_names
# vif_data["VIF"] = [
#     variance_inflation_factor(X_scaled, i)
#     for i in range(X_scaled.shape[1])
# ]
# print(vif_data)
# plt.figure(figsize=(10,6))
# plt.bar(vif_data['Feature'], vif_data['VIF'])
# plt.xlabel('Ознака')
# plt.ylabel('VIF')
# plt.title('VIF')
# plt.xticks(rotation=45)
# plt.show()

# X = sm.add_constant(X)
# model = sm.OLS(y, X).fit()
# print(model.summary())

# p-value: менше 0.05 — ознака того, що
# ознака є статистично значущою
# і її можна використовувати в моделі
# R²: показує, яку частку
# залежності пояснює модель
# Для R²:
# > 0.7 — хороша модель
# 0.4–0.7 — задовільна
# < 0.4 — слабка модель


# ПРАКТИЧНІ ЗАВДАННЯ

# ЗАВДАННЯ 2
# Додати categorical_features по локації
# Порахувати X_final
# Розрахувати coefficients
# np.random.seed(0)
# data = {
#     'Area': np.random.uniform(500, 5000, size=250),
#     'Bedrooms': np.random.randint(1, 6, size=250),
#     'Age': np.random.randint(0, 100, size=250),
#     'Location': np.random.choice(['Urban', 'Suburban', 'Rural'], size=250),
#     'Price': np.random.randint(50000, 1000000, size=250)
# }
# df = pd.DataFrame(data)

# X = df.drop("Price", axis=1)
# y = df['Price']

# # !!!!!!!!!!!!!!categorical_features = ["Location"]
# encoder = OneHotEncoder(drop='first', sparse=False)
# # !!!!!!!!!!!!!encoder = OneHotEncoder(drop='first', sparse_output=False)
# X_encoded = encoder.fit_transform(X[categorical_features])
# X_encoded = encoder.fit_transform(X[categorical_features])
# encoded_columns = encoder.get_feature_names_out(categorical_features)
# X_encoded_df = pd.DataFrame(X_encoded, columns=encoded_columns)

# X_numeric = X[['Area', 'Bedrooms', 'Age']].reset_index(drop=True)
# scaler = StandardScaler()
# X_numeric_scaled = scaler.fit_transform(X_numeric)
# X_numeric_scaled_df = pd.DataFrame(X_numeric_scaled, columns=['Area_Scaled', 'Bedrooms_Scaled', 'Age_Scaled'])

# # !!!!!!!!!!!!!X_final = pd.concat([X_numeric_scaled_df, X_encoded_df], axis=1)
# X_train, X_test, y_train, y_test = train_test_split(
#     X_final, y, test_size=0.15, random_state=42
# )

# model = Ridge(alpha=1.0)
# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)

# mae = mean_absolute_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)
# print("Mean Absolute Error:", mae)
# print("R² Score:", r2)

# plt.scatter(y_test, y_pred, color='green')
# plt.xlabel('Фактична ціна')
# plt.ylabel('Прогнозована ціна')
# plt.title('Фактична vs Прогнозована ціна нерухомості')
# plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
# plt.show()

# # ____________________________
# # coefficients
# # coefficients = pd.DataFrame({
# #     'Feature': X_final.columns,
# #     'Coefficient': model.coef_
# # })
# # print(coefficients)
# # ----------------------------


# ЗАВДАННЯ 3
# Розрахувати X_numeric, X_numeric_scaled, X_numeric_scaled_df
# np.random.seed(1)
# data = {
#     'Advertising_Spend': np.random.uniform(1000, 20000, size=300),
#     'Store_Size': np.random.randint(500, 5000, size=300),
#     'Region': np.random.choice(['North', 'South', 'East', 'West'], size=300),
#     'Sales': np.random.randint(20000, 150000, size=300)
# }
# df = pd.DataFrame(data)

# X = df[['Advertising_Spend', 'Store_Size', 'Region']]
# y = df['Sales']

# encoder = OneHotEncoder(drop='first', sparse_output=False)
# categorical_features = ['Region']
# X_encoded = encoder.fit_transform(X[categorical_features])
# encoded_columns = encoder.get_feature_names_out(categorical_features)
# X_encoded_df = pd.DataFrame(X_encoded, columns=encoded_columns)

# X_numeric = X[['Advertising_Spend', 'Store_Size']].reset_index(drop=True)
# scaler = StandardScaler()
# X_numeric_scaled = scaler.fit_transform(X_numeric)
# X_numeric_scaled_df = pd.DataFrame(
#     X_numeric_scaled, columns=['Advertising_Spend_Scaled', 'Store_Size_Scaled']
# )

# X_final = pd.concat([X_numeric_scaled_df, X_encoded_df], axis=1)

# X_train, X_test, y_train, y_test = train_test_split(
#     X_final, y, test_size=0.2, random_state=1
# )

# model = Lasso(alpha=0.1)
# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)

# mae = mean_absolute_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)
# print("Mean Absolute Error:", mae)
# print("R² Score:", r2)

# plt.scatter(y_test, y_pred, color='red')
# plt.xlabel('Фактичні продажі')
# plt.ylabel('Прогнозовані продажі')
# plt.title('Фактичні vs Прогнозовані продажі')
# plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
# plt.show()

# coefficients = pd.DataFrame({
#     'Feature': X_final.columns,
#     'Coefficient': model.coef_
# })
# print(coefficients)


# ЗАВДАННЯ 4
# Намалювати графік Фактичне споживання енергії,
# додати Прогнозоване споживання енергії та
# порівняти Фактичне vs Прогнозоване споживання енергії
# np.random.seed(3)
# data = {
#     'Temperature': np.random.uniform(-10, 40, size=400),
#     'Humidity': np.random.uniform(20, 100, size=400),
#     'Wind_Speed': np.random.uniform(0, 20, size=400),
#     'Energy_Consumption': np.random.randint(100, 2000, size=400)
# }
# df = pd.DataFrame(data)

# X = df[['Temperature', 'Humidity', 'Wind_Speed']]
# y = df['Energy_Consumption']

# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)
# X_scaled_df = pd.DataFrame(X_scaled, columns=['Temperature_Scaled', 'Humidity_Scaled', 'Wind_Speed_Scaled'])

# X_train, X_test, y_train, y_test = train_test_split(
#     X_scaled_df, y, test_size=0.3, random_state=3
# )

# model = ElasticNet(alpha=1.0, l1_ratio=0.5, random_state=3)
# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)

# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)
# print("Mean Squared Error:", mse)
# print("R² Score:", r2)

# coefficients = pd.DataFrame({
#     'Feature': X_scaled_df.columns,
#     'Coefficient': model.coef_
# })
# print(coefficients)

# Графік 1: Фактичне споживання енергії
# plt.figure(figsize=(10, 4))
# plt.plot(y_test.values, color='blue', label='Фактичне споживання енергії')
# plt.xlabel('Індекс зразка')
# plt.ylabel('Споживання енергії')
# plt.title('Фактичне споживання енергії')
# plt.legend()
# plt.tight_layout()
# plt.show()

# Графік 2: Прогнозоване споживання енергії
# plt.figure(figsize=(10, 4))
# plt.plot(y_pred, color='orange', label='Прогнозоване споживання енергії')
# plt.xlabel('Індекс зразка')
# plt.ylabel('Споживання енергії')
# plt.title('Прогнозоване споживання енергії')
# plt.legend()
# plt.tight_layout()
# plt.show()

# Графік 3: Фактичне vs Прогнозоване споживання енергії
# plt.figure(figsize=(8, 6))
# plt.scatter(y_test, y_pred, color='green', alpha=0.6, label='Передбачення')
# plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', label='Ідеальна лінія')
# plt.xlabel('Фактичне споживання енергії')
# plt.ylabel('Прогнозоване споживання енергії')
# plt.title('Фактичне vs Прогнозоване споживання енергії')
# plt.legend()
# plt.tight_layout()
# plt.show()


# ЗАВДАННЯ 5
# np.random.seed(5)
# data = {
#     'R&D_Spend': np.random.uniform(10000, 60000, size=350),
#     'Administration_Spend': np.random.uniform(5000, 25000, size=350),
#     'Marketing_Spend': np.random.uniform(20000, 120000, size=350),
#     'State': np.random.choice(['New York', 'California', 'Florida', 'Texas'], size=350),
#     'Profit': np.random.randint(10000, 60000, size=350)
# }
# df = pd.DataFrame(data)

# X = df[['R&D_Spend', 'Administration_Spend', 'Marketing_Spend', 'State']]
# y = df['Profit']

# encoder = OneHotEncoder(drop='first', sparse_output=False)
# categorical_features = ['State']
# X_encoded = encoder.fit_transform(X[categorical_features])
# encoded_columns = encoder.get_feature_names_out(categorical_features)
# X_encoded_df = pd.DataFrame(X_encoded, columns=encoded_columns)

# X_numeric = X[['R&D_Spend', 'Administration_Spend', 'Marketing_Spend']].reset_index(drop=True)
# scaler = StandardScaler()
# X_numeric_scaled = scaler.fit_transform(X_numeric)
# X_numeric_scaled_df = pd.DataFrame(X_numeric_scaled, columns=['R&D_Spend_Scaled', 'Administration_Spend_Scaled', 'Marketing_Spend_Scaled'])

# X_final = pd.concat([X_numeric_scaled_df, X_encoded_df], axis=1)

# X_train, X_test, y_train, y_test = train_test_split(
#     X_final, y, test_size=0.2, random_state=5
# )

# model = Ridge(alpha=1.0)
# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)

# plt.scatter(y_test, y_pred, color='cyan')
# plt.xlabel('Фактичний прибуток')
# plt.ylabel('Прогнозований прибуток')
# plt.title('Фактичний vs Прогнозований прибуток стартапів')
# plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
# plt.show()

# coefficients = pd.DataFrame({
#     'Feature': X_final.columns,
#     'Coefficient': model.coef_
# })
# print(coefficients)
# # Розрахувати r2 та mean_absolute_error
# r2 = r2_score(y_test, y_pred)
# mae = mean_absolute_error(y_test, y_pred)
# print("R2 Score:", r2)
# print("Mean Absolute Error:", mae)




