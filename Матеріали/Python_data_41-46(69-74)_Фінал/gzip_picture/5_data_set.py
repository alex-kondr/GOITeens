import kagglehub
from kagglehub import KaggleDatasetAdapter

# Set the path to the file you'd like to load
file_path = ""

# Load the latest version
df = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "mkechinov/ecommerce-behavior-data-from-multi-category-store",
  file_path,
  # Provide any additional arguments like 
  # sql_query or pandas_kwargs. See the 
  # documenation for more information:
  # https://github.com/Kaggle/kagglehub/blob/main/README.md#kaggledatasetadapterpandas
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