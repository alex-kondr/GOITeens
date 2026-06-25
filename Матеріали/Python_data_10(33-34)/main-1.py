from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier, IsolationForest
from sklearn.discriminant_analysis import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.datasets import load_digits
from sklearn.preprocessing import LabelEncoder

# 1. Логістична регресія
# data = {
#     'Feature1': [2.5, 0.5, 2.2, 1.9, 3.1, 2.3, 2.0, 1.0, 1.5, 1.1],
#     'Feature2': [2.4, 0.7, 2.9, 2.2, 3.0, 2.7, 1.6, 1.1, 1.6, 0.9],
#     'Target': [1, 0, 1, 1, 1, 1, 0, 0, 0, 0]
# }
# df = pd.DataFrame(data)
# X = df[['Feature1', 'Feature2']]
# y = df['Target']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# model = LogisticRegression()
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# print(accuracy_score(y_test, y_pred))
# print("Звіт класифікації:\n", classification_report(y_test, y_pred, zero_division=0)

# 2. Дерева рішень
# data = {
#     'Feature1': [2.5, 0.5, 2.2, 1.9, 3.1, 2.3, 2.0, 1.0, 1.5, 1.1],
#     'Feature2': [2.4, 0.7, 2.9, 2.2, 3.0, 2.7, 1.6, 1.1, 1.6, 0.9],
#     'Target': [1, 0, 1, 1, 1, 1, 0, 0, 0, 0]
# }
# df = pd.DataFrame(data)
# X = df[['Feature1', 'Feature2']]
# y = df['Target']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# model = DecisionTreeClassifier(random_state=42)
# # DecisionTreeClassifier(): Ініціалізація моделі дерева рішень.
# # criterion: Критерій для розділення вузлів (наприклад, 'gini', 'entropy').
# # max_depth: Максимальна глибина дерева.
# # min_samples_split: Мінімальна кількість зразків, необхідна для розділення внутрішнього вузла.
# # min_samples_leaf: Мінімальна кількість зразків, необхідна для утворення листового вузла.

# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# print(accuracy_score(y_test, y_pred))
# print("Звіт класифікації:\n", classification_report(y_test, y_pred, zero_division=0))
# tree.plot_tree(model, feature_names=['Feature1', 'Feature2'], class_names=['0', '1'], filled=True)
# plt.show()

# 3. Метод опорних векторів (SVM)
# data = {
#     'Feature1': [2.5, 0.5, 2.2, 1.9, 3.1, 2.3, 2.0, 1.0, 1.5, 1.1],
#     'Feature2': [2.4, 0.7, 2.9, 2.2, 3.0, 2.7, 1.6, 1.1, 1.6, 0.9],
#     'Target': [1, 0, 1, 1, 1, 1, 0, 0, 0, 0]
# }
# df = pd.DataFrame(data)
# X = df[['Feature1', 'Feature2']]
# y = df['Target']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# model = SVC(kernel='linear', random_state=42)
# # SVC(): Ініціалізація моделі машинного навчання з підтримкою векторних машин.
# # kernel: Ядро, яке використовується для відображення даних у простір вищої вимірності (наприклад, 'linear', 'poly', 'rbf', 'sigmoid').
# # random_state: Початкове значення для генератора випадкових чисел, що використовується для відтворюваності результатів.
# # gamma: Параметр ядра (для 'rbf', 'poly' та 'sigmoid').
# # degree: Ступінь полінома (для 'poly' ядра).

# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# print(accuracy_score(y_test, y_pred))
# print("Звіт класифікації:\n", classification_report(y_test, y_pred, zero_division=0))

# # Створення простої візуалізації
# plt.scatter(X['Feature1'], X['Feature2'], c=y, cmap=plt.cm.Paired)
# plt.xlabel('Feature1')
# plt.ylabel('Feature2')
# plt.title('Візуалізація даних')
# plt.show()

# 4. Алгоритм найближчих сусідів (KNN)
# data = {
#     'Feature1': [2.5, 0.5, 2.2, 1.9, 3.1, 2.3, 2.0, 1.0, 1.5, 1.1],
#     'Feature2': [2.4, 0.7, 2.9, 2.2, 3.0, 2.7, 1.6, 1.1, 1.6, 0.9],
#     'Target': [1, 0, 1, 1, 1, 1, 0, 0, 0, 0]
# }
# df = pd.DataFrame(data)
# X = df[['Feature1', 'Feature2']]
# y = df['Target']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# model = KNeighborsClassifier(n_neighbors=3)
# # KNeighborsClassifier(): Ініціалізація моделі алгоритму k-найближчих сусідів.
# # n_neighbors: Кількість найближчих сусідів, яку слід враховувати (зазвичай непарне число).
# # metric: Метрика відстані, яка використовується для визначення найближчих сусідів (наприклад, 'euclidean', 'manhattan').
# # weights: Ваги, що застосовуються до сусідів (наприклад, 'uniform', 'distance').

# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# print(accuracy_score(y_test, y_pred))
# print("Звіт класифікації:\n", classification_report(y_test, y_pred, zero_division=0))


# Розглянемо задачу класифікації клієнтів банку за допомогою алгоритму KNN.
# bank_data = {
#     "Age": [25, 45, 35, 50, 23, 43, 36, 29, 60, 38],
#     "Income": [50000, 80000, 60000, 120000, 40000, 75000, 65000, 48000, 110000, 70000],
#     "Credit_Score": [650, 700, 680, 720, 640, 710, 690, 660, 730, 700],
#     "Opened_Credit": [0, 1, 1, 1, 0, 1, 1, 0, 1, 1]
# }
# df = pd.DataFrame(bank_data)
# X = df[['Age', 'Income', 'Credit_Score']]
# y = df['Opened_Credit']
# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
# model = KNeighborsClassifier(n_neighbors=3, weights='uniform', algorithm='auto', p=2)
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# print(accuracy_score(y_test, y_pred))
# print("Звіт класифікації:\n", classification_report(y_test, y_pred, zero_division=0))


# ЗАВДАННЯ 1
# Ви отримали набір даних про квіти Іриса і
# хочете побудувати модель логістичної регресії для класифікації видів квітів.
# Набір даних iris з колонками ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
# Імпортувати необхідні бібліотеки.
# Завантажити набір даних iris з бібліотеки Scikit-learn.
# Перетворити цільову змінну species на числовий формат.
# Розділити дані на навчальний та тестовий набори.
# Створити та навчити модель логістичної регресії.
# Прогнозувати види квітів на тестових даних.
# Оцінити точність моделі.

# from sklearn.datasets import load_iris
# df = load_iris()
# X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
# y = df['species']
# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
# model = LogisticRegression()
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# print(accuracy_score(y_test, y_pred))


# ЗАВДАННЯ 3.
# Ви маєте набір даних про клієнтів банку і хочете побудувати модель SVM для прогнозування,
# чи клієнт відкриє кредитну картку.
# DataFrame bank_data з колонками ["Age", "Income", "Credit_Score", "Opened_Credit"]:
# Age: вік клієнта.
# Income: річний дохід клієнта.
# Credit_Score: кредитний рейтинг клієнта.
# Opened_Credit: 1 (відкрив) або 0 (не відкрив).
# Імпортувати необхідні бібліотеки.
# Створити DataFrame з наданими даними.
# Розділити дані на ознаки та цільову змінну.
# Масштабувати дані за допомогою StandardScaler.
# Розділити дані на навчальний та тестовий набори.
# Створити та навчити модель SVM з ядром rbf.
# Прогнозувати результати на тестових даних.
# Оцінити точність моделі.

# bank_data = {
#     "Age": [25, 45, 35, 50, 23, 43, 36, 29, 60, 38],
#     "Income": [50000, 80000, 60000, 120000, 40000, 75000, 65000, 48000, 110000, 70000],
#     "Credit_Score": [650, 700, 680, 720, 640, 710, 690, 660, 730, 700],
#     "Opened_Credit": [0, 1, 1, 1, 0, 1, 1, 0, 1, 1]
# }
# df = pd.DataFrame(bank_data)
# X = df[["Age", "Income", "Credit_Score"]]
# y = df["Opened_Credit"]
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)
# X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, random_state=42)
# model = SVC(kernel="rbf")
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# print(accuracy_score(y_test, y_pred))


# ЗАВДАННЯ 4
# Ви маєте набір даних про фрукти і хочете
# побудувати модель KNN для класифікації типу фрукта на основі його характеристик.
# DataFrame fruit_data з колонками ["Weight", "Color_Score", "Texture_Score", "Fruit_Type"]:
# Weight: вага фрукта в грамах.
# Color_Score: оцінка кольору (1-10).
# Texture_Score: оцінка текстури (1-10).
# Fruit_Type: тип фрукта ("Apple", "Banana", "Cherry").
# Імпортувати необхідні бібліотеки.
# Створити DataFrame з наданими даними.
# Перетворити цільову змінну Fruit_Type на числовий формат.
# Розділити дані на ознаки та цільову змінну.
# Масштабувати дані за допомогою StandardScaler.
# Розділити дані на навчальний та тестовий набори.
# Створити та навчити модель KNN з n_neighbors=3.
# Прогнозувати типи фруктів на тестових даних.
# Оцінити точність моделі.

