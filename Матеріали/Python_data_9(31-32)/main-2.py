import pandas as pd
import numpy as np


# df = pd.read_csv('data.csv')
# df.to_excel('data.xlsx', index=False)
# df.head()
# df.info()
# df.describe()
# df.isnull().sum()
# df = df.dropna()
# df['column'].fillna(df['column'].mean(), inplace=True)

# Кодування категоріальних змінних
# from sklearn.preprocessing import LabelEncoder
# le = LabelEncoder()
# df['category'] = le.fit_transform(df['category'])

# Масштабування даних
# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)

# Вибір ознак
# from sklearn.feature_selection import SelectKBest, chi2
# selector = SelectKBest(chi2, k=10)
# X_new = selector.fit_transform(X, y)


# ЗАВДАННЯ 1
# Датасет містить інформацію про клієнтів, їх
# фінансовий стан та результат перевірки кредитоспроможності,
# що відображено в мітці Creditability.
# Задача моделі полягає в тому, щоб на основі ознак передбачити,
# чи є клієнт надійним (1) чи ні (0).
# Датасет завантажено з UCI Machine Learning Repository, і він містить як числові, так і категоріальні змінні.

# from sklearn.preprocessing import LabelEncoder, StandardScaler
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score, classification_report

# le = LabelEncoder()

# url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data'
# column_names = [
#     "CheckingAccountStatus",
#     "DurationInMonths",
#     "CreditHistory",
#     "Purpose",
#     "CreditAmount",
#     "SavingsAccountBonds",
#     "EmploymentStatusSince",
#     "InstallmentRatePercentage",
#     "PersonalStatusSex",
#     "OtherDebtorsGuarantors",
#     "PresentResidenceSince",
#     "Property",
#     "AgeInYears",
#     "OtherInstallmentPlans",
#     "Housing",
#     "ExistingCreditsAtBank",
#     "Job",
#     "NumberDependents",
#     "Telephone",
#     "ForeignWorker",
#     "Creditability",  # Цільова змінна (1 - надійний, 2 - ненадійний)
# ]
# df = pd.read_csv(url, sep=" ", header=None, names=column_names)
# print(df.head())
# df.info()
# print(df.isnull().sum())

# categorical_features = [
#     "CheckingAccountStatus",
#     "CreditHistory",
#     "Purpose",
#     "SavingsAccountBonds",
#     "EmploymentStatusSince",
#     "PersonalStatusSex",
#     "OtherDebtorsGuarantors",
#     "Property",
#     "OtherInstallmentPlans",
#     "Housing",
#     "Job",
#     "Telephone",
#     "ForeignWorker",
# ]
# for feature in categorical_features:
#     df[feature] = le.fit_transform(df[feature])

# # print(df.head())

# X = df.drop(['Creditability'], axis=1)
# y = df['Creditability']
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)
# X_train, X_test, y_train, y_test = train_test_split(
#     X_scaled, y, test_size=0.3, random_state=42, stratify=y
# )
# model = RandomForestClassifier(n_estimators=100, random_state=42)
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# print("Accuracy:", accuracy_score(y_test, y_pred))
# print("Classification Report:\\n", classification_report(y_test, y_pred))

# ЗАВДАННЯ 2
# Мета цієї задачі — створити модель, яка зможе точно
# класифікувати діагнози на основі різних
# характеристик клітин. У цьому прикладі
# використовуються дані, доступні з UCI Machine Learning Repository.

# from sklearn.preprocessing import LabelEncoder, StandardScaler
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score, classification_report
# from sklearn.svm import SVC

# url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data'
# column_names = [
#     "ID",
#     "Diagnosis",
#     "radius_mean",
#     "texture_mean",
#     "perimeter_mean",
#     "area_mean",
#     "smoothness_mean",
#     "compactness_mean",
#     "concavity_mean",
#     "concave_points_mean",
#     "symmetry_mean",
#     "fractal_dimension_mean",
#     "radius_se",
#     "texture_se",
#     "perimeter_se",
#     "area_se",
#     "smoothness_se",
#     "compactness_se",
#     "concavity_se",
#     "concave_points_se",
#     "symmetry_se",
#     "fractal_dimension_se",
#     "radius_worst",
#     "texture_worst",
#     "perimeter_worst",
#     "area_worst",
#     "smoothness_worst",
#     "compactness_worst",
#     "concavity_worst",
#     "concave_points_worst",
#     "symmetry_worst",
#     "fractal_dimension_worst",
# ]
# cancer = pd.read_csv(url, header=None, names=column_names)
# # print(cancer.head())
# le = LabelEncoder()
# cancer['Diagnosis'] = le.fit_transform(cancer['Diagnosis'])
# X = cancer.drop(['ID', 'Diagnosis'], axis=1)
# y = cancer['Diagnosis']
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)
# X_train, X_test, y_train, y_test = train_test_split(
#     X_scaled, y, test_size=0.3, random_state=42, stratify=y
# )
# # Модель навчається на тренувальних даних.
# model = SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# print("Accuracy:")
# print(accuracy_score(y_test, y_pred))
# print("Classification Report:\\n")
# print(classification_report(y_test, y_pred))


