import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = sns.load_dataset("penguins")

# Завдання 1
# Створіть графік розподілу категоріальної
# змінної species з датасету penguins за допомогою
# функції countplot(). Використовуйте кольорову
# палітру Set2 та додайте заголовок та підписи до осей.

# Завдання 2
# Створіть графік середніх значень змінної
# body_mass_g для кожного виду пінгвінів за
# допомогою функції barplot(). Використовуйте
# кольорову палітру pastel та додайте заголовок та підписи до осей.


# Розподіл даних
# distplot "deprecated"
# sns.distplot(a, bins=None, hist=True, kde=True, rug=False, color=None,
#              label=None, ax=None, hist_kws=None, kde_kws=None, rug_kws=None)
# a: Дані, які потрібно візуалізувати.
# bins: Кількість бінів (інтервалів) для гістограми.
# hist: Відображати гістограму (True/False).
# kde: Відображати графік KDE (True/False).
# rug: Відображати "ковзні" лінії для кожного спостереження (True/False).
# color: Колір графіка.
# label: Мітка для легенди.
# ax: Об'єкт осі matplotlib для побудови графіка.
# hist_kws: Додаткові параметри для гістограми.
# kde_kws: Додаткові параметри для KDE.
# rug_kws: Додаткові параметри для rug-графіка.
################################################
# Для гістограми та оцінки щільності (KDE) — histplot
# sns.histplot(data=df, x="body_mass_g", kde=True)

# Для чистої оцінки щільності — kdeplot
# sns.kdeplot(data=df, x="body_mass_g")

# Для сукупності розподілу (емпірична функція) — ecdfplot
# sns.ecdfplot(data=df, x="body_mass_g")

# Для універсального вибору — displot
# sns.displot(data=df, x="body_mass_g", kind="hist", kde=True)
############################################################

# sns.distplot(df['body_mass_g'], bins=20, kde=False, color='blue')
# plt.title('Гістограма Масси Тіла Пінгвінів')
# plt.xlabel('Маса Тіла (г)')
# plt.ylabel('Кількість Спостережень')
# plt.show()

# Налаштування колірної палітри та стилю графіків
# sns.histplot(data=df, x='body_mass_g', bins=20, kde=True, color='teal')
# sns.histplot(data=df, x='body_mass_g', bins=20, kde=True, color='brown')
# plt.show()

# Приклад 1
# Уявімо, що ми аналізуємо оцінки студентів за
# предметом. Ми можемо побудувати графік розподілу
# оцінок, щоб зрозуміти, чи розподіл симетричний,
# чи спостерігається мультимодальність.
# Створимо випадкові дані для оцінок студентів
# grades = np.random.normal(loc=75, scale=10, size=200)
# sns.distplot(grades, bins=15, kde=True, color='skyblue', rug=True)
# plt.show()

# Приклад 2
# Якщо ми аналізуємо продажі різних продуктів,
# можемо порівняти їхні розподіли за допомогою distplot()
# sales_product_A = np.random.gamma(shape=2., scale=50., size=100)
# sales_product_B = np.random.gamma(shape=3., scale=40., size=100)
# sns.distplot(sales_product_A, bins=20, kde=True, color='green', label='Продукт A')
# sns.distplot(sales_product_B, bins=20, kde=True, color='red', label='Продукт B')
# plt.show()

# Приклад 3
# Побудова графіка розподілу може допомогти виявити аномальні значення в даних.
# data = np.concatenate([np.random.normal(50, 5, 1000), np.random.normal(100, 5, 10)])
# sns.distplot(data, bins=30, kde=True, color='purple', rug=True)
# plt.show()

# Аргументи розподілу даних

# Параметр bins
# Визначає кількість інтервалів для гістограми.
# Збільшення кількості бінів робить гістограму більш деталізованою,
# але може створити шум, тоді як зменшення кількості бінів робить її більш гладкою
# plt.figure(figsize=(12, 6))
# sns.distplot(df['body_mass_g'], bins=10, kde=False, color='blue', label='10 бінів')
# sns.distplot(df['body_mass_g'], bins=30, kde=False, color='orange', label='30 бінів')
# plt.show()

