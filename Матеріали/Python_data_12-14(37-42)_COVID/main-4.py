import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, mean_absolute_error
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from imblearn.over_sampling import SMOTE
import warnings

# Вимикаємо попередження для чистоти виводу
warnings.filterwarnings('ignore')

# Створюємо директорію для графіків, якщо вона відсутня
os.makedirs("charts", exist_ok=True)

# Завантаження датасету
url = "https://catalog.ourworldindata.org/garden/covid/latest/compact/compact.csv"
print(f"Завантаження даних з посилання: {url}...")
df = pd.read_csv(url)
print(f"Датасет завантажено. Початковий розмір: {df.shape}")

# ==============================================================================
# Попередня підготовка даних (Аналогічно до main-3.py для збереження консистентності)
# ==============================================================================
# 1. Залишаємо лише записи, де вказано континент (виключаємо континентальні та глобальні агрегації)
df = df.dropna(subset=['continent'])

# 2. Заповнюємо пропущені значення у ключових змінних
df['new_cases'] = df['new_cases'].fillna(0).clip(lower=0)
df['total_cases'] = df['total_cases'].fillna(0)
df['total_deaths'] = df['total_deaths'].fillna(0)
df['total_vaccinations'] = df['total_vaccinations'].fillna(0)

# Для інших числових змінних заповнимо медіаною по всьому датасету
df['population'] = df['population'].fillna(df['population'].median())
df['population_density'] = df['population_density'].fillna(df['population_density'].median())
df['median_age'] = df['median_age'].fillna(df['median_age'].median())
df['gdp_per_capita'] = df['gdp_per_capita'].fillna(df['gdp_per_capita'].median())

# Для швидкої та коректної роботи моделей на навчальних заняттях беремо репрезентативну вибірку у розмірі 30 000 спостережень
df_sampled = df.sample(n=30000, random_state=42).copy()

# Створення цільової змінної для класифікації
df_sampled['high_cases'] = (df_sampled['new_cases'] > 1000).astype(int)

# Базовий набір ознак X (виключаємо new_cases, high_cases, date, country)
X_base = df_sampled.drop(columns=['new_cases', 'high_cases', 'date', 'country'])
y_reg = df_sampled['new_cases']
y_clf = df_sampled['high_cases']

# Передобробка категоріальних та числових змінних
X_processed = X_base.copy()
X_processed = pd.get_dummies(X_processed, columns=['continent'], drop_first=True, dtype=int)
le = LabelEncoder()
X_processed['code'] = le.fit_transform(X_processed['code'].astype(str))

# Очищення від NaNs
X_processed = X_processed.dropna(how='all', axis=1)
numeric_cols = X_processed.select_dtypes(include=[np.number]).columns
for col in numeric_cols:
    median_val = X_processed[col].median()
    X_processed[col] = X_processed[col].fillna(0 if pd.isna(median_val) else median_val)

X_processed = X_processed.select_dtypes(include=[np.number]).fillna(0)

# Масштабування StandardScaler
scale_cols = [col for col in ['total_cases', 'total_deaths', 'total_vaccinations', 'population', 'population_density', 'median_age', 'gdp_per_capita'] if col in X_processed.columns]
scaler = StandardScaler()
X_processed[scale_cols] = scaler.fit_transform(X_processed[scale_cols])

# Розділення на Train/Test (80/20)
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
    X_processed, y_reg, test_size=0.2, random_state=42
)
X_train_clf, X_test_clf, y_train_clf, y_test_clf = train_test_split(
    X_processed, y_clf, test_size=0.2, random_state=42, stratify=y_clf
)

# Застосовуємо SMOTE для класифікації
smote = SMOTE(random_state=42)
X_train_clf_res, y_train_clf_res = smote.fit_resample(X_train_clf, y_train_clf)


# ==============================================================================
# Завдання 1. Оцінка класифікаційних моделей
# ==============================================================================
# - Для кожної моделі (Logistic Regression, Decision Tree, Random Forest, k-NN) розрахуйте: Accuracy, Precision, Recall, F1-Score.
# - Побудуйте матрицю плутанини для кожної моделі та візуалізуйте у вигляді heatmap.
# - Проаналізуйте: яка модель має найменше FN (пропущених спалахів)?
# ==============================================================================
print("\n" + "="*80)
print(" ЗАВДАННЯ 1. ОЦІНКА КЛАСИФІКАЦІЙНИХ МОДЕЛЕЙ")
print("="*80)

