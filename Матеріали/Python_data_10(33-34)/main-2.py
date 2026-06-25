from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingClassifier
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
from sklearn.datasets import load_iris, make_classification, load_digits
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import roc_curve, auc
from imblearn.over_sampling import SMOTE # imbalanced-learn
import seaborn as sns


# Метрики для оцінки точності
# Популярні метрики для оцінки точності

# 1. Точність (Accuracy)
# Точність визначає відсоток правильно передбачених класів серед усіх передбачень
# формула: accuracy = (TP + TN) / (TP + TN + FP + FN)

# 2. Повнота (Recall)
# Повнота (або чутливість) вимірює здатність моделі виявити всі позитивні випадки
# формула: recall = TP / (TP + FN)

# 3. Точність (Precision)
# Точність вимірює точність позитивних передбачень
# формула: precision = TP / (TP + FP)

# 4. F-міра (F-Score)
# F-міра є середнім гармонійним між точністю і повнотою
# формула: f1_score = 2 * (precision * recall) / (precision + recall)


# ЗАВДАННЯ 1
# Вам надано результати роботи класифікаційної моделі:
# TP = 85  # True Positives (Істинно позитивні)
# TN = 55  # True Negatives (Істинно негативні)
# FP = 15  # False Positives (Хибно позитивні)
# FN = 5   # False Negatives (Хибно негативні)
# Розрахуйте точність моделі.
# Розрахуйте повноту моделі.
# Розрахуйте точність (Precision).
# Розрахуйте F1-міру.
# Напишіть Python-скрипт, який обчислює ці метрики за допомогою формул.

# 2.1 Точність (Accuracy)
# Формула: (TP + TN) / (TP + TN + FP + FN)
# accuracy = (TP + TN) / (TP + TN + FP + FN)

# 2.2 Повнота (Recall)
# Формула: TP / (TP + FN)
# recall = TP / (TP + FN)

# 2.3 Точність (Precision)
# Формула: TP / (TP + FP)
# precision = TP / (TP + FP)

# 2.4 F1-міра (F1-Score)
# Формула: 2 * (precision * recall) / (precision + recall)
# f1_score = 2 * (precision * recall) / (precision + recall)

# 3. Виведення результатів
# print("--- Розраховані метрики ---")
# print(f"1. Точність (Accuracy): {accuracy:.4f} (або {accuracy*100:.2f}%)")
# print(f"2. Повнота (Recall): {recall:.4f} (або {recall*100:.2f}%)")
# print(f"3. Точність (Precision): {precision:.4f} (або {precision*100:.2f}%)")
# print(f"4. F1-міра (F1-Score): {f1_score:.4f} (або {f1_score*100:.2f}%)")


# ROC-КРИВА ТА AUC ВІДПОВІДАЮТЬ НА ЗАПИТАННЯ:
# Як модель працює на всіх можливих порогах?
# Як добре модель відокремлює позитивний і негативний класи?
# Чим вище AUC, тим краще модель здатна розділяти класи. Наприклад:
# AUC = 0.9: Висока якість класифікації.
# AUC = 0.7: Прийнятна якість.
# AUC = 0.5: Класи не розділяються.
# X, y = make_classification(n_samples=1000, n_features=20, random_state=42)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# model = RandomForestClassifier(random_state=42)
# model.fit(X_train, y_train)
# y_prob = model.predict_proba(X_test)[:, 1]
# fpr, tpr, thresholds = roc_curve(y_test, y_prob)
# roc_auc = auc(fpr, tpr)

# plt.figure()
# plt.plot(fpr, tpr, label=f'ROC-крива (AUC = {roc_auc:.2f})')
# plt.plot([0, 1], [0, 1], linestyle='--', color='gray')
# plt.xlabel('False Positive Rate')
# plt.ylabel('True Positive Rate')
# plt.title('ROC-крива')
# plt.legend()
# plt.show()