# Параметр kde
# Визначає, чи відображати графік KDE. За замовчуванням встановлено True
# sns.distplot(df['body_mass_g'], bins=20, kde=False, color='cyan')

# Параметр rug
# Визначає, чи відображати rug-графік.
# Rug-графік додає маленькі вертикальні лінії під гістограмою, що представляють кожне спостереження.
# sns.distplot(df['body_mass_g'], bins=20, kde=True, rug=True, color='magenta')

# Приклад 1
# Ми можемо побудувати розподіли для
# різних груп даних, наприклад, для різних видів пінгвінів.
# plt.figure(figsize=(12, 8))

# for species in df['species'].unique():
#     subset = df[df['species'] == species]
#     sns.distplot(subset['body_mass_g'], kde=True, label=species)

# plt.title('Розподіл Масси Тіла за Видами Пінгвінів')
# plt.xlabel('Маса Тіла (г)')
# plt.ylabel('Щільність Ймовірності')
# plt.legend()
# plt.show()

# Приклад 2
# Ми можемо налаштувати додаткові параметри
# графіка, такі як лінії кольорів, прозорість та інші.
# sns.distplot(df['body_mass_g'], bins=30, kde=True, rug=True, color='darkblue', hist_kws={'alpha':0.6}, kde_kws={'linewidth':2})
# plt.title('Налаштований Графік Розподілу Масси Тіла Пінгвінів')
# plt.xlabel('Маса Тіла (г)')
# plt.ylabel('Щільність Ймовірності')
# plt.show()


# Завдання 1
# Нижче наведено код, який має на меті побудувати
# гістограму розподілу суми рахунку (total_bill) з
# 20 бінів. Однак, код містить помилку, через яку графік не відображається правильно.
# 1.Знайдіть і виправте помилку у коді.
# df = sns.load_dataset('tips')
# sns.distplot(df['total_bill'], bins='twenty', kde=False, color='blue')
# plt.title('Розподіл Суми Рахунку')
# plt.xlabel('Сума Рахунку (USD)')
# plt.ylabel('Кількість Спостережень')
# plt.show()

# Завдання 2
# Вам потрібно побудувати комбінований графік
# гістограми та KDE для розподілу суми рахунку (total_bill).
# Однак, графік KDE не відображається, і кольорова палітра графіка не відповідає вимогам.
# 1. Додайте графік KDE до існуючої гістограми.
# 2. Змініть колір графіка на зелений.
# df = sns.load_dataset('tips')
# sns.distplot(df['total_bill'], bins=25, kde=False, color='pink')
# plt.title('Розподіл Суми Рахунку з KDE')
# plt.xlabel('Сума Рахунку (USD)')
# plt.ylabel('Щільність Ймовірності')
# plt.show()

# Завдання 3
# Нижче наведено код для побудови графіка розподілу
# суми рахунку (total_bill), але аномалії у даних не
# відображаються належним чином через неправильне налаштування параметрів.
# 1. Збільште кількість бінів, щоб краще відобразити аномалії.
# 2. Додайте rug-графік для відображення окремих спостережень.
# data = np.concatenate([np.random.normal(50, 5, 1000), np.random.normal(100, 5, 10)])
# sns.distplot(data, bins=10, kde=True, color='red')
# plt.title('Розподіл Даних з Аномаліями')
# plt.xlabel('Значення')
# plt.ylabel('Щільність Ймовірності')
# plt.show()

# Завдання 4
# Вам потрібно побудувати графік розподілу суми рахунку
# (total_bill) з використанням палітри кольорів 'muted'
# та стилю графіка 'darkgrid'. Проте, код містить помилки в налаштуваннях стилю та палітри.
# 1. Виправте помилки у встановленні стилю та палітри.
# 2. Переконайтеся, що графік використовує палітру 'muted' та стиль 'darkgrid'.
# df = sns.load_dataset('tips')
# sns.set_style('muted')
# sns.set_palette('darkgrid')
# sns.distplot(df['total_bill'], bins=20, kde=True, color='brown')
# plt.title('Розподіл Суми Рахунку з Налаштуваннями Стилю та Палітри')
# plt.xlabel('Сума Рахунку (USD)')
# plt.ylabel('Щільність Ймовірності')
# plt.show()