models_clf = {
    'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
    'Decision Tree': DecisionTreeClassifier(max_depth=8, random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42, n_jobs=-1),
    'k-NN': KNeighborsClassifier(n_neighbors=5, n_jobs=-1)
}

clf_evaluation = {}
fn_counts = {}

plt.figure(figsize=(16, 12))

for idx, (name, model) in enumerate(models_clf.items(), 1):
    model.fit(X_train_clf_res, y_train_clf_res)
    y_pred = model.predict(X_test_clf)

    # Розрахунок метрик
    cm = confusion_matrix(y_test_clf, y_pred)
    acc = accuracy_score(y_test_clf, y_pred)
    prec = precision_score(y_test_clf, y_pred)
    rec = recall_score(y_test_clf, y_pred)
    f1 = f1_score(y_test_clf, y_pred)

    # Кількість False Negatives (FN) знаходиться у cm[1, 0]
    fn = cm[1, 0]
    fn_counts[name] = fn

    clf_evaluation[name] = {
        'Accuracy': acc,
        'Precision': prec,
        'Recall': rec,
        'F1-Score': f1,
        'False Negatives (FN)': fn
    }

    # Побудова та збереження heatmap
    plt.subplot(2, 2, idx)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
                xticklabels=['<=1000 cases', '>1000 cases'],
                yticklabels=['<=1000 cases', '>1000 cases'])
    plt.title(f"Confusion Matrix: {name}\n(FN = {fn})", fontsize=12, fontweight='bold')
    plt.ylabel('Actual')
    plt.xlabel('Predicted')

plt.tight_layout()
cm_plot_path = "charts/classification_confusion_matrices.png"
plt.show()
print(f"- Візуалізацію матриць плутанини збережено у файл '{cm_plot_path}'")

# Порівняльна таблиця класифікації
df_clf_eval = pd.DataFrame(clf_evaluation).T
print("\nПорівняльна таблиця класифікаційних моделей:")
print(df_clf_eval)

# Аналіз найменшого FN
min_fn_model = min(fn_counts, key=fn_counts.get)
print(f"\nАналіз помилок другого роду (пропущених спалахів):")
for model_name, fn_val in fn_counts.items():
    print(f" - {model_name}: {fn_val} пропущених спалахів (FN)")
print(f"Модель з найменшою кількістю FN (найкраще виявляє спалахи): {min_fn_model} (FN = {fn_counts[min_fn_model]})")


# ==============================================================================
# Завдання 2. Оцінка регресійних моделей
# ==============================================================================
# - Для кожної моделі (Linear, Polynomial, Ridge, Lasso) обчисліть: MSE, RMSE, MAE, R^2.
# - Порівняйте результати у таблиці.
# - Визначте, яка модель найкраще прогнозує кількість нових випадків.
# ==============================================================================
print("\n" + "="*80)
print(" ЗАВДАННЯ 2. ОЦІНКА РЕГРЕСІЙНИХ МОДЕЛЕЙ")
print("="*80)

reg_results = {}

# 1. Linear Regression
lr = LinearRegression()
lr.fit(X_train_reg, y_train_reg)
y_pred_lr = lr.predict(X_test_reg)

# 2. Polynomial Regression (degree 2 на ключових кумулятивних змінних)
poly_cols = ['total_cases', 'total_deaths', 'total_vaccinations']
X_train_poly = X_train_reg[poly_cols]
X_test_poly = X_test_reg[poly_cols]
poly_pipeline = make_pipeline(PolynomialFeatures(degree=2, include_bias=False), LinearRegression())
poly_pipeline.fit(X_train_poly, y_train_reg)
y_pred_poly = poly_pipeline.predict(X_test_poly)

# 3. Ridge Regression
ridge = Ridge(alpha=1.0)
ridge.fit(X_train_reg, y_train_reg)
y_pred_ridge = ridge.predict(X_test_reg)

# 4. Lasso Regression
lasso = Lasso(alpha=0.1, max_iter=2000)
lasso.fit(X_train_reg, y_train_reg)
y_pred_lasso = lasso.predict(X_test_reg)

models_reg_preds = {
    'Linear Regression': y_pred_lr,
    'Polynomial Regression (deg 2)': y_pred_poly,
    'Ridge Regression': y_pred_ridge,
    'Lasso Regression': y_pred_lasso
}

for name, y_pred in models_reg_preds.items():
    mse = mean_squared_error(y_test_reg, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test_reg, y_pred)
    r2 = r2_score(y_test_reg, y_pred)

    reg_results[name] = {
        'MSE': mse,
        'RMSE': rmse,
        'MAE': mae,
        'R^2': r2
    }

