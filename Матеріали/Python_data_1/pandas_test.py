# data = np.array([[1, 2, 3], [4, 5, 6]])
# df = pd.DataFrame(data, columns=['A', 'B', 'C'])

# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35],
#     'City': ['New York', 'Los Angeles', 'Chicago']
# }
# df = pd.DataFrame(data)

# data = [
#     ['John', 28, 'Engineer'],
#     ['Anna', 22, 'Designer'],
#     ['Mike', 32, 'Manager']
# ]
# df = pd.DataFrame(data, columns=['Name', 'Age', 'Profession'])

# data = [
#     ('Emma', 29, 'Doctor'),
#     ('Liam', 34, 'Lawyer'),
#     ('Olivia', 26, 'Nurse')
# ]
# df = pd.DataFrame(data, columns=['Name', 'Age', 'Profession'])

# data = np.array([
#     ('Tom', 30, 'Teacher'),
#     ('Jerry', 25, 'Artist'),
#     ('Spike', 35, 'Scientist')
# ], dtype=[('Name', 'U10'), ('Age', 'i4'), ('Profession', 'U15')])
# df = pd.DataFrame(data)

# data = {
#     'Name': ['Sara', 'David', 'Laura'],
#     'Age': [27, 32, 24],
#     'City': ['Miami', 'Seattle', 'Boston']
# }
# df_original = pd.DataFrame(data)

# Створіть двовимірний NumPy масив розміру 3x4,
# заповнений числами від 1 до 12. Перетворіть
# цей масив на DataFrame з назвами стовпців ['A', 'B', 'C', 'D']
# data = np.arange(1, 13).reshape(3, 4)
# df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])

# Створіть двовимірний NumPy масив розміру 4x2 з випадковими
# числами з нормальним розподілом (середнє=50, стандартне відхилення=5).
# Перетворіть цей масив на DataFrame з назвами стовпців ['Height', 'Weight']
# data = np.random.normal(50, 5, size=(4, 2))
# df = pd.DataFrame(data, columns=['Height', 'Weight'])

# Створіть словник з наступними ключами та значеннями:
# 'Product': ['Laptop', 'Smartphone', 'Tablet']
# 'Price': [1200, 800, 400]
# 'Stock': [50, 150, 200]
# Перетворіть цей словник на DataFrame.
# data = {
#     'Product': ['Laptop', 'Smartphone', 'Tablet'],
#     'Price': [1200, 800, 400],
#     'Stock': [50, 150, 200]
# }
# df = pd.DataFrame(data)

# Створіть список списків, де кожний внутрішній список
# містить дані про студентів: ім'я, вік та оцінку.
# Перетворіть цей список на DataFrame з назвами стовпців ['Name', 'Age', 'Score'].
# data = [
#     ['John', 22, 88],
#     ['Alice', 23, 92],
#     ['Bob', 24, 75]
# ]
# df = pd.DataFrame(data, columns=['Name', 'Age', 'Score'])

# Створіть список кортежів, де кожен кортеж містить дані про продукт: назва, ціна та кількість.
# Перетворіть цей список на DataFrame з назвами стовпців ['Product', 'Price', 'Quantity'].
# data = [
#     ('Laptop', 1200, 50),
#     ('Smartphone', 800, 150),
#     ('Tablet', 400, 200)
# ]
# df = pd.DataFrame(data, columns=['Product', 'Price', 'Quantity'])

# Створіть структурований NumPy масив з даними про країни: назва, населення та площа.
# data = np.array([
#     ('Ukraine', 44134693, 603500),
#     ('Poland', 38386000, 312679),
#     ('Germany', 83166711, 357022)
# ], dtype=[('Name', 'U10'), ('Population', 'i8'), ('Area', 'i8')])
# df = pd.DataFrame(data)

# Створіть новий DataFrame на основі існуючого, вибираючи лише певні стовпці
# data = {
#     'Name': ['Sara', 'David', 'Laura'],
#     'Age': [27, 32, 24],
#     'City': ['Miami', 'Seattle', 'Boston'],
#     'Salary': [70000, 80000, 75000]
# }
# df_original = pd.DataFrame(data)
# df_new = pd.DataFrame(df_original, columns=['Name', 'Salary'])