# Завдання 5
# Ви побудували графік розподілу за допомогою distplot(),
# але він виглядає занадто світлим і важко розрізняти різні
# частини. Ваше завдання — покращити видимість графіка,
# змінивши кольори та додавши елементи стилю.
# 1. Змініть колір графіка на більш контрастний, наприклад, 'navy'.
# 2. Додайте стиль 'whitegrid' до графіка.
# df = sns.load_dataset('tips')
# sns.distplot(df['total_bill'], bins=20, kde=True, color='lightgray')
# plt.title('Розподіл Суми Рахунку')
# plt.xlabel('Сума Рахунку (USD)')
# plt.ylabel('Щільність Ймовірності')
# plt.show()

# sns.distplot(df['total_bill'], bins=20, kde=True, color='teal',
#              kde_kws={'linewidth': 3, 'linestyle': '--'})


# ТЕПЛОВІ КАРТИ
# Основні Поняття
# Кореляція це статистична міра, яка визначає ступінь
# та напрямок лінійного зв'язку між двома змінними.
# Значення кореляції варіюються від -1 до 1, де -1
# означає повністю негативну кореляцію,
# 1 — повністю позитивну, а 0 — відсутність кореляції.

# sns.heatmap(data, annot=False, cmap='coolwarm', linewidths=0.5, fmt=".2f")
# data: Кореляційна матриця (наприклад, датафрейм або numpy масив).
# annot: Відображати значення чисел у клітинках (True/False).
# cmap: Колірна палітра для теплової карти.
# linewidths: Ширина ліній між клітинками.
# fmt: Формат чисел при анотації.

# df = sns.load_dataset('iris')
# numeric_df = df.select_dtypes(include=[float, int])
# corr = numeric_df.corr()
# sns.heatmap(corr, annot=True, cmap='coolwarm')
# plt.title('Кореляційна Матриця для Датасету Iris')
# plt.show()

# Побудуємо теплову карту з налаштованою палітрою та без анотацій
# sns.heatmap(corr, annot=False, cmap='viridis', linewidths=0.5)

# Встановимо стилі для покращення вигляду
# sns.set_style('white')
# Створимо маску для верхньої половини матриці (щоб уникнути дублювання)
# mask = np.triu(np.ones_like(corr, dtype=bool))
# Побудова теплової карти з маскою
# sns.heatmap(corr, mask=mask, annot=True, cmap='YlGnBu', linewidths=0.3, fmt=".2f")

# coolwarm: Підходить для відображення позитивних та негативних кореляцій.
# viridis: Відмінно підходить для високої контрастності.
# YlGnBu: Гарна палітра для відображення різних рівнів кореляції.

# Створення дивергентної палітри за допомогою diverging_palette():
# custom_div_cmap = sns.diverging_palette(220, 20, as_cmap=True)
# sns.heatmap(corr, annot=True, cmap=custom_div_cmap)
# plt.title('Кореляційна Матриця (Custom Diverging)')
# plt.show()

# Власна кольорова палітра
# custom_cmap = sns.color_palette(['#FF5733', '#33FF57', '#3357FF'], as_cmap=True)
# sns.heatmap(corr, annot=True, cmap=custom_cmap)
# plt.title('Кореляційна Матриця (Custom Colors)')
# plt.show()

# Власна дивергентна палітра
# custom_div_cmap = sns.diverging_palette(250, 10, n=15, s=50, l=20, as_cmap=True)
# sns.heatmap(corr, annot=True, cmap=custom_div_cmap, center=0)
# plt.title('Кореляційна Матриця (Custom Diverging)')
# plt.show()

# ЗАВДАННЯ 1
# Створіть кореляційну матрицю для числових
# змінних датасету penguins та відобразіть її за
# допомогою теплової карти з використанням стандартної кольорової палітри.
# Датасет penguins завантажується за допомогою функції
# sns.load_dataset(). Кореляційна матриця обчислюється методом .corr().
# df = sns.load_dataset('penguins')
# numeric_df = df.select_dtypes(include=[float, int])
# corr = numeric_df.corr()
# sns.heatmap(corr, annot=True, cmap='coolwarm')
# plt.title('Кореляційна Матриця для Датасету Penguins')
# plt.show()

