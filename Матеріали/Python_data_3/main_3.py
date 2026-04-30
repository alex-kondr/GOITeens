# pip install scikit-learn

import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer

# df = pd.read_csv('data.csv')
# df = pd.read_csv('employee_data.csv')
# missing_values = df.isnull()
# missing_values = df.isnull().sum()
# missing_values = df.isna().sum()
# print(missing_values)
# print(df.info())
# msno.matrix(df) #Візуалізація Пропущених Значень
# plt.show()

# Заповнення Середнім Значенням
# mean_value = df['age'].mean()
# df['age'].fillna(mean_value, inplace=True)

# Заповнення Медіаною
# median_value = df['income'].median()
# df['income'].fillna(median_value, inplace=True)

# Заповнення Модою
# mode_value = df['Gender'].mode()[0]
# df['Gender'].fillna(mode_value, inplace=True)
# print(df)

# Заповнення Методами Переднього та Заднього Заповнення
# df['sales'].fillna(method='ffill', inplace=True)
# df['sales'].fillna(method='bfill', inplace=True)

# url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
# df = pd.read_csv(url)
# print(df.head())
# Завдання 1: Визначте кількість пропущених значень у кожному стовпці датафрейму df та виведіть результат.
# missing_values = df.isnull().sum()
# print(missing_values)
# Завдання 2: Візуалізуйте пропущені значення у датафреймі df за допомогою бібліотеки missingno та відобразіть графік.
# msno.matrix(df)
# plt.show()
# Завдання 3: Заповніть пропущені значення у стовпці 'Age' середнім значенням віку та виведіть оновлений датафрейм.
# df['Age'] = df['Age'].fillna(df['Age'].mean())
# msno.matrix(df)
# plt.show()
# Завдання 4: Заповніть пропущені значення у стовпці 'Cabin' модою (найчастіше зустрічається значення) та виведіть оновлений датафрейм.
# Завдання 5: Заповніть пропущені значення у стовпці 'Embarked' методом переднього заповнення (forward fill) та виведіть оновлений датафрейм.

# Завдання 1
# Виправте помилку у коді, щоб правильно виявити пропущені значення у DataFrame df.
# df = pd.read_csv('data.csv')
# missing_values = ...
# print(missing_values)

# Завдання 2
# Додайте рядок коду, щоб заповнити пропущені значення у стовпці Age середнім значенням цього стовпця.
# df = pd.read_csv('data.csv')
# mean_age = df['Age'].mean()
# df['Age']...
# print(df['Age'].head())

# Завдання 3
# Виправте код, щоб заповнити пропущені значення у стовпці Salary медіаною цього стовпця.
# df = pd.read_csv('data.csv')
# median_salary = df['Salary'].median()
# df['Salary']...
# print(df['Salary'].head())

# Завдання 4
# Виправте код, щоб заповнити пропущені значення у стовпці Department модою цього стовпця.
# df = pd.read_csv('data.csv')
# mode_department = df['Department'].mode()[0]
# df['Department']...
# print(df['Department'].head())

# Завдання 5
# Додайте рядок коду, щоб використовувати метод info() для отримання інформації про пропущені значення у DataFrame df.
# df = pd.read_csv('data.csv')
# df...

# Завдання 6
# Виправте код, щоб додати візуалізацію пропущених значень за допомогою бібліотеки missingno.
# df = pd.read_csv('data.csv')
# ...
# plt.show()

# Завдання 7
# Додайте рядки коду, щоб заповнити пропущені значення у стовпці Sales методом переднього заповнення (ffill) та заднього заповнення (bfill).
# df = pd.read_csv('data.csv')
# df['Sales'].fillna...
# df['Sales'].fillna...
# print(df['Sales'].head())

# Завдання 8
# Виправте код, щоб заповнити пропущені значення у стовпцях Age середнім, Salary медіаною та Department модою.
# df = pd.read_csv('data.csv')
# df['Age']...
# df['Salary']...
# df['Department']...
# print(df.head())


# ВИДАЛЕННЯ ПРОПУЩЕНИХ ЗНАЧЕНЬ

# Видалення всього рядка з будь-яким пропущеним значенням
# df = sns.load_dataset('diamonds')
# df_dropped = df.dropna()
# print(df_dropped.shape)

# Видалення рядка з пропущеним значенням у конкретному стовпці
# df = sns.load_dataset('diamonds')
# df_dropped_specific = df.dropna(subset=['price'])
# print(df_dropped_specific.shape)

# Робота з категоріями, де є пропущені дані
# df = sns.load_dataset('diamonds')
# mode_cut = df['cut'].mode()[0]
# df['cut'].fillna(mode_cut, inplace=True)
# print(df['cut'].isnull().sum())

