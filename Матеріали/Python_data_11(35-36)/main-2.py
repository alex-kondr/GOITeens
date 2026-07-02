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
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import statsmodels.api as sm
from statsmodels.graphics.regressionplots import plot_partregress


# -------------------------------------------------------
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

# -------------------------------------------------------
# ЗАВДАННЯ 1
# np.random.seed(0)
# data = {
#     'Area': np.random.uniform(500, 5000, size=250),
#     'Bedrooms': np.random.randint(1, 6, size=250),
#     'Age': np.random.randint(0, 100, size=250),
#     'Location': np.random.choice(['Urban', 'Suburban', 'Rural'], size=250),
#     'Price': np.random.randint(50000, 1000000, size=250)
# }
# Використовуючи набір даних real_estate_data, побудуйте модель лінійної регресії для прогнозування цін на нерухомість.
# Витягніть та відобразіть коефіцієнти моделі.
# Інтерпретуйте значення коефіцієнтів для ознак Area та Age.
# Визначте, які ознаки мають найбільший вплив на ціну нерухомості.
# Візуалізуйте фактичні та прогнозовані ціни за допомогою діаграми розсіювання.
# Оцініть модель за допомогою MSE та R².
# Проаналізуйте результати та зробіть висновки щодо якості моделі.

# df = pd.DataFrame(data)

# cat_col = ["Location"]
# encoder = OneHotEncoder(sparse_output=False, drop="first")
# X_encoded = encoder.fit_transform(df[cat_col])
# col_name = encoder.get_feature_names_out(cat_col)
# X_encoded_df = pd.DataFrame(X_encoded, columns=col_name)

# df_numeric = df.drop(columns=cat_col + ["Price"])
# scaler = StandardScaler()
# df_numeric_scaled = scaler.fit_transform(df_numeric)
# df_numeric_scaled_df = pd.DataFrame(df_numeric_scaled, columns=df_numeric.columns)

# X_final = pd.concat([X_encoded_df, df_numeric_scaled_df], axis=1)
# y = df["Price"]

# X_train, X_test, y_train, y_test = train_test_split(X_final, y, random_state=10, test_size=0.3)
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
# print("Intercept:", model.intercept_)

# coefficients = pd.DataFrame({
#     'Feature': X_final.columns,
#     'Coefficient': model.coef_
# })
# print("\nCoefficients:")
# print(coefficients)

# plt.scatter(y_test, y_pred, color="blue")
# plt.plot(y_test, y_test, color="red")
# plt.xlabel("Actual Price")
# plt.ylabel("Predicted Price")
# plt.title("Actual vs Predicted Price")
# plt.show()

# -------------------------------------------------------
# ЗАВДАННЯ 2
# np.random.seed(1)
# data = {
#     'Advertising_Spend': np.random.uniform(1000, 20000, size=300),
#     'Store_Size': np.random.randint(500, 5000, size=300),
#     'Region': np.random.choice(['North', 'South', 'East', 'West'], size=300),
#     'Sales': np.random.randint(20000, 150000, size=300)
# }
# Використовуючи набір даних marketing_data, побудуйте модель Ridge регресії для прогнозування продажів.
# Витягніть та проаналізуйте коефіцієнти моделі.
# Оцініть модель за допомогою MAE та R².
# Візуалізуйте фактичні та прогнозовані продажі.
# Обговоріть вплив різних ознак на прогнозовані продажі.


# -------------------------------------------------------
# ПОБУДОВА ГРАФІКІВ ДЛЯ ВІЗУАЛІЗАЦІЇ РЕГРЕСІЙНИХ ЛІНІЙ

# Діаграма розсіювання (Scatter Plot)
# np.random.seed(0)
# X = 2.5 * np.random.randn(100) + 1.5
# res = 0.5 * np.random.randn(100)
# y = 2 + 0.3 * X + res
# df = pd.DataFrame({'X': X, 'Y': y})
# plt.figure(figsize=(10,6))
# sns.regplot(x='X', y='Y', data=df, ci=None, line_kws={"color":"red"})
# plt.title('Діаграма розсіювання з регресійною лінією')
# plt.xlabel('Незалежна змінна X')
# plt.ylabel('Залежна змінна Y')
# plt.show()

# -------------------------------------------------------
# ДІАГРАМА ЗАЛИШКІВ (RESIDUAL PLOT)
# np.random.seed(0)
# X = 2.5 * np.random.randn(100) + 1.5
# res = 0.5 * np.random.randn(100)
# y = 2 + 0.3 * X + res
# model = LinearRegression()
# model.fit(X.reshape(-1,1), y)
# y_pred = model.predict(X.reshape(-1,1))
# residuals = y - y_pred

