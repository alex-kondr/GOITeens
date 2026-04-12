# df['ColumnName'] = df['ColumnName'].astype(NewType)

# data = {
#     'Product': ['Laptop', 'Smartphone', 'Tablet'],
#     'Price': [1200.50, 800.75, 400.20],
#     'Stock': [50, 150, 200]
# }
# df['Price'] = df['Price'].astype(int)

# data = {
#     'Event': ['Conference', 'Meeting', 'Workshop'],
#     'Date': ['2024-05-21', '2024-06-15', '2024-07-10']
# }
# df = pd.DataFrame(data)
# df['Date'] = pd.to_datetime(df['Date'])

# При спробі перетворити стовпець на тип, який не сумісний з його даними, виникнуть помилки.
# Потрібно використовувати параметр errors для керування такими ситуаціями.
# data = {
#     'Value': ['10', '20', 'thirty', '40']
# }
# df = pd.DataFrame(data)
# df['Value'] = pd.to_numeric(df['Value'], errors='coerce')

# 1. errors='raise' (Значення за замовчуванням)
# Якщо функція зустрічає значення, яке не є числом, вона зупиняє роботу і видає помилку ValueError.
# 2. errors='coerce'
# Це найпопулярніший варіант. Якщо значення не вдається перетворити на число, pandas замінює його на NaN (Not a Number — "не число").
# 3. errors='ignore'
# Якщо функція зустрічає некоректне значення, вона просто повертає вхідні дані без будь-яких змін.


# Метод rename дозволяє змінювати назви стовпців або індексів.
# df.rename(columns={'OldName': 'NewName'}, inplace=True)
# columns: Словник, де ключі — старі назви стовпців, а значення — нові.
# inplace: Якщо True, зміни будуть застосовані безпосередньо до DataFrame.

# data = {
#     'Product': ['Laptop', 'Smartphone', 'Tablet'],
#     'Price': [1200, 800, 400],
#     'Stock': [50, 150, 200]
# }
# df = pd.DataFrame(data)
# df.rename(columns={'Price': 'Cost'}, inplace=True)

# data = {
#     'Name': ['Alex', 'Bella', 'Chris'],
#     'Age': [30, 25, 35],
#     'City': ['Kyiv', 'Lviv', 'Odesa']
# }
# df = pd.DataFrame(data)
# Перейменуємо стовпці 'Name' на 'Employee Name' та 'City' на 'Location'.
# df.rename(columns={'Name': 'Employee Name', 'City': 'Location'}, inplace=True)

# data = {
#     'Name': ['Anna', 'Boris', 'Clara', 'Diana'],
#     'Age': [28, np.nan, 29, 42],
#     'City': ['Kyiv', 'Lviv', np.nan, 'Dnipro']
# }
# df = pd.DataFrame(data)
# Метод dropna видаляє рядки або стовпці з пропущеними значеннями
# df.dropna(axis=0, how='any', inplace=True)
# axis=0: Видаляються рядки.
# axis=1: Видаляються стовпці.
# how='any': Видаляється рядок, якщо хоча б одне значення пропущене.
# how='all': Видаляється рядок лише якщо всі значення пропущені.
# inplace=True: Зміни застосовуються безпосередньо до DataFrame.
# df_clean = df.dropna()

# Метод fillna дозволяє заповнювати пропущені значення певним значенням або методом.
# df.fillna(value, inplace=True)
# value: Значення або словник для заповнення пропущених значень.
# inplace=True: Зміни застосовуються безпосередньо до DataFrame.
# mean_age = df['Age'].mean()
# df.fillna({'Age': mean_age}, inplace=True)

# Заповнимо пропущених значень методом 'ffill' (forward fill)
# df['City'] = df['City'].ffill()

# Інтерполяція це ****заповнення пропущених значень шляхом інтерполяції між сусідніми значеннями.
# df['Age'].interpolate(method='linear', inplace=True)


# Перевірка пропущених значень

# isna() або isnull(): Повертає булевий DataFrame, де True позначає пропущені значення.
# sum(): Підраховує кількість пропущених значень у кожному стовпці.
# info(): Показує загальну інформацію про DataFrame, включаючи кількість ненульових значень у кожному стовпці.

