import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# from sklearn.preprocessing import StandardScaler
# data = np.array([[1, 2], [3, 4], [5, 6]])
# scaler = StandardScaler()
# scaled_data = scaler.fit_transform(data)
# print(scaled_data)


# from sklearn.impute import SimpleImputer
# data = np.array([[1, 2], [np.nan, 4], [5, 6]])
# imputer = SimpleImputer(strategy="mean")
# imputed_data = imputer.fit_transform(data)
# print(imputed_data)


# from sklearn.preprocessing import OneHotEncoder
# categories = np.array([["red"], ["blue"], ["green"], ["blue"]])
# encoder = OneHotEncoder(sparse_output=False)
# encoded_cat = encoder.fit_transform(categories)
# print(encoded_cat)


# from sklearn.model_selection import train_test_split
# import random
# x = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
# y = np.array([0, 1, 0, 1])
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)
# print("Навчальні дані:", x_train, y_train)
# print("Тестові дані:", x_test, y_test)

# x, y = np.arange(1, 11).reshape(5, 2), [random.randint(0, 1) for _ in range(5)]
# print(x, y)
# x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.4, random_state=42)
# print("Навчальні дані:\n", x_train)
# print("Тестові дані:\n", x_test)
# print("Навчальні мітки:\n", y_train)
# print("Тестові мітки:\n", y_test)

# ЗАВДАННЯ 1: лінійна регресія
# from sklearn.linear_model import LinearRegression
# X = np.array([[50], [60], [70], [80], [90], [100]])
# Y = np.array([150000, 180000, 210000, 240000, 270000, 300000])
# model = LinearRegression()
# model.fit(X, Y)
# X_new = np.array([[55], [65], [85]])
# Y_pred = model.predict(X_new)

# plt.scatter(X, Y, label="Дані", color="blue")
# plt.scatter(X_new, Y_pred, label="Прогноз", color="green")
# plt.plot(X, model.predict(X), label="Лінія регресії")
# plt.xlabel("Площа квартири (кв.м.)")
# plt.ylabel("Ціна '$'")
# plt.legend()
# plt.show()

# ЗАВДАННЯ 2: Логістична регресія
# from sklearn.datasets import load_iris
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score, classification_report

# iris = load_iris()
# X = iris.data
# y = iris.target

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model = LogisticRegression(max_iter=200)
# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)

# print("Точність моделі:", accuracy_score(y_test, y_pred))
# print("Звіт класифікації:\\n", classification_report(y_test, y_pred))

# ЗАВДАННЯ 3: Алгоритм K-середніх - є потужним інструментом для кластеризації
# from sklearn.cluster import KMeans

# data = {
#     'Income': [15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
#     'Spending': [39, 81, 6, 77, 40, 76, 6, 94, 3, 72]
# }
# df = pd.DataFrame(data)
# k_means = KMeans(n_clusters=2, random_state=0)
# k_means.fit(df)
# df['Cluster'] = k_means.labels_
# plt.scatter(df['Income'], df['Spending'], c=df['Cluster'], cmap='viridis')
# plt.xlabel('Дохід (тис. доларів)')
# plt.ylabel('Витрати (тис. доларів)')
# plt.title('Кластеризація покупців за доходом та витратами')
# plt.show()

# ЗАВДАННЯ 4: Grid Search - обирає найкращий набір
# from sklearn.datasets import load_iris
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import GridSearchCV

# iris = load_iris()
# X = iris.data
# y = iris.target

# dt = DecisionTreeClassifier()
# param_grid = {
#     'max_depth': [3, 5, 7, None],
#     'min_samples_split': [2, 5, 10],
#     'min_samples_leaf': [1, 2, 4]
# }
# grid_search = GridSearchCV(estimator=dt, param_grid=param_grid, cv=5, scoring='accuracy')
# grid_search.fit(X, y)
# print("Найкращі параметри:", grid_search.best_params_)
# print("Найкраща точність:", grid_search.best_score_)


# ПРИКЛАДИ

# ЗАВДАННЯ 1
# Ви отримали дані про висоту та вагу людей, але деякі записи містять пропущені значення.
# Висота: [170, 165, None, 180, 175]
# Вага: [70, None, 60, 80, 75]
# Створити DataFrame з наданими даними.
# Заповнити пропущені значення середнім значенням за колонкою.
# Вивести оновлений DataFrame.

