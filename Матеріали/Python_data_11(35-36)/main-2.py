# Mean Squared Error (MSE)
# Середнє квадратичне відхилення між фактичними та прогнозованими значеннями.
# Формула: MSE = (1/n) * Σ(y_i - ŷ_i)²

# Coefficient of Determination (R²)
# Пояснює, яка частка дисперсії залежної змінної пояснюється незалежними змінними.
# Формула: R² = 1 - Σ(y_i - ŷ_i)² / Σ(y_i - ȳ)²


# Mean Absolute Error (MAE)
# Середня абсолютна помилка, менш чутлива до викидів, ніж MSE.
# Формула: MAE = (1/n) * Σ|y_i - ŷ_i|

# Root Mean Squared Error (RMSE)
# Квадратний корінь з MSE, має ту ж одиницю виміру, що й цільова змінна.
# Формула: RMSE = √MSE


# Завдання 1
# Дано: Набір фактичних та прогнозованих значень продажів за місяць:
# Спостереження,Фактичні продажі (yi​),Прогнозовані продажі (y^​i​)
# 1,150,160
# 2,200,195
# 3,250,245
# 4,300,310
# 5,350,340
# Розрахуйте Mean Squared Error (MSE).
# Розрахуйте Root Mean Squared Error (RMSE).


# Завдання 2:
# Розрахунок MAE та R^2
# Дано: Набір фактичних та прогнозованих значень температури у місті за тиждень:
# Спостереження,Фактична температура (yi),Прогнозована температура (y^i)
# 1,22,21
# 2,25,26
# 3,19,20
# 4,28,27
# 5,21,23
# Розрахуйте Mean Absolute Error (MAE).
# Розрахуйте Coefficient of Determination (R²).


# Завдання 3
# Дано: Набір фактичних та прогнозованих значень прибутку компанії за місяць:
# Спостереження,Фактичний прибуток (yi),Прогнозований прибуток (y^i)
# 1,100000,110000
# 2,120000,115000
# 3,150000,160000
# 4,130000,125000
# 5,180000,175000
# Розрахуйте MSE, RMSE, MAE та R2.
# Ідентифікуйте спостереження з найбільшими відхиленнями між фактичним та прогнозованим прибутком.
# Обговоріть можливі причини високих відхилень у цих спостереженнях.


# Завдання 4:
# Оцінка моделі з низьким R2
# Дано: Набір фактичних та прогнозованих значень температури у промисловій зоні:
# Спостереження,Фактична температура (yi​),Прогнозована температура (y^​i​)
# 1,35,30
# 2,40,38
# 3,30,32
# 4,45,40
# 5,50,45
# 6,55,50
# 7,60,58
# 8,65,60
# 9,70,65
# 10,75,70
# Розрахуйте MSE, RMSE, MAE та R2.
# Обговоріть, чому модель може мати низький R2 та що це означає.


# Завдання 5:
# Порівняння моделей
# Дано: Набір фактичних та прогнозованих значень площі будинку.
# Спостереження,Фактична площа (yi),Прогнозована площа Моделлю 1 (y^i),Прогнозована площа Моделлю 2 (y^i)
# 1,150,160,155
# 2,200,195,198
# 3,250,245,252
# 4,300,310,295
# 5,350,340,355
# 6,400,410,395
# 7,450,445,452
# 8,500,510,495
# 9,550,545,555
# 10,600,610,595
# Розрахуйте MSE та R² для обох моделей.
# Порівняйте продуктивність моделей та визначте, яка модель краще прогнозує площу будинку.


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error


# np.random.seed(42)
# data = {
#     'Years_Experience': np.random.randint(0, 40, size=200),
#     'Education_Level': np.random.choice(['High School', 'Bachelors', 'Masters', 'PhD'], size=200),
#     'Age': np.random.randint(22, 65, size=200),
#     'Department': np.random.choice(['Sales', 'Engineering', 'HR', 'Marketing'], size=200),
#     'Salary': np.random.randint(30000, 120000, size=200)
# }
# df = pd.DataFrame(data)

# cat_columns = ["Education_Level", "Department"]
# encoder = OneHotEncoder(sparse_output=False, drop="first")
# X_encoded = encoder.fit_transform(df[cat_columns])
# encoded_columns = encoder.get_feature_names_out(cat_columns)
# X_encoded_df = pd.DataFrame(X_encoded, columns=encoded_columns)

# X_numeric = df.drop(cat_columns, axis=1)
# scaler = StandardScaler()
# X_scaler = scaler.fit_transform(X_numeric)

# df = pd.concat([X_encoded_df, pd.DataFrame(X_scaler, columns=X_numeric.columns)], axis=1)
# X = df.drop(["Salary"], axis=1)
# y = df["Salary"]

# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=10, test_size=0.3)
# model = LinearRegression()
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# mse = mean_squared_error(y_test, y_pred)
# rmse = np.sqrt(mse)
# r2 = r2_score(y_test, y_pred)
# mae = mean_absolute_error(y_test, y_pred)
# print("Mean Squared Error:", mse)
# print("Root Mean Squared Error:", rmse)
# print("R² Score:", r2)
# print("Mean Absolute Error:", mae)

# plt.scatter(y_test, y_pred, color='purple')
# plt.xlabel('Фактична зарплата')
# plt.ylabel('Прогнозована зарплата')
# plt.title('Фактична vs Прогнозована зарплата працівників')
# plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
# plt.show()