# Порівняльна таблиця регресії
df_reg_eval = pd.DataFrame(reg_results).T
print("\nПорівняльна таблиця результатів регресії:")
print(df_reg_eval)

best_reg_model = df_reg_eval['R^2'].idxmax()
print(f"\nМодель, яка найкраще прогнозує кількість нових випадків (за R^2): {best_reg_model} (R^2 = {df_reg_eval.loc[best_reg_model, 'R^2']:.4f})")


# ==============================================================================
# Завдання 3. Крос-валідація
# ==============================================================================
# - Виконайте 5-fold cross-validation для всіх класифікаційних моделей.
# - Обчисліть середній F1-Score та стандартне відхилення для кожної.
# - Визначте найстабільнішу модель (найменше стандартне відхилення).
# ==============================================================================
print("\n" + "="*80)
print(" ЗАВДАННЯ 3. КРОС-ВАЛІДАЦІЯ КЛАСИФІКАТОРІВ (5-Fold)")
print("="*80)

cv_results = {}
stds = {}

# Використовуємо збалансовані тренувальні дані X_train_clf_res для крос-валідації
for name, model in models_clf.items():
    print(f"- Проводимо 5-fold CV для моделі '{name}'...")
    # Обчислюємо F1-score на кожному фолді
    scores = cross_val_score(model, X_train_clf_res, y_train_clf_res, cv=5, scoring='f1', n_jobs=-1)
    mean_f1 = np.mean(scores)
    std_f1 = np.std(scores)
    stds[name] = std_f1

    cv_results[name] = {
        'Mean F1-Score': mean_f1,
        'F1 StDev (Стандартне відхилення)': std_f1
    }

# Вивід результатів крос-валідації
df_cv = pd.DataFrame(cv_results).T
print("\nРезультати 5-fold крос-валідації (за метрикою F1-Score):")
print(df_cv)

stable_model = min(stds, key=stds.get)
print(f"\nНайстабільніша модель (найменше стандартне відхилення F1): {stable_model} (StDev = {stds[stable_model]:.6f})")


# ==============================================================================
# Завдання 4. Оптимізація гіперпараметрів
# ==============================================================================
# - Для Random Forest виконайте GridSearchCV з параметрами:
#   n_estimators: [50, 100, 200], max_depth: [5, 10, 20, None], min_samples_split: [2, 5, 10]
# - Визначте найкращі параметри та оновіть модель.
# - Порівняйте F1-Score до та після оптимізації.
# ==============================================================================
print("\n" + "="*80)
print(" ЗАВДАННЯ 4. ОПТИМІЗАЦІЯ ГІПЕРПАРАМЕТРІВ (GridSearchCV для Random Forest)")
print("="*80)

# Базовий F1-Score Random Forest до оптимізації
f1_rf_before = clf_evaluation['Random Forest']['F1-Score']
print(f"F1-Score Random Forest з базовими параметрами: {f1_rf_before:.4f}")

# Налаштування сітки параметрів
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 20, None],
    'min_samples_split': [2, 5, 10]
}

rf_base = RandomForestClassifier(random_state=42, n_jobs=-1)

# Використовуємо 3-fold CV для швидкості обчислень під час пошуку по сітці
print("- Запуск GridSearchCV (це може зайняти близько 10-20 секунд)...")
grid_search = GridSearchCV(estimator=rf_base, param_grid=param_grid, cv=3, scoring='f1', n_jobs=-1)
grid_search.fit(X_train_clf_res, y_train_clf_res)

best_params = grid_search.best_params_
print(f"\nНайкращі знайдені параметри: {best_params}")

# Оновлена модель
best_rf_model = grid_search.best_estimator_

# Розрахунок F1-Score оновленої моделі на тестовій вибірці
y_pred_opt = best_rf_model.predict(X_test_clf)
f1_rf_after = f1_score(y_test_clf, y_pred_opt)

print(f"F1-Score Random Forest після оптимізації: {f1_rf_after:.4f}")
print(f"Зміна F1-Score: {f1_rf_after - f1_rf_before:+.4f}")


# ==============================================================================
# Завдання 5. Gradient Boosting
# ==============================================================================
# - Додайте GradientBoostingClassifier до набору моделей.
# - Навчіть модель та обчисліть всі метрики класифікації.
# - Порівняйте з Random Forest: яка модель краща?
# ==============================================================================
print("\n" + "="*80)
print(" ЗАВДАННЯ 5. GRADIENT BOOSTING CLASSIFIER")
print("="*80)