# ======================= ЗАВДАННЯ 1 =======================
# Використовуючи бібліотеку sklearn.datasets, згенеруйте набір даних із 1000 зразків, 20 ознак та 2 класів.
# Розділіть дані на тренувальний (70%) та тестовий (30%) набори.
# Навчіть модель класифікації (наприклад, RandomForestClassifier).
# Розрахуйте ROC-криву та AUC для тестових даних.
# Побудуйте графік ROC-кривої та проаналізуйте значення AUC.

# X, y = make_classification(n_samples=1000, n_features=20, random_state=42)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# model = RandomForestClassifier(random_state=42)
# model.fit(X_train, y_train)
# y_prob = model.predict_proba(X_test)[:, 1]
# fpr, tpr, thresholds = roc_curve(y_test, y_prob)
# roc_auc = auc(fpr, tpr)

# plt.figure()
# plt.plot(fpr, tpr, label=f'ROC-крива (AUC = {roc_auc:.2f})')
# plt.plot([0, 1], [0, 1], linestyle='--', color='gray')
# plt.xlabel('False Positive Rate')
# plt.ylabel('True Positive Rate')
# plt.title('ROC-крива')
# plt.legend()
# plt.show()



# ======================= ЗАВДАННЯ 2 =======================

# Використайте той самий синтетичний набір даних, що і в Завданні 1.
# Створіть та навчіть дві різні моделі:
# RandomForestClassifier
# LogisticRegression
# Побудуйте ROC-криві для обох моделей на одному графіку.
# Обчисліть AUC для кожної моделі та порівняйте їхню якість.

# X, y = make_classification(n_samples=1000, n_features=20, random_state=42)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# model1 = RandomForestClassifier(random_state=42)
# model1.fit(X_train, y_train)
# y_prob1 = model1.predict_proba(X_test)[:, 1]
# fpr1, tpr1, thresholds1 = roc_curve(y_test, y_prob1)
# roc_auc1 = auc(fpr1, tpr1)

# model2 = LogisticRegression(random_state=42)
# model2.fit(X_train, y_train)
# y_prob2 = model2.predict_proba(X_test)[:, 1]
# fpr2, tpr2, thresholds2 = roc_curve(y_test, y_prob2)
# roc_auc2 = auc(fpr2, tpr2)

# plt.figure()
# plt.plot(fpr1, tpr1, label=f'ROC-крива RandomForestClassifier (AUC = {roc_auc1:.2f})')
# plt.plot(fpr2, tpr2, label=f'ROC-крива LogisticRegression (AUC = {roc_auc2:.2f})')
# plt.plot([0, 1], [0, 1], linestyle='--', color='gray')
# plt.xlabel('False Positive Rate')
# plt.ylabel('True Positive Rate')
# plt.title('ROC-крива')
# plt.legend()
# plt.show()


# ======================= ЗАВДАННЯ 3 =======================
# Завантажте датасет із відкритих джерел, наприклад, Heart Disease UCI Dataset.
# Проведіть попередню обробку даних:
# Заповніть пропущені значення.
# Закодуйте категоріальні змінні.
# Масштабуйте числові дані.
# Розділіть дані на тренувальний та тестовий набори.
# Навчіть класифікаційну модель та побудуйте ROC-криву для оцінки якості моделі.
# Проаналізуйте значення AUC та зробіть висновки.

# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"
# df = pd.read_csv(url, header=None)
# df.columns = [
#     "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
#     "thalach", "exang", "oldpeak", "slope", "ca", "thal", "target"
# ]

# df = df.replace("?", np.nan)
# df = df.apply(pd.to_numeric)
# df = df.fillna(df.median())

# X = df.drop("target", axis=1)
# y = (df["target"] > 0).astype(int)
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.3, random_state=42
# )

# model = RandomForestClassifier(random_state=42)
# model.fit(X_train, y_train)
# y_prob = model.predict_proba(X_test)[:, 1]
# fpr, tpr, thresholds = roc_curve(y_test, y_prob)
# roc_auc = auc(fpr, tpr)
# plt.figure()
# plt.plot(fpr, tpr, label=f'ROC-крива (AUC = {roc_auc:.2f})')
# plt.plot([0, 1], [0, 1], linestyle='--', color='gray')
# plt.xlabel('False Positive Rate')
# plt.ylabel('True Positive Rate')
# plt.title('ROC-крива')
# plt.legend()
# plt.show()