# ЗАВДАННЯ 1
# Ви маєте датасет telco_customer_churn.csv, який
# містить інформацію про клієнтів телекомунікаційної
# компанії. Потрібно закодувати категоріальні змінні
# за допомогою LabelEncoder.

# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score
# from sklearn.preprocessing import LabelEncoder

# url = 'https://raw.githubusercontent.com/treselle-systems/customer_churn_analysis/master/WA_Fn-UseC_-Telco-Customer-Churn.csv'
# churn = pd.read_csv(url)
# # print(churn.head())

# X = churn.drop(['customerID', 'Churn'], axis=1)
# y = churn['Churn']

# Додайте рядок коду для кодування категоріальних змінних.
# le = LabelEncoder()
# cat_cols = X.select_dtypes(include=["object", "str"]).columns
# for col in cat_cols:
#     X[col] = le.fit_transform(X[col])

# y = le.fit_transform(y)

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# model = RandomForestClassifier(n_estimators=100, random_state=42)
# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)
# print("Точність моделі:", accuracy_score(y_test, y_pred))


# ЗАВДАННЯ 2
# Ви маєте датасет fruit_data.csv, який містить
# інформацію про фрукти з різними ознаками. Потрібно
# закодувати цільову змінну Fruit_Type за допомогою LabelEncoder.

# Змініть 1 рядок коду, щоб використовувати LabelEncoder для кодування цільової змінної Fruit_Type.

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.metrics import accuracy_score
# from sklearn.preprocessing import LabelEncoder

# fruit_data = {
#     "Weight": [150, 120, 130, 160, 140, 170, 110, 180, 115, 155],
#     "Color_Score": [7, 6, 8, 9, 7, 10, 5, 9, 6, 8],
#     "Texture_Score": [6, 5, 7, 8, 6, 9, 4, 8, 5, 7],
#     "Fruit_Type": ["Apple", "Banana", "Cherry", "Apple", "Cherry", "Apple", "Banana", "Apple", "Banana", "Cherry"]
# }
# df = pd.DataFrame(fruit_data)

# X = df[['Weight', 'Color_Score', 'Texture_Score']]
# y = df['Fruit_Type']

# le = LabelEncoder()
# y = le.fit_transform(y)

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# model = KNeighborsClassifier(n_neighbors=3)
# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)
# print("Точність моделі:", accuracy_score(y_test, y_pred))


# ЗАВДАННЯ 3
# Ви маєте датасет sms_spam.csv, який містить
# текст повідомлень та їхні мітки (spam/ham).
# Потрібно додати векторизацію тексту за допомогою TfidfVectorizer.

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.metrics import accuracy_score, classification_report
# from sklearn.feature_extraction.text import TfidfVectorizer

# sms = pd.read_csv('https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/sms_spam.csv')
# # print(sms.head())
# sms.columns = ["label_num", "message"]

# X = sms['message']
# y = sms['label_num']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# # Векторизація тексту
# # Додайте рядки тут
# vectorizer = TfidfVectorizer()
# X_train_vectorized = vectorizer.fit_transform(X_train)
# X_test_vectorized = vectorizer.transform(X_test)

# model = MultinomialNB()
# model.fit(X_train_vectorized, y_train)

# y_pred = model.predict(X_test_vectorized)
# print("Точність моделі:", accuracy_score(y_test, y_pred))


# ЗАВДАННЯ 4
# Ви маєте датасет diabetes.csv, який містить
# інформацію про пацієнтів з діабетом.
# Потрібно додати кодування категоріальних змінних
# за допомогою LabelEncoder, якщо такі є.

# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler, LabelEncoder
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score, classification_report

# url = 'https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv'
# diabetes = pd.read_csv(url)
# # print(diabetes.head())

# X = diabetes.drop('Outcome', axis=1)
# y = diabetes['Outcome']