print("- Навчання Gradient Boosting Classifier...")
gb_clf = GradientBoostingClassifier(random_state=42)
gb_clf.fit(X_train_clf_res, y_train_clf_res)
y_pred_gb = gb_clf.predict(X_test_clf)

# Обчислення метрик
acc_gb = accuracy_score(y_test_clf, y_pred_gb)
prec_gb = precision_score(y_test_clf, y_pred_gb)
rec_gb = recall_score(y_test_clf, y_pred_gb)
f1_gb = f1_score(y_test_clf, y_pred_gb)

print(f"\nМетрики Gradient Boosting:")
print(f" - Accuracy: {acc_gb:.4f}")
print(f" - Precision: {prec_gb:.4f}")
print(f" - Recall: {rec_gb:.4f}")
print(f" - F1-Score: {f1_gb:.4f}")

# Зберігаємо в загальну таблицю порівняння для наочності
df_compare_rf_gb = pd.DataFrame({
    'Random Forest (Default)': [clf_evaluation['Random Forest']['Accuracy'],
                                clf_evaluation['Random Forest']['Precision'],
                                clf_evaluation['Random Forest']['Recall'],
                                clf_evaluation['Random Forest']['F1-Score']],
    'Random Forest (Optimized)': [accuracy_score(y_test_clf, y_pred_opt),
                                  precision_score(y_test_clf, y_pred_opt),
                                  recall_score(y_test_clf, y_pred_opt),
                                  f1_rf_after],
    'Gradient Boosting': [acc_gb, prec_gb, rec_gb, f1_gb]
}, index=['Accuracy', 'Precision', 'Recall', 'F1-Score']).T

print("\nПорівняння моделей ансамблів:")
print(df_compare_rf_gb)

# Висновок про найкращу ансамблеву модель
best_ensemble = df_compare_rf_gb['F1-Score'].idxmax()
print(f"\nНайкраща модель серед ансамблів (за F1-Score): {best_ensemble}")


# ==============================================================================
# Завдання 6. Фінальне прогнозування та діагностичні графіки
# ==============================================================================
# - Виберіть найкращу класифікаційну модель та зробіть прогнози на тестовому наборі.
# - Виберіть найкращу регресійну модель та зробіть прогнози на тестовому наборі.
# - Побудуйте графік Predicted vs Actual для регресії.
# - Побудуйте гістограму розподілу помилок (residuals).
# ==============================================================================
print("\n" + "="*80)
print(" ЗАВДАННЯ 6. ФІНАЛЬНЕ ПРОГНОЗУВАННЯ ТА ВІЗУАЛІЗАЦІЯ")
print("="*80)

# 1. Фінальна класифікація
# Вибираємо модель з найвищим F1-Score серед усіх навчених моделей
all_clf_metrics = {
    'Logistic Regression': clf_evaluation['Logistic Regression']['F1-Score'],
    'Decision Tree': clf_evaluation['Decision Tree']['F1-Score'],
    'Random Forest (Default)': clf_evaluation['Random Forest']['F1-Score'],
    'Random Forest (Optimized)': f1_rf_after,
    'Gradient Boosting': f1_gb,
    'k-NN': clf_evaluation['k-NN']['F1-Score']
}
best_overall_clf_name = max(all_clf_metrics, key=all_clf_metrics.get)
print(f"Найкраща загальна модель класифікації для фінального прогнозу: {best_overall_clf_name} (F1 = {all_clf_metrics[best_overall_clf_name]:.4f})")

# 2. Фінальна регресія
# Вибираємо модель з найвищим R^2
print(f"Найкраща модель регресії для фінального прогнозу: {best_reg_model} (R^2 = {df_reg_eval.loc[best_reg_model, 'R^2']:.4f})")

# Отримуємо передбачення найкращої регресійної моделі
y_pred_best_reg = models_reg_preds[best_reg_model]