# ======================= ЗАВДАННЯ 5 =======================
# Створіть синтетичний набір даних із 1000 зразків, де один клас становить 90% даних.
# Навчіть модель класифікації (наприклад, GradientBoostingClassifier) на цьому наборі даних.
# Розрахуйте ROC-криву та AUC для тестових даних.
# Проаналізуйте, як незбалансованість даних впливає на ROC-криву та AUC.
# Спробуйте збалансувати дані (наприклад, використовуючи техніки oversampling або class_weight) і повторіть оцінку.

# X, y = make_classification(
#     n_samples=1000,
#     n_features=20,
#     weights=[0.9, 0.1],
#     random_state=42
# )

# # Розділяємо дані на тренувальну та тестову вибірки
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# print(f"Розподіл класів у тренувальній вибірці: {np.bincount(y_train)}")

# # --- КРОК 2: Навчання GradientBoostingClassifier на незбалансованих даних ---
# model_imbalanced = GradientBoostingClassifier(random_state=42)
# model_imbalanced.fit(X_train, y_train)

# # Отримуємо ймовірності для позитивного класу (клас 1)
# y_pred_proba_imb = model_imbalanced.predict_proba(X_test)[:, 1]

# # Розрахунок ROC-кривої та AUC
# fpr_imb, tpr_imb, _ = roc_curve(y_test, y_pred_proba_imb)
# roc_auc_imb = auc(fpr_imb, tpr_imb)

# # --- КРОК 3: Збалансування даних (техніка Oversampling за допомогою SMOTE) ---
# # SMOTE штучно генерує нові зразки меншинного класу для вирівнювання балансу
# smote = SMOTE(random_state=42)
# X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

# print(f"Розподіл класів після SMOTE: {np.bincount(y_train_res)}")

# # Навчаємо нову модель на збалансованих даних
# model_balanced = GradientBoostingClassifier(random_state=42)
# model_balanced.fit(X_train_res, y_train_res)

# # Отримуємо ймовірності для збалансованої моделі
# y_pred_proba_bal = model_balanced.predict_proba(X_test)[:, 1]

# # Розрахунок нових точок ROC та AUC
# fpr_bal, tpr_bal, _ = roc_curve(y_test, y_pred_proba_bal)
# roc_auc_bal = auc(fpr_bal, tpr_bal)

# # --- КРОК 4: Побудова графіків ROC-кривих для порівняння ---
# plt.figure(figsize=(8, 6))
# plt.plot(fpr_imb, tpr_imb, color='red', lw=2, label=f'Незбалансовані дані (AUC = {roc_auc_imb:.2f})')
# plt.plot(fpr_bal, tpr_bal, color='green', lw=2, label=f'Збалансовані дані SMOTE (AUC = {roc_auc_bal:.2f})')
# plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Випадкове вгадування')

# plt.xlim([0.0, 1.0])
# plt.ylim([0.0, 1.05])
# plt.xlabel('False Positive Rate (FPR)')
# plt.ylabel('True Positive Rate (TPR)')
# plt.title('Порівняння ROC-кривих')
# plt.legend(loc="lower right")
# plt.grid(True)
# plt.show()

# # Додатково виведемо текстовий звіт для глибокого аналізу
# print("\nЗвіт класифікації для НЕЗБАЛАНСОВАНОЇ моделі:")
# print(classification_report(y_test, model_imbalanced.predict(X_test)))

# print("\nЗвіт класифікації для ЗБАЛАНСОВАНОЇ моделі:")
# print(classification_report(y_test, model_balanced.predict(X_test)))
# =====================================================================