# Створіть DataFrame, який містить різні типи даних, такі як числові значення, рядки та дати.
# data = {
#     'ID': [1, 2, 3],
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Signup Date': [datetime(2020, 5, 17), datetime(2021, 6, 21), datetime(2022, 7, 25)],
#     'Score': [88.5, 92.3, 79.8]
# }
# df = pd.DataFrame(data)


# МЕТОДИ ДОСТУПУ ДО ДАНИХ
# data = {
#     'Name': ['Anna', 'Boris', 'Clara', 'Diana'],
#     'Age': [28, 34, 29, 42],
#     'City': ['Kyiv', 'Lviv', 'Odesa', 'Dnipro']
# }
# df = pd.DataFrame(data)
# names = df['Name']
# subset = df[['Name', 'City']]

# Ми використовуємо методи loc та iloc
# для вибору рядків у DataFrame.
# loc дозволяє вибирати рядки за їхніми мітками індексу, тоді як iloc використовує позиційні індекси.
# row = df.loc[1]
# row = df.iloc[0]
# rows = df.iloc[0:2]

# Фільтрація даних за умовами
# filtered_df = df[df['Age'] > 30]
# filtered_df = df[df['City'].isin(['Kyiv', 'Odesa'])]
# filtered_df = df[(df['Age'] > 30) & (df['City'] == 'Lviv')]


# Завдання 1.1: Вибір одного стовпця
# data = {
#     'Name': ['Anna', 'Boris', 'Clara', 'Diana'],
#     'Age': [28, 34, 29, 42],
#     'City': ['Kyiv', 'Lviv', 'Odesa', 'Dnipro']
# }
# df = pd.DataFrame(data)
# print(df['Age'])

# Виберіть всі рядки, де назва міста починається з літери 'O'
# result = df.loc[df['City'].str.startswith('O')]

# Завдання 1.2
# Наступне завдання обрати стовпці 'Name' та 'City'
# і створіть новий DataFrame з цими стовпцями.
# subset = df[['Name', 'City']]

# Завдання 2.1
# Виберіть другий рядок DataFrame за допомогою loc (індекс 1) та виведіть його.
# row_loc = df.loc[1]

# Завдання 2.2
# Виберіть перший рядок DataFrame за допомогою iloc (позиційний індекс 0) та виведіть його.
# row_iloc = df.iloc[0]

# Завдання 2.3
# Виберіть перші три рядки DataFrame за допомогою iloc та виведіть їх.
# rows = df.iloc[0:3]

# Завдання 3.1: Фільтрація рядків за однією умовою
# Виберіть всі рядки, де 'Age' більше 40 років.
# filtered_df = df[df['Age'] > 40]

# Завдання 3.2
# Виберіть всі рядки, де 'Age' більше 25 років та 'City' — 'Kyiv' або 'Odesa'
# filtered_df = df[(df['Age'] > 25) & (df['City'].isin(['Kyiv', 'Odesa']))]

# Завдання 3.3
# Використовуючи loc, виберіть всі рядки, де 'City' дорівнює 'Lviv' або 'Dnipro'
# filtered_df = df.loc[df['City'].isin(['Lviv', 'Dnipro'])]

# Завдання 4.1
# Виберіть всі рядки, де 'Age' більше 28 років, та виведіть лише стовпці 'Name' та 'City'
# filtered_subset = df[df['Age'] > 28][['Name', 'City']]

# Завдання 4.2
# Виберіть всі рядки, де 'Age' більше 25 років або 'City' — 'Kyiv'
# filtered_df = df[(df['Age'] > 25) | (df['City'] == 'Kyiv')]

# Завдання 4.3: Фільтрація з числовими умовами
# Завдання: Виберіть всі рядки, де 'Age' знаходиться в діапазоні від 30 до 40 років включно
# filtered_df = df[df['Age'].between(30, 40)]


