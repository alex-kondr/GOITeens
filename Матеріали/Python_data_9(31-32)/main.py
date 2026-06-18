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
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

iris = load_iris()
X = iris.data
y = iris.target

dt = DecisionTreeClassifier()
param_grid = {
    'max_depth': [3, 5, 7, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}
grid_search = GridSearchCV(estimator=dt, param_grid=param_grid, cv=5, scoring='accuracy')
grid_search.fit(X, y)
print("Найкращі параметри:", grid_search.best_params_)
print("Найкраща точність:", grid_search.best_score_)