# Створення нової категорії для пропущених значень
# df = sns.load_dataset('diamonds')
# df['color'].fillna('Unknown', inplace=True)
# print(df['color'].isnull().sum())

# Заповнення за допомогою алгоритмів машинного навчання
# df = sns.load_dataset('diamonds')
# df['clarity'] = df['clarity'].astype(object)
# imputer = SimpleImputer(strategy='most_frequent')
# df['clarity'] = imputer.fit_transform(df[['clarity']])[:, 0]
# print(df['clarity'].isnull().sum())


# Завдання 1
# Виправте код, щоб правильно виявити кількість пропущених значень у стовпці Salary DataFrame df
# df = pd.read_csv('employee_data.csv')
# missing_salary = df['Salary'].isnull() #.sum()
# print(missing_salary)

# Завдання 2
# Додайте рядок коду, щоб видалити всі рядки, де відсутні значення у стовпці Age.
# df = pd.read_csv('employee_data.csv')
# df_cleaned = df.dropna(subset=['Age'])
# print(df_cleaned.shape)

# Завдання 3
# Виправте код, щоб видалити всі рядки, які містять хоча б одне пропущене значення у DataFrame df.
# df = pd.read_csv('employee_data.csv')
# df_dropped = df.dropna(axis=1)
# print(df_dropped.columns)

# Завдання 4
# Виправте код, щоб видалити рядки з пропущеними значеннями у стовпцях Age та Department.
# df = pd.read_csv('employee_data.csv')
# df_important = df.dropna(subset=['Age']) #, 'Department'])
# print(df_important.head())

# Завдання 5
# Виправте код, щоб видалити стовпець Manager, якщо кількість пропущених значень перевищує 50% від загальної кількості рядків
# df = pd.read_csv('employee_data.csv')
# threshold = len(df) * 0.5
# df_dropped_columns = df.dropna(axis=0, thresh=threshold) #, subset=['Manager'])
# print(df_dropped_columns.columns)

# Завдання 6
# Додайте параметр, щоб заповнити пропущені значення у стовпці Age середнім значенням цього стовпця
# df = pd.read_csv('employee_data.csv')
# mean_age = df['Age'].mean()
# df['Age'].fillna(mean_age) #, inplace=True)
# print(df['Age'].head())


# ПЕРЕТВОРЕННЯ КАТЕГОРІАЛЬНИХ ДАНИХ
# url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
# df = pd.read_csv(url)
# print(df.head())
# df['Embarked'] = df['Embarked'].astype('category').cat.codes
# print(df[['Embarked']].head())

# Що таке One-Hot Encoding?
# One-hot encoding — це метод перетворення категоріальних
# змінних у числовий формат шляхом створення нових бінарних
# (0 або 1) змінних для кожної унікальної категорії.
# Цей метод особливо корисний для номінальних змінних без порядку.
# url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
# df = pd.read_csv(url)
# df_dummies = pd.get_dummies(df, columns=['Embarked'], drop_first=True)
# print(df_dummies.head())

# Приклад 1:
# Змінюємо категоріальну змінну 'Sex' на числовий формат, використовуючи коди категорій.
# url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
# df = pd.read_csv(url)
# df['Sex'] = df['Sex'].astype('category').cat.codes
# Створимо фіктивні змінні за допомогою One-Hot Encoding
# df_dummies = pd.get_dummies(df, columns=['Sex'], drop_first=True)
# print(df_dummies.head())


# ЩО ТАКЕ МЕТОД .replace()?
# DataFrame.replace(to_replace, value, inplace=False, limit=None, regex=False, method='pad')
# data = {'Gender': ['Male', 'Female', 'Female', 'Male', 'Male']}
# df = pd.DataFrame(data)
# df['Gender'] = df['Gender'].replace({'Male': 0, 'Female': 1})
# print(df)

# data = {'Status': ['Single', 'Married', 'Single', 'Divorced']}
# df = pd.DataFrame(data)
# df['Status'] = df['Status'].replace({'Single': 1, 'Married': 2, 'Divorced': 3})
# print(df)

# data = {'Comments': ['Good product', 'bad quality', 'average', 'excellent']}
# df = pd.DataFrame(data)
# df['Comments'] = df['Comments'].replace(to_replace='^bad.*', value='Poor', regex=True)
# print(df)

# Практичний приклад
# data = {'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego']}
# df = pd.DataFrame(data)
# frequency = df['City'].value_counts()
# rare_cities = frequency[frequency < 2].index
# df['City'] = df['City'].replace(rare_cities, 'Other')
# print(df)

data = {'Color': ['Red', 'Blue', 'Green', 'Blue', 'Red']}
df = pd.DataFrame(data)
df_encoded = pd.get_dummies(df, columns=['Color'], drop_first=True)
print(df_encoded)