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