# plt.figure(figsize=(10,6))
# plt.scatter(y_pred, residuals, color='purple')
# plt.axhline(0, color='red', linestyle='--')
# plt.title('Діаграма залишків')
# plt.xlabel('Прогнозовані значення Y')
# plt.ylabel('Залишки')
# plt.show()

# -------------------------------------------------------
# ДІАГРАМА ВПЛИВУ (INFLUENCE PLOT)
# Великі кружечки у верхньому правому або нижньому правому кутах:
# Це спостереження з високим важелем (high leverage)
# та великим залишком (high residual).
# Вони найбільше викривлюють модель. Саме ці точки
# зазвичай потребують додаткової перевірки (можливо,
# це помилка вимірювання або запису даних).
# np.random.seed(0)
# X = 2.5 * np.random.randn(100) + 1.5
# res = 0.5 * np.random.randn(100)
# y = 2 + 0.3 * X + res
# X_sm = sm.add_constant(X)
# model_sm = sm.OLS(y, X_sm).fit()

# fig, ax = plt.subplots(figsize=(10,6))
# sm.graphics.influence_plot(model_sm, ax=ax, criterion="cooks")
# plt.title('Діаграма впливу')
# plt.show()

# -------------------------------------------------------
# ДІАГРАМА ПРЕДИКТОРА (PARTIAL REGRESSION PLOT)
# Діаграма предиктора відображає зв'язок між однією
# незалежною змінною та залежною змінною,
# при цьому враховуючи вплив інших незалежних змінних.
# np.random.seed(0)
# X = 2.5 * np.random.randn(100) + 1.5
# Z1 = np.random.randn(100)
# Z2 = np.random.randn(100)
# res = 0.5 * np.random.randn(100)
# y = 2 + 0.3 * X + 0.5 * Z1 - 0.2 * Z2 + res
# df = pd.DataFrame({'X': X, 'Y': y, 'Z1': Z1, 'Z2': Z2})
# fig, ax = plt.subplots(figsize=(10,6))
# plot_partregress('Y', 'X', ['Z1', 'Z2'], data=df, ax=ax)
# plt.title('Діаграма часткової регресії')
# plt.show()

# -------------------------------------------------------
# ДІАГРАМА ПЕРЕДБАЧЕНИХ ЗНАЧЕНЬ (PREDICTED VS ACTUAL PLOT)
# Діаграма передбачених значень відображає фактичні
# значення залежної змінної проти прогнозованих моделью.

# np.random.seed(0)
# X = 2.5 * np.random.randn(100) + 1.5
# res = 0.5 * np.random.randn(100)
# y = 2 + 0.3 * X + res

# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=10, test_size=0.3)
# model = LinearRegression()
# model.fit(X_train.reshape(-1,1), y_train)
# y_pred = model.predict(X_test.reshape(-1,1))

# plt.figure(figsize=(10,6))
# plt.scatter(y_test, y_pred, color='blue')
# plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
# plt.xlabel('Фактичні значення')
# plt.ylabel('Прогнозовані значення')
# plt.title('Фактичні vs Прогнозовані значення')
# plt.show()


# -------------------------------------------------------
# ЗАВДАННЯ 1
# Побудуйте діаграму розсіювання
# залежної змінної Y від незалежної змінної X
# з регресійною лінією

# np.random.seed(0)
# X = 3.2 * np.random.randn(100) + 0.5
# res = 0.4 * np.random.randn(100)
# y = 3 + 0.5 * X + res

# -------------------------------------------------------
# ЗАВДАННЯ 2
# ДІАГРАМА ВПЛИВУ (INFLUENCE PLOT)
# Навчіть лінійну регресійну модель за допомогою бібліотеки statsmodels.
# Побудуйте діаграму впливу, щоб виявити спостереження з великим впливом на модель.
# Проаналізуйте, які спостереження можуть бути впливовими аномаліями.
# np.random.seed(0)
# X = 3.2 * np.random.randn(100) + 0.5
# res = 0.4 * np.random.randn(100)
# y = 3 + 0.5 * X + res

# # 1. Додаємо константу (інтерцепт) та навчаємо модель OLS
# X_sm = sm.add_constant(X)
# model_sm = sm.OLS(y, X_sm).fit()
# # 2. Будуємо діаграму впливу
# fig, ax = plt.subplots(figsize=(10, 6))
# sm.graphics.influence_plot(model_sm, ax=ax, criterion="cooks")
# plt.title('Діаграма впливу (Завдання 2)')
# plt.show()
# # 3. Виводимо зведену таблицю моделі для аналізу
# print(model_sm.summary())