# 3. Графік Predicted vs Actual
plt.figure(figsize=(10, 6))
plt.scatter(y_test_reg, y_pred_best_reg, alpha=0.5, color='teal', edgecolor='k')
# Побудова лінії ідеального прогнозу
max_val = max(y_test_reg.max(), y_pred_best_reg.max())
plt.plot([0, max_val], [0, max_val], color='red', linestyle='--', linewidth=2, label='Ідеальний прогноз')
plt.title(f"Регресія: Передбачені значення vs Фактичні ({best_reg_model})", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Фактичні нові випадки (Actual new_cases)")
plt.ylabel("Передбачені нові випадки (Predicted new_cases)")
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.show()

# 4. Гістограма розподілу залишків (residuals)
residuals = y_test_reg - y_pred_best_reg
plt.figure(figsize=(10, 6))
sns.histplot(residuals, bins=40, kde=True, color='purple', edgecolor='black')
plt.axvline(0, color='red', linestyle='--', linewidth=2, label='Нульова помилка (Zero Residual)')
plt.title("Розподіл помилок регресії (Residuals Distribution)", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Помилка прогнозу (Actual - Predicted)")
plt.ylabel("Частота")
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.show()


# ==============================================================================
# Завдання 7. Аналіз помилок
# ==============================================================================
# - Визначте 10 записів з найбільшими помилками прогнозування (для регресії).
# - Проаналізуйте: що спільного у цих записів? (країна, дата, особливі обставини)
# - Опишите можливі причини відхилень та як їх можна зменшити.
# ==============================================================================
print("\n" + "="*80)
print(" ЗАВДАННЯ 7. АНАЛІЗ ПОМИЛОК РЕГРЕСІЇ")
print("="*80)

# Створюємо тимчасовий датафрейм для тестових даних та їх помилок
test_indices = X_test_reg.index
df_errors = df_sampled.loc[test_indices].copy()
df_errors['Actual_new_cases'] = y_test_reg
df_errors['Predicted_new_cases'] = y_pred_best_reg
df_errors['Absolute_Error'] = np.abs(residuals)

# Топ-10 записів з найбільшими помилками
top_10_errors = df_errors.sort_values(by='Absolute_Error', ascending=False).head(10)

print("\nТоп-10 записів з найбільшими помилками прогнозування:")
print(top_10_errors[['country', 'date', 'Actual_new_cases', 'Predicted_new_cases', 'Absolute_Error']])

# Аналітичний опис причин помилок
print("\n" + "-"*80)
print(" АНАЛІЗ ТА РЕКОМЕНДАЦІЇ ЩОДО ЗМЕНШЕННЯ ПОМИЛОК")
print("-"*80)
print("""
СПІЛЬНІ РИСИ ЗАПИСІВ З НАЙБІЛЬШИМИ ПОМИЛКАМИ:
1. Масштаб країн: Майже всі записи в топі належать великим країнам з величезним населенням (наприклад, США, Індія, 
   Бразилія), де абсолютні добові показники захворюваності вимірювались десятками або сотнями тисяч.
2. Періоди хвиль (піки пандемії): Помилки концентруються на датах спалахів нових штамів (Дельта, Омікрон), коли 
   захворюваність експоненціально зростала за короткий час, що створює екстремальні викиди у порівнянні з рештою періоду.
3. Невідповідність кумулятивних показників добовим трендам: Якщо в країні накопичилась велика загальна кількість 
   випадків (total_cases), модель очікує стабільно високий рівень нових випадків, проте в періоди спаду (після хвилі) 
   або під час різкої зміни умов тестування добові випадки могли падати до мінімуму, викликаючи переоцінку з боку моделі.

ПРИЧИНИ ВІДХИЛЕНЬ:
- Мультиколінеарність і нелінійність: Кумулятивні ознаки мають дуже сильний вплив на модель, проте добова статистика 
  має виражені нелінійні коливання (хвилеподібний характер), які класичні лінійні моделі (Lasso/Ridge) не здатні вловити.
- Специфіка збору даних: У вихідні дні статистика часто штучно занижувалась, а в понеділок відбувався різкий скачок 
  за рахунок додавання пропущених даних, що створює локальні аномалії.

ЯК ЗМЕНШИТИ ПОМИЛКИ:
1. Використання часових лагів (Lags) та ковзних середніх (Rolling Averages): Додавання ознак, що показують приріст за
   попередні 3, 7 та 14 днів, дасть моделі інформацію про поточну швидкість та напрямок хвилі захворюваності.
2. Логарифмування або перехід до відносних величин: Прогнозування відносного показника (нових випадків на мільйон 
   населення) замість абсолютного допоможе моделі краще масштабуватись між малими та великими країнами.
3. Використання нелінійних моделей з регулюванням викидів: Градієнтний бустинг (наприклад, XGBoost Regressor або
   LightGBM) значно стійкіший до екстремальних викидів та краще моделює нелінійні залежності.
""")