# ------------------------------------------------------------
# Додайте рядок коду для кодування категоріальних
# змінних за допомогою LabelEncoder, якщо такі є.
# le = LabelEncoder()
# cat_columns = X.select_dtypes(include=["object", "str"]).columns
# for cat in cat_columns:
#     X[cat] = le.fit_transform(X[cat])
# ------------------------------------------------------------

# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)

# X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3)

# model = LogisticRegression(max_iter=200)
# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)
# print("Точність моделі:", accuracy_score(y_test, y_pred))


# ЗАВДАННЯ 5
# Ви маєте датасет heart.csv, який містить інформацію про
# пацієнтів з проблемами серцево-судинної системи.
# Потрібно додати параметр random_state=42
# у функцію train_test_split для відтворюваності результатів.

# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.svm import SVC
# from sklearn.metrics import accuracy_score, classification_report

# url = 'https://raw.githubusercontent.com/roninw/Heart-Disease-Investigation/master/heart.csv'
# heart = pd.read_csv(url)

# X = heart.drop('target', axis=1)
# y = heart['target']

# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)

# # ------------------------------------------------------------
# # Змініть рядок коду, щоб додати random_state=42 у функцію train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3)
# # ------------------------------------------------------------

# model = SVC(kernel='rbf', C=10, gamma=0.001)
# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)
# print("Точність моделі:", accuracy_score(y_test, y_pred))


# ЗАВДАННЯ 6
# Ви маєте датасет music_genre.csv, який містить
# тексти пісень та їхні жанри. Потрібно додати
# обробку пропущених значень у ознаках шляхом заповнення їх нулями.

# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score, classification_report
# from sklearn.feature_extraction.text import CountVectorizer

# url_spotify = 'https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-21/spotify_songs.csv'
# music = pd.read_csv(url_spotify)
# music = music.fillna(value="")
# # print(music.isnull().sum())

# X = music['track_name']
# # print(X)
# y = music['playlist_genre']


# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# vectorizer = CountVectorizer()
# X_train = vectorizer.fit_transform(X_train)
# X_test = vectorizer.transform(X_test)

# model = LogisticRegression(max_iter=200)
# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)
# print("Точність моделі:", accuracy_score(y_test, y_pred))


# ЗАВДАННЯ 7
# Розглянемо задачу класифікації клієнтів телекомунікаційної компанії
# датасет Telco Customer Churn
# Завантажте дані та виконайте перевірку на наявність пропущених значень.
# Заповніть пропущені значення в числових і категоріальних змінних відповідно до їх природи (мода або середнє значення).
# Перетворіть категоріальні змінні на числовий формат за допомогою LabelEncoder.
# Виділіть ознаки та цільову змінну, а потім розділіть дані на тренувальні та тестові набори.
# Масштабуйте числові ознаки, щоб уникнути впливу різних діапазонів значень.
# Використайте алгоритм Random Forest для класифікації.
# Виконайте прогнозування на тестових даних, оцініть точність моделі та отримайте звіт класифікації.

# from sklearn.preprocessing import LabelEncoder, StandardScaler
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split, cross_val_score
# from sklearn.metrics import accuracy_score, classification_report

# url = 'https://raw.githubusercontent.com/pplonski/datasets-for-start/master/telco-customer-churn/Telco-Customer-Churn.csv'
# churn = pd.read_csv(url)
# # print(churn.isnull().sum())
# # print(churn.head())

# X = churn.drop(columns=["customerID", "Churn"])

# le = LabelEncoder()
# cat_columns = X.select_dtypes(include=["object", "str"]).columns
# for cat in cat_columns:
#     X[cat] = le.fit_transform(X[cat])

# y = churn["Churn"]
# y = le.fit_transform(y)

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3, random_state=42)

# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)

# model = RandomForestClassifier(n_estimators=100, random_state=42)
# model.fit(X_train, y_train) #1
# scores = cross_val_score(model, X, y, cv=5, scoring='accuracy') #2

# y_pred = model.predict(X_test)

# print("=== РЕЗУЛЬТАТИ ОЦІНКИ МОДЕЛІ ===")
# print("Точність моделі за кожним фолдом:", scores)
# print("Середня точність:", scores.mean())
# print("Стандартне відхилення:", scores.std())
# print(f"Точність (Accuracy): {accuracy_score(y_test, y_pred):.4f}\n")
# print("Звіт класифікації (Classification Report):")
# print(classification_report(y_test, y_pred))
