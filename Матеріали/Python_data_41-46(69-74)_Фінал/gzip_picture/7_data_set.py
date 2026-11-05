import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import accuracy_score, f1_score, mean_squared_error, r2_score
import seaborn as sns
import matplotlib.pyplot as plt
import kagglehub
from kagglehub import KaggleDatasetAdapter


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
# АГРЕГАЦІЯ ДАНИХ НА РІВНІ КОРИСТУВАЧІВ
# ---------------------------------------------------------
# Одразу після завантаження або перед агрегацією зменшимо вибірку для швидкості,
# якщо датасет занадто великий (наприклад, залилимо 1 мільйон випадкових рядків)
if len(df) > 1_000_000:
  print("Датасет великий, робимо вибірку в 1 млн рядків для прискорення...")
  df = df.sample(n=1_000_000, random_state=42)

print("Агрегація даних на рівні користувачів (оптимізовано)...")

# Створюємо швидкі числові індикатори замість повільних лямбд
df['is_view'] = (df['event_type'] == 'view').astype(int)
df['is_cart'] = (df['event_type'] == 'cart').astype(int)
df['is_purchase'] = (df['event_type'] == 'purchase').astype(int)

# Векторизована агрегація працює миттєво
user_agg = (
    df.groupby('user_id')
    .agg(
        view_count=('is_view', 'sum'),
        cart_count=('is_cart', 'sum'),
        purchase_count=('is_purchase', 'sum'),
        total_sessions=('user_session', 'nunique'),
        avg_price=('price', 'mean'),
    )
    .reset_index()
)

# Заповнення можливих пропусків нулями
user_agg = user_agg.fillna(0)
print(f"Агрегацію завершено! Отримано унікальних користувачів: {len(user_agg)}")

# ---------------------------------------------------------
# 1. СЕГМЕНТАЦІЯ КОРИСТУВАЧІВ (KMeans)
# ---------------------------------------------------------
print("\n[1/5] Проведення сегментації користувачів (KMeans)...")
clustering_features = ['view_count', 'cart_count', 'purchase_count', 'total_sessions']
scaler = StandardScaler()
X_scaled = scaler.fit_transform(user_agg[clustering_features])

# Визначаємо 3 кластери для виділення профілів
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
user_agg['cluster'] = kmeans.fit_predict(X_scaled)

# Аналіз середніх показників у кластерах для визначення профілів
cluster_profiles = user_agg.groupby('cluster')[clustering_features].mean()
print("Середні показники активності за кластерами:\n", cluster_profiles)

# ---------------------------------------------------------
# 2. ВДІБІР ОЗНАК ЗА ДОПОМОГОЮ SelectKBest
# ---------------------------------------------------------
print("\n[2/5] Відбір найбільш релевантних ознак (SelectKBest)...")
# Створення цільової змінної 'high_engagement' (користувачі з активністю вище медіани)
user_agg['total_activity'] = user_agg['view_count'] + user_agg['cart_count'] + user_agg['purchase_count']
median_activity = user_agg['total_activity'].median()
user_agg['high_engagement'] = (user_agg['total_activity'] > median_activity).astype(int)

X_features = user_agg[['view_count', 'cart_count', 'purchase_count', 'total_sessions', 'avg_price']]
y_class = user_agg['high_engagement']

# Вибираємо топ-3 найбільш релевантні ознаки
selector = SelectKBest(score_func=f_classif, k=3)
X_selected = selector.fit_transform(X_features, y_class)
selected_features = X_features.columns[selector.get_support()].tolist()
print(f"Найбільш релевантні ознаки (SelectKBest): {selected_features}")

# ---------------------------------------------------------
# 3 & 4. КЛАСИФІКАЦІЯ (Logistic Regression)
# ---------------------------------------------------------
print("\n[3/5] Побудова та оцінка моделі класифікації...")
X_train, X_test, y_train, y_test = train_test_split(X_selected, y_class, test_size=0.2, random_state=42)

clf = LogisticRegression()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

acc = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average='weighted')
print(f"Метрики класифікації -> Accuracy: {acc:.4f} | F1-score: {f1:.4f}")

# ---------------------------------------------------------
# 5. РЕГРЕСІЯ (Linear Regression)
# ---------------------------------------------------------
print("\n[4/5] Побудова та оцінка моделі регресії...")
# Прогнозуємо загальну кількість подій (quantitative metric)
y_reg = user_agg['total_activity']
X_reg_features = user_agg[['view_count', 'cart_count', 'purchase_count', 'total_sessions']]

X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X_reg_features, y_reg, test_size=0.2, random_state=42)

reg = LinearRegression()
reg.fit(X_train_r, y_train_r)
y_pred_r = reg.predict(X_test_r)

mse = mean_squared_error(y_test_r, y_pred_r)
r2 = r2_score(y_test_r, y_pred_r)
print(f"Метрики регресії -> MSE: {mse:.4f} | R²: {r2:.4f}")

print("\n[5/5] Усі завдання успішно виконано!")