# data = {
#     'Name': ['Anna', 'Boris', 'Clara', 'Diana'],
#     'Age': [28, np.nan, 29, 42],
#     'City': ['Kyiv', 'Lviv', np.nan, 'Dnipro'],
#     'Salary': [50000, 60000, np.nan, 70000]
# }
# df = pd.DataFrame(data)
# df.isna()
# Підрахунок пропущених значень у кожному стовпці. df.isna().sum() підраховує кількість пропущених значень у кожному стовпці.
# df.isna().sum()
# Інформація про DataFrame. df.info() надає загальну інформацію про DataFrame, включаючи типи даних та кількість ненульових значень.
# df.info()


# імпортувати CSV-файл
# Читаємо файл, ігноруючи структурні помилки (зайві коми)
# df = pd.read_csv('file.csv', on_bad_lines='skip')
# Конвертуємо Price, перетворюючи помилкові типи на NaN
# df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
# Видаляємо рядки, де Price став NaN (тобто був помилковим)
# df = df.dropna(subset=['Price'])


# data = {
#     'Product': ['Laptop', 'Smartphone', 'Tablet'],
#     'Price': [1200.50, 800.75, 400.20],
#     'Stock': [50, 150, 200]
# }
# df = pd.DataFrame(data)
# Змінимо тип стовпця 'Price' з float64 на int64.
# df['Price'] = df['Price'].astype(int)

# data = {
#     'Event': ['Conference', 'Meeting', 'Workshop'],
#     'Date': ['2024-05-21', '2024-06-15', '2024-07-10']
# }
# df = pd.DataFrame(data)
# Перетворимо стовпець 'Date' на тип datetime.
# df['Date'] = pd.to_datetime(df['Date'])

# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Department': ['HR', 'IT', 'Finance', 'IT'],
#     'Salary': [50000, 60000, 55000, 62000]
# }
# df = pd.DataFrame(data)
# Змінимо тип стовпця 'Department' на category.
# df['Department'] = df['Department'].astype('category')

# data = {
#     'Item': ['Book', 'Pen', 'Notebook'],
#     'Quantity': [10, 50, 30],
#     'Price': [15, 1, 5]
# }
# df = pd.DataFrame(data)
# Змінимо тип стовпця 'Price' на float.
# df['Price'] = df['Price'].astype(float)

# data = {
#     'Name': ['Anna', 'Boris', 'Clara'],
#     'Age': [28, 34, 29],
#     'City': ['Kyiv', 'Lviv', 'Odesa']
# }
# df = pd.DataFrame(data)
# Перейменовуємо стовпець City на Location
# df.rename(columns={'City': 'Location'}, inplace=True)

# data = {
#     'Name': ['Eve', 'Frank', 'Grace'],
#     'Age': [29, 34, 31],
#     'Salary': ['50000', '60000', '55000']
# }
# df = pd.DataFrame(data)
# Змініть тип стовпця 'Salary' з object на int64 за допомогою astype.

# data = {
#     'FirstName': ['Helen', 'Ian', 'Jack'],
#     'LastName': ['Taylor', 'Smith', 'Brown'],
#     'Age': [25, 30, 28]
# }
# df = pd.DataFrame(data)
# Перейменуйте стовпці 'FirstName' на 'Name' та 'LastName' на 'Surname'.

# data = {
#     'Name': ['Karen', 'Leo', 'Mona'],
#     'Age': [27, 32, 26],
#     'City': ['Kyiv', 'Lviv', 'Odesa'],
#     'Salary': [48000, 52000, 50000]
# }
# df = pd.DataFrame(data)
# Видаліть стовпець 'City' за допомогою методу drop.

# data = {
#     'Name': ['Nina', 'Oscar', 'Paul'],
#     'Age': [24, 35, 29],
#     'Salary': [45000, 70000, 62000]
# }
# df = pd.DataFrame(data)
# Додайте новий стовпець 'Tax', який дорівнює 20% від 'Salary' для всіх рядків.

# data = {
#     'Product': ['Laptop', 'Smartphone', 'Tablet'],
#     'Price': [1200, 800, 400],
#     'Stock': [50, 150, 200]
# }
# df = pd.DataFrame(data)
# Додайте новий рядок {'Product': 'Monitor', 'Price': 200, 'Stock': 80} до DataFrame за допомогою concat.


# Імпорт даних із файлів CSV