# data = {
#     "Weight": [150, 170, 140, 130, 120, 115, 15, 10, 12],
#     "Color_Score": [7, 8, 7, 9, 8, 9, 2, 3, 2],
#     "Texture_Score": [8, 7, 9, 3, 2, 3, 5, 6, 5],
#     "Fruit_Type": ["Apple", "Apple", "Apple", "Banana", "Banana", "Banana", "Cherry", "Cherry", "Cherry"]
# }
# df = pd.DataFrame(data)
# X = df[["Weight", "Color_Score", "Texture_Score"]]
# y = df["Fruit_Type"]
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)
# X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, random_state=42)
# model = KNeighborsClassifier(n_neighbors=3)
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# print(accuracy_score(y_test, y_pred))


# ЗАВДАННЯ 5.
# Ви хочете оптимізувати параметри моделі SVM для
# досягнення найкращої точності класифікації на наборі даних про рукописні цифри.
# Набір даних digits з бібліотеки Scikit-learn.
# Імпортувати необхідні бібліотеки.
# Завантажити набір даних digits.
# Розділити дані на ознаки та цільову змінну.
# Масштабувати дані за допомогою StandardScaler.
# Розділити дані на навчальний та тестовий набори.
# Використати GridSearchCV для пошуку оптимальних параметрів C та gamma для SVM з ядром rbf.
# Навчити оптимізовану модель.
# Прогнозувати класи на тестових даних.
# Оцінити точність моделі.
# Вивести найкращі параметри.

# from sklearn.datasets import load_digits
# data = load_digits()
# X = data.data
# y = data.target
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)
# X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, random_state=42)
# param_grid = {'C': [0.1, 1, 10], 'gamma': [0.01, 0.1, 1], 'kernel': ['rbf']}
# grid = GridSearchCV(SVC(), param_grid, cv=5)
# grid.fit(X_train, y_train)
# print("Найкращі параметри:", grid.best_params_)
# y_pred = grid.predict(X_test)
# print("Точність:", accuracy_score(y_test, y_pred))


# ПРИКЛАД 1
# Використаємо набір даних Іриса для
# класифікації видів квітів за допомогою логістичної регресії.
# iris = load_iris()
# X = pd.DataFrame(data=iris.data, columns=iris.feature_names)
# y = iris.target
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# model = LogisticRegression(max_iter=200)
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# print("Точність моделі:", accuracy_score(y_test, y_pred))
# print("Звіт класифікації:\n", classification_report(y_test, y_pred))


# ПРИКЛАД 2
# Виноробство є важливою галуззю,
# яка значною мірою залежить від якості вина.
# Ось приклад використання SVC для класифікації вина:
# from sklearn.datasets import load_wine

# data = load_wine()
# X = pd.DataFrame(data=data.data, columns=data.feature_names)
# y = data.target
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)
# X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)
# model = LogisticRegression(max_iter=200)
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# print("Точність моделі:", accuracy_score(y_test, y_pred))
# print("Звіт класифікації:\n", classification_report(y_test, y_pred))


# ПРИКЛАД 3
# Виявлення їстівних грибів від небезпечних
# для здоров'я є важливим завданням у галузі ботаніки та безпеки харчових продуктів.
# Ось приклад використання SVC для класифікації грибів:
# from ucimlrepo import fetch_ucirepo

# data = fetch_ucirepo(id=73).data
# le = LabelEncoder()
# for col in data.features.columns:
#     data.features[col] = le.fit_transform(data.features[col])

# # print(data.features.head())
# X = data.features
# y = le.fit_transform(data.targets)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# model = RandomForestClassifier(n_estimators=100, random_state=42)
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# print("Точність моделі:", accuracy_score(y_test, y_pred))
# print("Звіт класифікації:\n", classification_report(y_test, y_pred))



# ПРИКЛАД 3-1
# Класифікація електронних книг від паперових
# є важливим завданням у галузі електронної комерції
# та видавничої справи. Ось приклад використання SVC для класифікації книг:
# from sklearn.datasets import load_book

# data = load_book()
# X = pd.DataFrame(data=data.data, columns=data.feature_names)
# y = data.target
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)
# X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)
# model = SVC(kernel='rbf')
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# print("Точність моделі:", accuracy_score(y_test, y_pred))
# print("Звіт класифікації:\n", classification_report(y_test, y_pred))


# ПРИКЛАД 4
# Ми використаємо набір даних digits з бібліотеки Scikit-learn,
# який містить зображення рукописних цифр та їхні відповідні мітки
# digits = load_digits()
# X = digits.data
# y = digits.target
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)
# X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
# model = SVC(kernel='rbf', C=10, gamma=0.001)
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# print("Точність моделі:", accuracy_score(y_test, y_pred))
# print("Звіт класифікації:\n", classification_report(y_test, y_pred))