# Завдання 2
# Нижче наведено код для побудови кореляційної
# матриці, але він містить помилку. Ваше завдання — знайти та виправити цю помилку.
# df = sns.load_dataset('penguins')
# corr_matrix = df.corr_matrix()
# sns.heatmap(corr_matrix, annot=True, cmap='viridis')
# plt.title('Кореляційна Матриця для Датасету Penguins')
# plt.show()

# Завдання 3
# Побудуйте кореляційну матрицю з використанням
# палітри 'YlGnBu' та застосуйте маску для верхньої половини матриці,
# щоб уникнути дублювання інформації. Додайте анотації до клітинок.
# df = sns.load_dataset('penguins')
# corr = df.corr()
# mask = np.triu(np.ones_like(corr, dtype=bool))
# sns.heatmap(corr, mask=mask, annot=True, cmap='YlGnBu', linewidths=0.5)
# plt.title('Кореляційна Матриця для Датасету Penguins (З Маскою)')
# plt.show()

# Завдання 4
# Побудуйте кореляційну матрицю з використанням власної
# дивергентної палітри та додайте лінії розділу між
# клітинками для кращої візуальної сегрегації.
# У цьому завданні створюється власна дивергентна
# палітра кольорів за допомогою LinearSegmentedColormap.
# from matplotlib.colors import LinearSegmentedColormap
# df = sns.load_dataset('penguins')
# corr = df.corr()
# colors = ["#d73027", "#f46d43", "#fdae61", "#fee08b", "#d9ef8b", "#a6d96a", "#66bd63", "#1a9850"]
# custom_div_cmap = LinearSegmentedColormap.from_list("CustomDivMap", colors, N=100)
# mask = np.triu(np.ones_like(corr, dtype=bool))
# sns.heatmap(corr, mask=mask, annot=True, cmap=custom_div_cmap, linewidths=0.7, linecolor='white')
# plt.title('Кореляційна Матриця для Датасету Penguins (Власна Палітра та Лінії Розділу)')
# plt.show()

# Завдання 5
# Нижче наведено код для побудови кореляційної
# матриці з невідомою палітрою. Знайдіть та виправте помилку.
# df = sns.load_dataset('penguins')
# corr = df.corr()
# sns.heatmap(corr, annot=True, cmap='unknown_palette')
# plt.title('Кореляційна Матриця з Невідомою Палітрою')
# plt.show()

# Завдання 7
# Побудуйте кластеризовану теплову карту
# кореляційної матриці, групуючи схожі змінні разом.
# Функція sns.clustermap() створює кластеризовану
# теплову карту, групуючи схожі змінні разом. Параметр figsize встановлює розмір графіка.
# df = sns.load_dataset('penguins')
# corr = df.corr()
# g = sns.clustermap(corr, annot=True, cmap='coolwarm', figsize=(10, 10))
# g.fig.suptitle('Кластеризована Кореляційна Матриця для Датасету Penguins', y=1.02)
# plt.show()

# Завдання 10
# Створіть власну кольорову шкалу та
# використовуйте її для теплової карти кореляційної матриці.
# Створюємо власну кольорову шкалу, переходячи
# від червоного через білий до синього, за допомогою LinearSegmentedColormap.
# from matplotlib.colors import LinearSegmentedColormap
# df = sns.load_dataset('penguins')
# corr = df.corr()
# colors = ["#ff0000", "#ffffff", "#0000ff"]
# custom_cmap = LinearSegmentedColormap.from_list("CustomMap", colors, N=100)
# sns.heatmap(corr, annot=True, cmap=custom_cmap, linewidths=0.5)
# plt.title('Кореляційна Матриця з Власною Кольоровою Шкалою')
# plt.show()

# Діаграма Розсіяння з Лінією Тренду
# df = sns.load_dataset('iris')
# sns.scatterplot(data=df, x='sepal_length', y='sepal_width', hue='species')
# plt.title('Залежність Довжини та Ширини Сепалу за Видами Ірису')
# plt.xlabel('Довжина Сепалу (см)')
# plt.ylabel('Ширина Сепалу (см)')
# plt.show()

# Парні Графіки
# df = sns.load_dataset('iris')
# sns.pairplot(df, hue='species')
# plt.show()