# df = pd.read_csv('path_to_file.csv')
# filepath_or_buffer: Шлях до файлу або URL. Може бути локальним шляхом до файлу на вашому комп'ютері або посиланням на файл в Інтернеті.
# sep: Роздільник, який використовується для розділення значень у файлі. За замовчуванням це кома (,), але може бути змінений на будь-який інший символ, наприклад, крапка з комою (;) або табуляція (\\t).
# header: Вказує рядок, що містить заголовки стовпців. За замовчуванням header=0, тобто перший рядок файлу розглядається як заголовок. Якщо заголовків немає, встановіть header=None.

# encoding
# utf-8: Стандартне кодування для більшості сучасних файлів.
# latin1, ISO-8859-1: Інші популярні кодування.
# cp1251: Кодування для кириличних текстів.

# usecols: Вибір лише певних стовпців для імпорту.
# df = pd.read_csv('onboarding_username_minimum.csv', sep=';', usecols=['Username', 'First name'])

# dtype: Визначення типів даних для стовпців.
# df = pd.read_csv('onboarding_username_minimum.csv', sep=';', dtype={'Identifier': str})

# na_values: Визначення значень, які будуть розпізнані як пропущені (NaN)
# df = pd.read_csv('onboarding_username_missing_values.csv', sep=';', na_values=['NULL', 'N/A'])

# df.to_csv('path_to_new_file.csv', index=False)
# path_or_buf: Шлях до файлу або об'єкт буфера.
# sep: Роздільник (за замовчуванням ,).
# index: Чи зберігати індекс (за замовчуванням True). Часто встановлюють False, щоб уникнути збереження числового індексу.
# header: Чи зберігати заголовки стовпців (за замовчуванням True).

# df_mixed_types = pd.read_csv('addresses.csv', dtype={'Identifier': str}, on_bad_lines='skip')


# Метод .groupby()
# grouped = df.groupby('column_name')
# grouped = df.groupby(['column1', 'column2'])

# data = {
#     'Department': ['Sales', 'Engineering', 'Sales', 'HR', 'Engineering', 'HR'],
#     'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
#     'Salary': [70000, 80000, 75000, 60000, 82000, 58000]
# }
# df = pd.DataFrame(data)
# grouped = df.groupby('Department')
# average_salary = grouped['Salary'].mean()

# data = {
#     'Department': ['Sales', 'Engineering', 'Sales', 'HR', 'Engineering', 'HR', 'Sales'],
#     'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
#     'Salary': [70000, 80000, 75000, 60000, 82000, 58000, 72000],
#     'Region': ['North', 'South', 'North', 'East', 'South', 'East', 'West']
# }
# grouped_multiple = df.groupby(['Department', 'Region'])
# agg_results = grouped_multiple.agg(
#     Total_Salary=('Salary', 'sum'),
#     Employee_Count=('Employee', 'count')
# )

# Агрегаційні операції

# Після групування даних можна виконувати різноманітні агрегаційні операції:
# Середнє значення (mean()): Обчислює середнє значення для кожної групи.
# Сума (sum()): Обчислює суму значень для кожної групи.
# Підрахунок (count()): Обчислює кількість елементів у кожній групі.
# Мінімум та максимум (min(), max()): Знаходить мінімальні та максимальні значення у групах.
# Стандартне відхилення (std()): Обчислює стандартне відхилення для кожної групи.

# agg_functions = grouped.agg(
#     Average_Salary=('Salary', 'mean'),
#     Total_Salary=('Salary', 'sum'),
#     Employee_Count=('Employee', 'count'),
#     Max_Salary=('Salary', 'max'),
#     Min_Salary=('Salary', 'min')
# )

# Створення Агрегаційної Таблиці

# agg_table = grouped.agg(
#     Average_Salary=('Salary', 'mean'),
#     Total_Salary=('Salary', 'sum'),
#     Employee_Count=('Employee', 'count')
# )
# import matplotlib.pyplot as plt

# agg_table['Average_Salary'].plot(kind='bar', color='skyblue')
# plt.title('Середня Зарплата за Департаментами')
# plt.xlabel('Департамент')
# plt.ylabel('Середня Зарплата')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# data = {
#     'Department': ['Sales', 'Engineering', 'Sales', 'HR', 'Engineering', 'HR'],
#     'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
#     'Salary': [70000, 80000, 75000, 60000, 82000, 58000]
# }
# df = pd.DataFrame(data)
# grouped = df.groupby('Department')
# average_salary = grouped['Salary'].mean()
# count_employees = grouped['Employee'].count()
# agg_results = grouped.agg(
#     Average_Salary=('Salary', 'mean'),
#     Total_Salary=('Salary', 'sum'),
#     Employee_Count=('Employee', 'count')
# )