# ======================= ПРИКЛАД 2 =======================
# Розглянемо приклад створення та аналізу матриці плутанини за допомогою мови програмування Python та бібліотеки scikit-learn.
# data = {
#     "Age": [25, 45, 35, 50, 23, 43, 36, 29, 60, 38],
#     "Income": [50000, 80000, 60000, 120000, 40000, 75000, 65000, 48000, 110000, 70000],
#     "Credit_Score": [650, 700, 680, 720, 640, 710, 690, 660, 730, 700],
#     "Opened_Credit": [0, 1, 1, 1, 0, 1, 1, 0, 1, 1]
# }
# df = pd.DataFrame(data)
# # print("Перші рядки датасету:")
# # print(df.head())
# X = df[['Age', 'Income', 'Credit_Score']]
# y = df['Opened_Credit']
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y,
#     test_size=0.3,
#     random_state=42,
#     stratify=y
# )
# scaler = StandardScaler()
# X_train_scaled = scaler.fit_transform(X_train)
# X_test_scaled = scaler.transform(X_test)
# model = RandomForestClassifier(n_estimators=100, random_state=42)
# model.fit(X_train_scaled, y_train)
# y_pred = model.predict(X_test_scaled)
# accuracy = accuracy_score(y_test, y_pred)
# print("Точність моделі:", accuracy)
# report = classification_report(y_test, y_pred)
# print("Звіт класифікації:\n", report)

# cm = confusion_matrix(y_test, y_pred)
# sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Не відкрив кредит', 'Відкрив кредит'], yticklabels=['Не відкрив кредит', 'Відкрив кредит'])
# plt.ylabel('Справжній клас')
# plt.xlabel('Передбачений клас')
# plt.title('Конфузійна матриця')
# plt.show()
# =====================================================================


# ======================= ЗАВДАННЯ 1 =======================
# Дано:
# Набір даних credit_data з колонками ["Age", "Income", "Credit_Score", "Credit_Approved"]
# data = {
#     'Age': np.random.randint(18, 70, size=100),
#     'Income': np.random.randint(30000, 70000, size=100),
#     'Credit_Score': np.random.randint(300, 850, size=100),
#     'Credit_Approved': np.random.choice([0, 1], size=100, p=[0.5, 0.5])
# }
# # Завдання:
# # Розділити дані на навчальні та тестові набори.
# # Навчити модель логістичної регресії.
# # Використати модель для прогнозування на тестових даних.
# # Створити і вивести конфузійну матрицю.
# # Оцінити точність моделі.
# df = pd.DataFrame(data)
# # Розділення даних на навчальні та тестові набори
# X = df[["Age", "Income", "Credit_Score"]]
# y = df["Credit_Approved"]
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y,
#     test_size=0.3,
#     random_state=42,
#     stratify=y  # Важливо для балансування класів
# )
# # Навчання моделі логістичної регресії
# model = LogisticRegression()
# model.fit(X_train, y_train)
# # Прогнозування на тестових даних
# y_pred = model.predict(X_test)
# # Виведення конфузійної матриці
# cm = confusion_matrix(y_test, y_pred)
# print("Конфузійна матриця:\n", cm)
# # Оцінка точності моделі
# accuracy = accuracy_score(y_test, y_pred)
# print("Точність моделі:", accuracy)
# =====================================================================


# ======================= ЗАВДАННЯ 2 =======================
# Дано:
# Набір даних housing_data з колонками ["Square_Feet", "Bedrooms", "Bathrooms", "Price"]
# data = {
#     'Square_Feet': np.random.randint(1000, 4500, size=150),
#     'Bedrooms': np.random.randint(1, 5, size=150),
#     'Bathrooms': np.random.randint(1, 4, size=150),
#     'Price': np.random.randint(200000, 750000, size=150)
# }
# # Завдання:
# # Застосувати K-Fold крос-валідацію для оцінювання моделі.
# # Навчити модель лінійної регресії.
# # Вивести середню помилку на кожному фолді.
# df = pd.DataFrame(data)
# # Розділення ознак та цільової змінної
# X = df[["Square_Feet", "Bedrooms", "Bathrooms"]]
# y = df["Price"]
# # Ініціалізація моделі
# model = LinearRegression()
# # Ініціалізація KFold з 5 фолдами
# kf = KFold(n_splits=5, shuffle=True, random_state=42)
# # Виконання крос-валідації
# cv_scores = cross_val_score(
#     model,
#     X,
#     y,
#     cv=kf,
#     scoring='neg_mean_squared_error'  # Негативна середньоквадратична помилка
# )
# # Розрахунок середньої помилки та стандартного відхилення
# mean_mse = np.mean(-cv_scores)
# std_mse = np.std(-cv_scores)
# print(f"Середня MSE: {mean_mse:.2f}")
# print(f"Стандартне відхилення MSE: {std_mse:.2f}")
# # Виведення середньої помилки на кожному фолді
# for i, score in enumerate(-cv_scores):
#     print(f"Фолд {i + 1} MSE: {score:.2f}")
# =====================================================================