# data = {
#     'Employee': ['John', 'Emma', 'Oliver', 'Sophia', 'Liam'],
#     'Department': ['HR', 'Finance', 'IT', 'Marketing', 'IT'],
#     'Salary': [50000, 70000, 60000, 65000, 62000],
#     'Age': [28, 34, 29, 42, 31]
# }
# Виберіть всі стовпці 'Employee' та 'Salary'.
# Виберіть третій рядок за допомогою iloc.
# Виберіть всі працівники з 'Department' — 'IT'.
# Виберіть всі працівники, де 'Salary' більше 60000 та 'Age' менше 35 років.


# data = {
#     'Product': ['Laptop', 'Smartphone', 'Tablet', 'Monitor', 'Keyboard'],
#     'Price': [1200, 800, 400, 300, 50],
#     'Stock': [50, 150, 200, 80, 500]
# }
# Виберіть всі продукти, де 'Price' більше 500.
# Виберіть всі продукти, де 'Stock' менше 100 або 'Price' більше 1000.
# Виберіть лише 'Product' та 'Stock' для продуктів, де 'Price' дорівнює 400.
# Використовуючи метод isin, виберіть всі продукти, які знаходяться у списку ['Laptop', 'Monitor']


# data = {
#     'Student': ['Tom', 'Jerry', 'Mickey', 'Donald', 'Goofy'],
#     'Grade': ['A', 'B', 'A', 'C', 'B'],
#     'Age': [20, 21, 19, 22, 20]
# }
# Виберіть і виведіть імена студентів, які мають оцінку 'A' та віком менше 21 року.


# ДОДАВАННЯ ТА ВИДАЛЕННЯ СТОВПЦІВ ТА РЯДКІВ
# data = {
#     'Name': ['Anna', 'Boris', 'Clara'],
#     'Age': [28, 34, 29],
#     'City': ['Kyiv', 'Lviv', 'Odesa']
# }
# df = pd.DataFrame(data)
# df['Country'] = 'Ukraine'
# df['Age in 5 Years'] = df['Age'] + 5

# def age_category(age):
#     if age < 30:
#         return 'Young'
#     else:
#         return 'Adult'
# df['Age Category'] = df['Age'].apply(age_category)
# df = df.drop('Country', axis=1)
# df = df.drop(1, axis=0)
# df = df.drop(['Age in 5 Years', 'Age Category'], axis=1)

# new_data = {
#     'Name': ['Eva', 'Frank'],
#     'Age': [35, 45],
#     'City': ['Kharkiv', 'Zaporizhzhia']
# }
# new_df = pd.DataFrame(new_data)
# df = pd.concat([df, new_df], ignore_index=True)

# 3. Додавання рядка з іншого DataFrame
# additional_data = {
#     'Name': ['Grace', 'Hank'],
#     'Age': [31, 38],
#     'City': ['Vinnytsia', 'Chernihiv']
# }
# additional_df = pd.DataFrame(additional_data)
# df = pd.concat([df, additional_df], ignore_index=True)

# Завдання 1
# Створимо DataFrame з наступними даними:
# data = {
#     'Product': ['Laptop', 'Smartphone', 'Tablet'],
#     'Price': [1200, 800, 400],
#     'Stock': [50, 150, 200]
# }
# df = pd.DataFrame(data)
# df['Category'] = 'Electronics'
# df['Price with Tax'] = df['Price'] * 1.20

# def stock_level(stock):
#     if stock < 100:
#         return 'Low'
#     else:
#         return 'High'
# df['Stock Level'] = df['Stock'].apply(stock_level)

# def calculate_discount(price):
#     if price > 500:
#         return '10%'
#     else:
#         return '5%'
# df['Discount'] = df['Price'].apply(calculate_discount)

# Завдання 5
# data = {
#     'Employee': ['Liam', 'Emma', 'Noah', 'Olivia', 'Ava'],
#     'Department': ['IT', 'HR', 'Finance', 'IT', 'Marketing'],
#     'Salary': [60000, 50000, 70000, 62000, 58000],
#     'Age': [28, 34, 29, 42, 31]
# }
# df = pd.DataFrame(data)
# Виберіть всі стовпці 'Employee' та 'Salary'.
# Виберіть третій рядок за допомогою iloc.
# Виберіть всіх працівників з 'Department' — 'IT'.
# Виберіть всіх працівників, де 'Salary' більше 60000 та 'Age' менше 35 років.
# Виберіть всі рядки, де назва міста починається з літери 'O'.