# data = {
#     'Department': ['Sales', 'Engineering', 'Sales', 'HR', 'Engineering', 'HR', 'Sales'],
#     'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
#     'Salary': [70000, 80000, 75000, 60000, 82000, 58000, 72000],
#     'Region': ['North', 'South', 'North', 'East', 'South', 'East', 'West']
# }
# df = pd.DataFrame(data)
# grouped_multiple = df.groupby(['Department', 'Region'])
# agg_multiple = grouped_multiple.agg(
#     Total_Salary=('Salary', 'sum'),
#     Employee_Count=('Employee', 'count')
# )

# data = {
#     'Region': ['North', 'South', 'North', 'East', 'West', 'South', 'East', 'West'],
#     'Product': ['Laptop', 'Smartphone', 'Tablet', 'Laptop', 'Tablet', 'Laptop', 'Smartphone', 'Tablet'],
#     'Sales': [1200, 1500, 800, 1300, 900, 1100, 1600, 850],
#     'Quantity': [10, 15, 8, 13, 9, 11, 16, 8]
# }
# df = pd.DataFrame(data)
# grouped = df.groupby(['Region', 'Product'])
# agg_results = grouped.agg(
#     Total_Sales=('Sales', 'sum'),
#     Average_Sales=('Sales', 'mean'),
#     Total_Quantity=('Quantity', 'sum'),
#     Average_Quantity=('Quantity', 'mean')
# ).reset_index()

# data = {
#     'Category': ['Utilities', 'Office Supplies', 'Utilities', 'Office Supplies', 'Travel', 'Travel', 'Utilities', 'Office Supplies'],
#     'Month': ['January', 'January', 'February', 'February', 'January', 'February', 'March', 'March'],
#     'Amount': [300, 150, 200, 180, 400, 350, 250, 170]
# }
# df = pd.DataFrame(data)
# grouped = df.groupby(['Category', 'Month'])
# agg_results = grouped.agg(
#     Total_Amount=('Amount', 'sum'),
#     Average_Amount=('Amount', 'mean'),
#     Transaction_Count=('Amount', 'count')
# ).reset_index()


# Завдання 1
# Department,Employee,Salary
# Sales,Alice,70000
# Engineering,Bob,80000
# Sales,Charlie,75000
# HR,David,60000
# Engineering,Eve,82000
# HR,Frank,58000
# Sales,Grace,72000
# Завдання:
# Імпортуйте дані з файлу employees.csv у Pandas DataFrame.
# Групуйте дані за стовпцем 'Department'.
# Обчисліть середню зарплату для кожного департаменту.
# Виведіть отримані результати.


# Завдання 2
# Department,Employee,Salary,Region
# Sales,Alice,70000,North
# Engineering,Bob,80000,South
# Sales,Charlie,75000,North
# HR,David,60000,East
# Engineering,Eve,82000,South
# HR,Frank,58000,East
# Sales,Grace,72000,West
# Завдання:
# Імпортуйте дані з файлу employees_region.csv у Pandas DataFrame.
# Групуйте дані за стовпцями 'Department' та 'Region'.
# Обчисліть суму зарплат та кількість співробітників для кожної групи.
# Виведіть отримані результати у вигляді таблиці.


# Методи
# Метод .reset_index(): Метод, який перетворює мультиіндексований DataFrame у звичайний з новими числовими індексами.
# Метод .unstack(): Метод, який перетворює рівень індексу в стовпці, створюючи широкі таблиці.
# Метод .pivot_table(): Альтернативний метод для створення агрегаційних таблиць з можливістю багатовимірного групування та агрегації.

