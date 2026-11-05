import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Налаштування стилю візуалізацій
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# 1. Завантаження датасету через Kagglehub (наприклад, файл за жовтень 2019 року)
file_path = "2019-Oct.csv"

print("Завантаження даних із Kaggle...")
df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "mkechinov/ecommerce-behavior-data-from-multi-category-store",
    file_path
)
print(f"Датасет успішно завантажено. Розмірність: {df.shape}")

# ---------------------------------------------------------
# ПУНКТ 1 & 2: Обробка пропущених значень та конвертація дат
# ---------------------------------------------------------
print("\n[1/5] Обробка пропущених значень та дат...")

# Перетворення стовпця з часом у правильний формат datetime
df['event_time'] = pd.to_datetime(df['event_time'])

# Обробка пропущених значень:
# Для категоріальних змінних (наприклад, category_code, brand) заповнюємо значенням 'Unknown'
df['category_code'] = df['category_code'].fillna('Unknown')
df['brand'] = df['brand'].fillna('Unknown')

# Якщо є числові пропуски в ціні (price), заповнюємо медіаною
if 'price' in df.columns:
    df['price'] = df['price'].fillna(df['price'].median())

# Видалення рядків із будь-якими іншими критичними пропусками (якщо залишилися)
df = df.dropna(subset=['event_type', 'product_id', 'user_id'])

# ---------------------------------------------------------
# ПУНКТ 3: Виявлення та видалення дублікатів
# ---------------------------------------------------------
print("\n[2/5] Очищення від дублікатів та некоректних записів...")
initial_rows = df.shape[0]
df = df.drop_duplicates()
print(f"Видалено дублікатів: {initial_rows - df.shape[0]}")

# Фільтрація аномальних значень (наприклад, ціна не може бути від'ємною)
if 'price' in df.columns:
    df = df[df['price'] >= 0]

# ---------------------------------------------------------
# ПУНКТ 4: Перетворення категоріальних змінних
# ---------------------------------------------------------
print("\n[3/5] Кодування категоріальних змінних...")
# Приклад використання Label Encoding або One-Hot Encoding для event_type
# (Для економії пам'яті великих датасетів краще використовувати category type або Label Encoding)
df['event_type_code'] = df['event_type'].astype('category').cat.codes

# ---------------------------------------------------------
# ПУНКТ 5: Створення нових ознак (Feature Engineering)
# ---------------------------------------------------------
print("\n[4/5] Створення нових ознак...")
# Додаємо часові ознаки на основі event_time
df['hour'] = df['event_time'].dt.hour
df['day_of_week'] = df['event_time'].dt.day_name()

# Розрахунок середнього часу перегляду або кількості подій за сесією (user_session)
# Наприклад, тривалість сесії або кількість кліків у сесії:
session_activity = df.groupby('user_session').size().reset_index(name='session_events_count')
df = df.merge(session_activity, on='user_session', how='left')

# ---------------------------------------------------------
# ПУНКТ 6, 7, 8: Візуалізація даних та аналіз аномалій
# ---------------------------------------------------------
print("\n[5/5] Генерація графіків...")

# Зменшимо вибірку для швидшої побудови графіків, якщо датасет занадто великий
df_sample = df.sample(n=min(50000, len(df)), random_state=42)

# 1. Лінійний графік: тренди активності користувачів за годинами доби
plt.figure()
hourly_activity = df.groupby('hour')['product_id'].count()
hourly_activity.plot(kind='line', marker='o', color='b', title='Тренд активності користувачів за годинами доби')
plt.xlabel('Година доби')
plt.ylabel('Кількість подій')
plt.savefig('hourly_trend.png')
plt.close()

# 2. Бар-чарт: порівняння популярності типів подій (view, cart, purchase)
plt.figure()
df['event_type'].value_counts().plot(kind='bar', color=['skyblue', 'orange', 'green'], title='Популярність типів подій')
plt.xlabel('Тип події')
plt.ylabel('Кількість')
plt.xticks(rotation=0)
plt.savefig('event_types_bar.png')
plt.close()

# 3. Гістограма та Boxplot для виявлення аномалій у цінах (price)
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Гістограма розподілу цін
sns.histplot(df_sample[df_sample['price'] < 500]['price'], bins=50, ax=axes[0], color='purple')
axes[0].set_title('Розподіл цін товарів (до 500 у.о.)')
axes[0].set_xlabel('Ціна')

# Boxplot для пошуку викидів
sns.boxplot(x=df['price'], ax=axes[1], color='red')
axes[1].set_title('Boxplot ціни товарів для виявлення аномалій')
axes[1].set_xlabel('Ціна')

plt.tight_layout()
plt.savefig('price_distribution_and_box.png')
plt.close()

print("\n Усі завдання успішно виконано! Графіки збережено у файли ('hourly_trend.png', 'event_types_bar.png', 'price_distribution_and_box.png').")