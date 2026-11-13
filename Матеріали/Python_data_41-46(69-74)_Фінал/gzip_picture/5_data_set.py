import kagglehub
from kagglehub import KaggleDatasetAdapter

# Set the path to the file you'd like to load
file_path = "2019-Dec.csv"

print("Завантаження даних із Kaggle...")
df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "mkechinov/ecommerce-events-history-in-cosmetics-shop",
    file_path
)

print("First 5 records:", df.head())

# Загальна інформація про структуру та типи даних
print(df.info())

# Виведення назв усіх колонок
print(df.columns)

missing_values = df.isnull().sum()
print(missing_values)

# Перевірка кількості дублікатів до видалення
print(f"Кількість дублікатів: {df.duplicated().sum()}")

# Видалення дублікатів
df = df.drop_duplicates()

# Перевірка результату
print(f"Кількість рядків після очищення: {df.shape[0]}")