# data = {
#     'Department': ['Sales', 'Engineering', 'Sales', 'HR', 'Engineering', 'HR', 'Sales'],
#     'Region': ['North', 'South', 'North', 'East', 'South', 'East', 'West'],
#     'Sales': [1200, 1500, 800, 600, 1600, 750, 900],
#     'Quantity': [10, 15, 8, 5, 20, 7, 9]
# }
# df = pd.DataFrame(data)
# grouped = df.groupby(['Department', 'Region']).agg(
#     Total_Sales=('Sales', 'sum'),
#     Average_Sales=('Sales', 'mean'),
#     Total_Quantity=('Quantity', 'sum'),
#     Average_Quantity=('Quantity', 'mean')
# )
# agg_table = grouped.reset_index()
# grouped_sum = df.groupby(['Department', 'Region'])['Sales'].sum().unstack()
# pivot_avg_salary = pd.pivot_table(
#     df,
#     values='Sales',
#     index='Department',
#     columns='Region',
#     aggfunc='mean'
# )
# pivot_sum_sales = pd.pivot_table(
#     df,
#     values='Sales',
#     index='Department',
#     columns='Region',
#     aggfunc='sum'
# )

# plt.figure(figsize=(8, 6))
# sns.heatmap(pivot_sum_sales, annot=True, fmt=".0f", cmap="YlGnBu")
# plt.title('Сума Продажів за Департаментом та Регіоном')
# plt.xlabel('Region')
# plt.ylabel('Department')
# plt.show()


# Region,Product,Sales,Quantity
# North,Laptop,1200,10
# South,Smartphone,1500,15
# North,Tablet,800,8
# East,Laptop,1300,13
# South,Tablet,900,9
# East,Smartphone,1600,16
# West,Tablet,850,8
# Завдання:
# Імпортуйте дані з файлу company_sales.csv у Pandas DataFrame.
# Групуйте дані за стовпцями 'Region' та 'Product'.
# Обчисліть для кожної групи:
# Сума продажів ('Sales').
# Середнє значення продажів.
# Кількість транзакцій ('Quantity').
# Перетворіть результати групування у звичайну таблицю з використанням .reset_index().
# Виведіть отриману агрегаційну таблицю.


# Category,Month,Amount
# Utilities,January,300
# Office Supplies,January,150
# Utilities,February,200
# Office Supplies,February,180
# Travel,January,400
# Travel,February,350
# Utilities,March,250
# Office Supplies,March,170
# Завдання:
# Імпортуйте дані з файлу company_expenses.csv у Pandas DataFrame.
# Створіть Pivot Table для обчислення суми та середнього значення витрат за категоріями та місяцями.
# Виведіть отриману Pivot Table.
# Імпортуємо дані з CSV-файлу
# pivot_expenses = pd.pivot_table(
#     df_expenses,
#     values='Amount',
#     index='Category',
#     columns='Month',
#     aggfunc=['sum', 'mean'],
#     fill_value=0
# )

# Employee,Project,Month,Performance_Score
# John,Alpha,January,85
# John,Beta,January,78
# Anna,Alpha,January,92
# Anna,Beta,February,88
# Mike,Alpha,February,75
# Mike,Beta,March,80
# Sara,Alpha,March,95
# Sara,Beta,April,90
# Tom,Alpha,April,70
# Tom,Beta,May,65
# Завдання:
# 1.Імпортуйте дані з файлу employee_performance.csv у Pandas DataFrame.
# 2.Групуйте дані за стовпцями 'Project' та 'Month'.
# 3.Обчисліть для кожної групи:
# Середній бал продуктивності ('Performance_Score').
# Максимальний бал продуктивності.
# 4.Перетворіть результати групування у звичайну таблицю.
# 5.Виведіть отриману агрегаційну таблицю.

# Store,Quarter,Product,Sales
# Store_A,Q1,Laptop,5000
# Store_A,Q1,Smartphone,7000
# Store_A,Q2,Laptop,6000
# Store_A,Q2,Smartphone,8000
# Store_B,Q1,Laptop,4000
# Store_B,Q1,Smartphone,6500
# Store_B,Q2,Laptop,5500
# Store_B,Q2,Smartphone,7500
# Store_C,Q1,Laptop,3000
# Store_C,Q1,Smartphone,5000
# Store_C,Q2,Laptop,4500
# Store_C,Q2,Smartphone,6000
# Завдання:
# Імпортуйте дані з файлу store_sales.csv у Pandas DataFrame.
# Створіть Pivot Table для обчислення суми продажів за магазинами та продуктами.
# Виведіть отриману Pivot Table.
# Побудуйте теплову карту (heatmap) для візуалізації сум продажів.