# from sklearn.impute import SimpleImputer
# data = {
#     "H": [170, 165, None, 180, 175],
#     "W": [70, None, 60, 80, 75]
# }
# df = pd.DataFrame(data)
# impute = SimpleImputer(strategy="mean")
# full_df = impute.fit_transform(df)
# print(full_df)

# ЗАВДАННЯ 2
# Ви маєте категоріальні дані про типи автомобілів, які потрібно перетворити на числовий формат для подальшого аналізу.
# Типи: ["Sedan", "SUV", "Coupe", "SUV", "Sedan"]
# Створити DataFrame з наданими даними.
# Використати OneHotEncoder для кодування категоріальних змінних.
# Вивести результат кодування.

# from sklearn.preprocessing import OneHotEncoder
# cat_avto = np.array(["Sedan", "SUV", "Coupe", "SUV", "Sedan"]).reshape(-1, 1)
# # cat_avto = np.array([["Sedan"], ["SUV"], ["Coupe"], ["SUV"], ["Sedan"]])
# # print(cat_avto)
# encoder = OneHotEncoder(sparse_output=False)
# encoded_data = encoder.fit_transform(cat_avto)
# print(encoded_data)

# ЗАВДАННЯ 3
# Ви працюєте з набором даних, який містить числові та категоріальні ознаки.
# Потрібно підготувати дані для навчання моделі машинного навчання.
# Вік: [25, 30, 22, 35, 28]
# Дохід: [50000, 60000, None, 80000, 55000]
# Стать: ["Male", "Female", "Female", "Male", "Female"]
# Створити DataFrame з наданими даними.
# Заповнити пропущені значення у колонці Дохід середнім значенням.
# Стандартизувати числові дані (Вік, Доход) за допомогою StandardScaler.
# Закодувати категоріальні дані (Стать) за допомогою LabelEncoder.
# Вивести готовий DataFrame.

# from sklearn.preprocessing import StandardScaler, LabelEncoder
# data = {
#     "Вік": [25, 30, 22, 35, 28],
#     "Дохід": [50000, 60000, None, 80000, 55000],
#     "Стать": ["Male", "Female", "Female", "Male", "Female"]
# }
# df = pd.DataFrame(data)
# df["Дохід"] = df["Дохід"].fillna(df["Дохід"].mean())
# scaler = StandardScaler()
# df[["Вік", "Дохід"]] = scaler.fit_transform(df[["Вік", "Дохід"]])
# encoder = LabelEncoder()
# df["Стать"] = encoder.fit_transform(df["Стать"])
# print(df)

# ЗАВДАННЯ 4
# Ви маєте дані про студентів, включаючи їхні оцінки та факультет.
# Необхідно підготувати дані для побудови моделі прогнозування успішності.
# Оцінка з математики: [88, 92, 79, None, 85]
# Оцінка з фізики: [90, None, 85, 80, 88]
# Факультет: ["Engineering", "Science", "Arts", "Science", "Engineering"]
# Створити DataFrame з наданими даними.
# Заповнити пропущені значення у колонках оцінок середнім значенням.
# Нормалізувати дані за допомогою MinMaxScaler.
# Використати OneHotEncoder для кодування категоріальної змінної Факультет.
# Об'єднати всі підготовлені дані та вивести результат.

from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
data = {
    "Оцінка з математики": [88, 92, 79, None, 85],
    "Оцінка з фізики": [90, None, 85, 80, 88],
    "Факультет": ["Engineering", "Science", "Arts", "Science", "Engineering"]
}
df = pd.DataFrame(data)
df["Оцінка з математики"] = df["Оцінка з математики"].fillna(df["Оцінка з математики"].mean())
df["Оцінка з фізики"] = df["Оцінка з фізики"].fillna(df["Оцінка з фізики"].mean())
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(df[["Оцінка з математики", "Оцінка з фізики"]])
encoder = OneHotEncoder(sparse_output=False)
encoded_data = encoder.fit_transform(df[["Факультет"]])
final_data = np.hstack((scaled_data, encoded_data))
print(final_data)