# -------------------------------------------------------
# ЗАВДАННЯ 4
# ДІАГРАМА ПРЕДИКТОРА (PARTIAL REGRESSION PLOT)
# Побудуйте діаграму часткової регресії
# для змінної X1, враховуючи вплив X2 на
# залежну змінну Y. Використовуйте бібліотеку
# statsmodels для створення часткової регресійної діаграми.
# np.random.seed(0)
# X1 = 2.5 * np.random.randn(100) + 1.5
# X2 = 1.5 * np.random.randn(100) + 2.0
# res = 0.5 * np.random.randn(100)
# y = 2 + 0.3 * X1 + 0.5 * X2 + res

# df = pd.DataFrame({'X1': X1, 'X2': X2, 'Y': y})

# Варіант-1
# fig, ax = plt.subplots(figsize=(10,6))
# plot_partregress('Y', 'X1', ['X2'], data=df, ax=ax)
# plt.title('Діаграма часткової регресії')
# plt.show()

# Варіант-2
# # 1. Додаємо константу
# X_sm = sm.add_constant(df[['X1', 'X2']])
# # 2. Навчаємо модель OLS
# model_sm = sm.OLS(df['Y'], X_sm).fit()
# # 3. Будуємо діаграму часткової регресії
# # Plotting Partial Regression Plot for X1
# fig, ax = plt.subplots(figsize=(10, 6))
# plot_partregress('Y', 'X1', ['X2'], data=df, ax=ax)
# plt.title('Діаграма часткової регресії (Завдання 4)')
# plt.show()


# -------------------------------------------------------
# ЗАВДАННЯ 5
# ДІАГРАМА ПЕРЕДБАЧЕНИХ ЗНАЧЕНЬ (PREDICTED VS ACTUAL PLOT)
# np.random.seed(0)
# X = 3 * np.random.randn(100) + 10
# res = 1.0 * np.random.randn(100)
# y = 5 + 2 * X + res

# df = pd.DataFrame({'X': X, 'Y': y})
# Навчіть лінійну регресійну модель для прогнозування Y на основі X.
# Розрахуйте прогнозовані значення Y (y_pred).
# Побудуйте діаграму передбачених значень Y проти фактичних значень Y.
# Додайте лінію 45 градусів для оцінки точності прогнозів.

# -------------------------------------------------------
# ЗАВДАННЯ 6
# np.random.seed(0)
# X1 = 2.0 * np.random.randn(100) + 3
# X2 = 1.0 * np.random.randn(100) + 2
# res = 0.5 * np.random.randn(100)
# y = 1 + 1.0 * X1 + 0.5 * X2 + res

# df = pd.DataFrame({'X1': X1, 'X2': X2, 'Y': y})
# Навчіть мультифакторну лінійну регресійну модель для прогнозування Y на основі X1 та X2.
# Побудуйте діаграму розсіювання з регресійними лініями для обох предикторів (X1 і X2).
# Побудуйте діаграму залишків для моделі.
# Побудуйте діаграму передбачених значень Y проти фактичних значень Y.
# Відобразіть коефіцієнти регресії на окремому графіку.

# 1. Навчаємо мультифакторну лінійну регресійну модель
# X = df[['X1', 'X2']]
# y = df['Y']

# model = LinearRegression()
# model.fit(X, y)
# y_pred = model.predict(X)
# residuals = y - y_pred

# # 2. Побудуємо діаграму розсіювання з регресійними лініями для обох предикторів
# fig, axes = plt.subplots(1, 2, figsize=(14, 6))
# sns.regplot(x='X1', y='Y', data=df, ax=axes[0], line_kws={'color': 'red'})
# axes[0].set_title('Залежність Y від X1')
# sns.regplot(x='X2', y='Y', data=df, ax=axes[1], line_kws={'color': 'red'})
# axes[1].set_title('Залежність Y від X2')
# plt.tight_layout()
# plt.show()

# # 3. Побудуємо діаграму залишків для моделі
# plt.figure(figsize=(10, 6))
# plt.scatter(y_pred, residuals)
# plt.axhline(y=0, color='r', linestyle='--')
# plt.xlabel('Передбачені значення')
# plt.ylabel('Залишки')
# plt.title('Діаграма залишків')
# plt.show()

# # 4. Побудуємо діаграму передбачених значень Y проти фактичних значень Y
# plt.figure(figsize=(10, 6))
# plt.scatter(y, y_pred)
# plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2)
# plt.xlabel('Фактичні значення')
# plt.ylabel('Передбачені значення')
# plt.title('Фактичні vs Передбачені значення')
# plt.show()

# # 5. Відобразимо коефіцієнти регресії на окремому графіку
# plt.figure(figsize=(8, 5))
# plt.bar(model.feature_names_in_, model.coef_)
# plt.ylabel('Коефіцієнти')
# plt.title('Коефіцієнти регресії для X1 та X2')
# plt.show()

# # Виводимо результати в консоль
# print("Коефіцієнти регресії:")
# for feature, coef in zip(model.feature_names_in_, model.coef_):
#     print(f"{feature}: {coef}")