# fig, axes = plt.subplots(2, 5, figsize=(10, 5))
# axes = axes.flatten()
# for i, ax in enumerate(axes):
#     img = X_test[i].reshape(8, 8)
#     ax.imshow(img, cmap='gray')
#     ax.set_title(f"Pred: {y_pred[i]}")
#     ax.axis('off')
# plt.tight_layout()
# plt.show()


# ПРИКЛАД 5
# Шахрайство у фінансових транзакціях є
# серйозною проблемою для банків та фінансових установ.
# try:
#     fraud = pd.read_csv("creditcard.csv")
# except FileNotFoundError:
#     print("Файл creditcard.csv не знайдено. Будь ласка, переконайтесь, що файл знаходиться в поточній директорії або вкажіть правильний шлях до файлу.")

# X = fraud.drop('Class', axis=1)
# y = fraud['Class']

# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)
# X_train, X_test, y_train, y_test = train_test_split(
#     X_scaled, y, test_size=0.3, random_state=42, stratify=y
# )
# model = IsolationForest(contamination=0.001, random_state=42)
# model.fit(X_train)
# y_pred = model.predict(X_test)
# y_pred = [1 if x == -1 else 0 for x in y_pred]
# print("Точність моделі:", accuracy_score(y_test, y_pred))
# print("Звіт класифікації:\n", classification_report(y_test, y_pred))
# print("Матриця плутанини:\n", confusion_matrix(y_test, y_pred))


# ПРИКЛАД 6
# Автоматичне фільтрування спаму є важливим завданням
# для забезпечення чистоти та безпеки електронної пошти
# sms = pd.read_csv("spam.csv", sep='\\t', header=None, names=['label', 'message'], encoding='ISO-8859-1')
# sms['label_num'] = sms.label.map({'ham': 0, 'spam': 1})
# X = sms['message']
# y = sms['label_num']
# vectorizer = TfidfVectorizer(stop_words='english')
# X_vectorized = vectorizer.fit_transform(X)
# X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.3, random_state=42)
# model = MultinomialNB()
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# print("Точність моделі:", accuracy_score(y_test, y_pred))
# print("Звіт класифікації:\n", classification_report(y_test, y_pred))
# print("Матриця плутанини:\n", confusion_matrix(y_test, y_pred))



# ЗАВДАННЯ 1
# Завдання: Змініть 1 рядок коду, щоб використовувати LabelEncoder для кодування цільової змінної Fruit_Type.
# fruit_data = {
#     "Weight": [150, 120, 130, 160, 140, 170, 110, 180, 115, 155],
#     "Color_Score": [7, 6, 8, 9, 7, 10, 5, 9, 6, 8],
#     "Texture_Score": [6, 5, 7, 8, 6, 9, 4, 8, 5, 7],
#     "Fruit_Type": ["Apple", "Banana", "Cherry", "Apple", "Cherry", "Apple", "Banana", "Apple", "Banana", "Cherry"]
# }
# df = pd.DataFrame(fruit_data)

# X = df[['Weight', 'Color_Score', 'Texture_Score']]
# y = df['Fruit_Type']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# model = KNeighborsClassifier(n_neighbors=3)
# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)
# print("Точність моделі:", accuracy_score(y_test, y_pred))




# ЗАВДАННЯ 2
# Завдання: Додайте рядки коду для векторизації тексту за допомогою TfidfVectorizer.
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.metrics import accuracy_score, classification_report
# from sklearn.feature_extraction.text import TfidfVectorizer

# sms = pd.read_csv('sms_spam.csv')

# X = sms['message']
# y = sms['label_num']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# # Векторизація тексту
# # Додайте рядки тут

# model = MultinomialNB()
# model.fit(X_train_vectorized, y_train)

# y_pred = model.predict(X_test_vectorized)
# print("Точність моделі:", accuracy_score(y_test, y_pred))



# ЗАВДАННЯ 3
# Завдання: Додайте рядок коду для встановлення параметра random_state=42 у функцію train_test_split.
# digits = load_digits()
# X = digits.data
# y = digits.target

# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)

# X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3)

# param_grid = {
#     'C': [0.1, 1, 10, 100],
#     'gamma': [1, 0.1, 0.01, 0.001]
# }

# grid = GridSearchCV(SVC(kernel='rbf'), param_grid, refit=True, verbose=0, cv=5)
# grid.fit(X_train, y_train)

# y_pred = grid.predict(X_test)
# print("Точність моделі:", accuracy_score(y_test, y_pred))
# print("Звіт класифікації:\\n", classification_report(y_test, y_pred))
# print("Найкращі параметри:", grid.best_params_)