# ======================= ЗАВДАННЯ 3 =======================
# Дано:
# Набір даних plant_data з колонками ["Height", "Root_Mass", "Leaf_Area", "Species"]
# Початковий код
# np.random.seed(0)
# data = {
#     'Height': np.random.randint(10, 100, size=200),
#     'Root_Mass': np.random.rand(200) * 20,
#     'Leaf_Area': np.random.rand(200) * 30,
#     'Species': np.random.choice(['Species1', 'Species2', 'Species3'], size=200)
# }
# df = pd.DataFrame(data)
# # Завдання:
# # Імпортувати необхідні бібліотеки.
# # Створити набір даних.
# # Розділити дані на навчальні та тестові набори.
# # Масштабувати дані.
# # Навчити модель SVM.
# # Вивести звіт класифікації.
# # Виділяємо ознаки (X) та цільову змінну (y)
# X = df[['Height', 'Root_Mass', 'Leaf_Area']]
# y = df['Species']
# # 2. Розділення даних на навчальний та тестовий набори (70% на 30%)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# # 3. Масштабування даних
# # SVM чутливий до масштабу ознак, тому використовуємо StandardScaler
# scaler = StandardScaler()
# X_train_scaled = scaler.fit_transform(X_train)
# X_test_scaled = scaler.transform(X_test)
# # 4. Навчання моделі SVM
# model = SVC(kernel='linear', random_state=42)
# model.fit(X_train_scaled, y_train)
# # 5. Прогнозування та виведення звіту класифікації
# y_pred = model.predict(X_test_scaled)
# print("Звіт класифікації для моделі SVM:")
# print(classification_report(y_test, y_pred))
# =====================================================================


# Основні методи параметричної оптимізації (бонусне)
# iris = load_iris()
# df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
# df['species'] = iris.target

# X = df.drop('species', axis=1)
# y = df['species']
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.3, random_state=42, stratify=y
# )
# param_grid = {
#     'n_estimators': [50, 100, 200],
#     'max_depth': [None, 10, 20, 30],
#     'min_samples_split': [2, 5, 10],
#     'min_samples_leaf': [1, 2, 4]
# }
# rf = RandomForestClassifier(random_state=42)
# grid_search = GridSearchCV(
#     estimator=rf,
#     param_grid=param_grid,
#     cv=5,
#     scoring='accuracy',
#     n_jobs=-1,
#     verbose=2
# )

# grid_search.fit(X_train, y_train)
# print("Найкращі параметри:", grid_search.best_params_)

# best_rf = grid_search.best_estimator_
# y_pred = best_rf.predict(X_test)

# accuracy = accuracy_score(y_test, y_pred)
# print("\\nТочність моделі після оптимізації:", accuracy)

# report = classification_report(y_test, y_pred, target_names=iris.target_names)
# print("\\nЗвіт класифікації:\\n", report)

# cm = confusion_matrix(y_test, y_pred)
# sns.heatmap(cm, annot=True, fmt='d', cmap='Greens',
#             xticklabels=iris.target_names,
#             yticklabels=iris.target_names)
# plt.ylabel('Справжній клас')
# plt.xlabel('Передбачений клас')
# plt.title('Конфузійна матриця')
# plt.show()

