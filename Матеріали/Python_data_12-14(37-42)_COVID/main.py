# 1. Захворюваність та смертність
# total_cases - Загальна кількість випадків COVID-19
# new_cases - Нові випадки за день
# new_cases_smoothed - Згладжене середнє за 7 днів (прибирає "шум" вихідних)
# total_deaths - Загальна кількість смертей
# new_deaths - Нові смерті за день
# 2. Показники на населення
# total_cases_per_million - Випадки на мільйон населення
# total_deaths_per_million - Смерті на мільйон населення
# new_cases_per_million - Нові випадки на мільйон за день
# 3. Медична система
# reproduction_rate - Скільки людей в середньому заражає один хворий
# icu_patients - Пацієнти у реанімації
# hosp_patients - Пацієнти в лікарнях
# hospital_beds_per_thousand - Лікарняні ліжка на 1000 населення
# 4. Тестування
# total_tests - Загальна кількість тестів
# positive_rate - Відсоток позитивних тестів
# tests_per_case - Скільки тестів на один виявлений випадок
# 5. Вакцинація
# total_vaccinations - Загальна кількість введених доз
# people_vaccinated - Люди з хоча б однією дозою
# people_fully_vaccinated - Повністю вакциновані
# total_boosters - Бустерні дози
# 6. Ідентифікатори
# iso_code - Код країни (UKR, USA, DEU...)
# continent - Континент
# location - Назва країни
# date - Дата запису


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_selection import SelectKBest, f_classif
from imblearn.over_sampling import SMOTE


# df = pd.read_csv(ur"https://catalog.ourworldindata.org/garden/covid/latest/compact/compact.csv")
# df = pd.read_csv("COVID.csv")

# cols_list = list(df.columns)
# cols_list = df.columns.to_list()
# for column in cols_list:
#     print(column)

# print(df.info())


# print(f"\n{cols_list}\n")


# new_df = df.drop("human_development_index", axis=1)
# print(new_df.info())
# print(new_df.isna().sum())
# print(new_df.isnull().sum().sort_values(ascending=False).describe())
# numeric_fill_cols = [
#     'total_cases', 'new_cases', 'new_cases_smoothed',
#     'total_cases_per_million', 'new_cases_per_million', 'new_cases_smoothed_per_million',
#     'total_deaths', 'new_deaths', 'new_deaths_smoothed',
#     'total_deaths_per_million', 'new_deaths_per_million', 'new_deaths_smoothed_per_million'
# ]
# new_df[numeric_fill_cols] = new_df[numeric_fill_cols].fillna(0)
# print(new_df.isnull().sum().sort_values(ascending=False))

# new_df["date"] = pd.to_datetime(new_df["date"])
# # new_df.info()
# new_df["code"] = new_df["code"].astype("category")
# new_df["continent"] = new_df["continent"].astype("category")
# new_df.info()
# new_new_columns = [
#     'total_cases', 'new_cases',
#     'total_deaths', 'new_deaths'
# ]


# print(new_df[new_new_columns].describe())

# df_ukr = new_df[new_df['country'] == "Ukraine"]
# print(df_ukr)

# print(new_df.duplicated().sum())
# new_df.drop_duplicates()

# new_df.to_csv("new_df.csv", index=False)
# df_ukr.to_csv("df_ukr.csv", index=False)

# new_df = pd.read_csv("new_df.csv")
# df_ukr = pd.read_csv("df_ukr.csv")
# print(new_df.head())

# fig, ax1 = plt.subplots(figsize=(12, 6))

# color = 'tab:blue'
# ax1.set_xlabel('Дата', fontsize=12, labelpad=10)
# ax1.set_ylabel('Загальна кількість випадків (total_cases)', color=color, fontsize=12)
# ax1.plot(df_ukr['date'], df_ukr['total_cases'], color=color, linewidth=2, label='Випадки')
# ax1.tick_params(axis='y', labelcolor=color)
# ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:,.0f}'))

# ax2 = ax1.twinx()
# color = 'tab:red'
# ax2.set_ylabel('Загальна кількість смертей (total_deaths)', color=color, fontsize=12)
# ax2.plot(df_ukr['date'], df_ukr['total_deaths'], color=color, linewidth=2, linestyle='--', label='Смерті')
# ax2.tick_params(axis='y', labelcolor=color)
# ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:,.0f}'))

# plt.title('Динаміка випадків захворювання та смертей від COVID-19 в Україні', fontsize=14, fontweight='bold', pad=15)
# fig.tight_layout()
# plt.show()


# latest_date = new_df['date'].max()
# countries_latest = new_df[(new_df['date'] == latest_date) & (new_df['continent'].notna())]
# continent_data = countries_latest.groupby('continent')['total_cases'].sum().reset_index()
# continent_data = continent_data.sort_values(by='total_cases', ascending=False)

# plt.figure(figsize=(10, 6))
# barplot = sns.barplot(
#     data=continent_data,
#     x='continent',
#     y='total_cases',
#     hue='continent',
#     legend=False,
#     palette='viridis'
# )

# plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1e6:.1f} млн'))
# plt.xlabel('Континент', fontsize=12)
# plt.ylabel('Загальна кількість випадків (млн)', fontsize=12)
# plt.title(f'Порівняння загальної кількості випадків COVID-19 за континентами на {latest_date}', fontsize=14, fontweight='bold', pad=15)

# for p in barplot.patches:
#     val = p.get_height()
#     if val > 0:
#         barplot.annotate(f'{val/1e6:.1f}M',
#                         (p.get_x() + p.get_width() / 2., val),
#                         ha='center', va='center',
#                         xytext=(0, 8),
#                         textcoords='offset points',
#                         fontsize=10, fontweight='bold')

# plt.tight_layout()
# plt.show()

# new_df = new_df.sort_values(by=['country', 'date'])
# new_df['growth_rate_new_cases'] = new_df.groupby('country')['new_cases'].pct_change().fillna(0).replace([np.inf, -np.inf], 0)
# new_df['growth_rate_new_deaths'] = new_df.groupby('country')['new_deaths'].pct_change().fillna(0).replace([np.inf, -np.inf], 0)

# corr_cols = ['new_cases', 'new_deaths', 'total_cases', 'population', 'gdp_per_capita']
# new_df['population'] = new_df['population'].fillna(0)
# new_df['gdp_per_capita'] = new_df['gdp_per_capita'].fillna(0)

# new_df1 = new_df[corr_cols]

# corr_matrix = new_df1.corr()
# print(corr_matrix)

# plt.figure(figsize=(10, 8))
# sns.heatmap(corr_matrix, annot=True, cmap='viridis')
# plt.show()

# df_latest_countries = new_df[(new_df['date'] == latest_date) & (new_df['continent'].notna())].copy()

# fig, axes = plt.subplots(1, 2, figsize=(14, 5))
# sns.histplot(df_latest_countries['total_cases'], bins=20, ax=axes[0], color='skyblue', kde=True)
# axes[0].set_title("Розподіл загальної кількості випадків (total_cases)", fontsize=11, fontweight='bold')
# axes[0].set_xlabel("Загальна кількість випадків (в сотнях млн)")
# axes[0].set_ylabel("Кількість країн")

# sns.histplot(df_latest_countries['total_deaths'], bins=20, ax=axes[1], color='salmon', kde=True)
# axes[1].set_title("Розподіл загальної кількості смертей (total_deaths)", fontsize=11, fontweight='bold')
# axes[1].set_xlabel("Загальна кількість смертей (в млн)")
# axes[1].set_ylabel("Кількість країн")
# plt.tight_layout()
# plt.show()

# plt.figure(figsize=(10, 6))
# df_latest_countries['total_deaths_per_million'] = df_latest_countries['total_deaths_per_million'].fillna(0)
# sns.boxplot(data=df_latest_countries, x='continent', y='total_deaths_per_million', hue='continent', legend=False, palette='Set3')
# plt.title("Порівняння відносної смертності (на мільйон) за континентами", fontsize=14, fontweight='bold', pad=15)
# plt.xlabel("Континент")
# plt.ylabel("Смертей на 1 мільйон населення")
# plt.tight_layout()
# plt.show()

# pairplot_cols = ['total_cases', 'total_deaths', 'total_vaccinations', 'population', 'continent']
# df_latest_countries['total_vaccinations'] = df_latest_countries['total_vaccinations'].fillna(0)
# sns.pairplot(df_latest_countries[pairplot_cols], hue='continent', palette='bright')
# plt.suptitle("Взаємозв'язки між ключовими показниками COVID-19", y=1.02, fontsize=14, fontweight='bold')
# plt.show()






# Завдання 1. Визначення задачі та підготовка даних
#     Виберіть цільову змінну: new_cases для регресії  #LinearRegression
#     АБО створіть high_cases (поріг 1000) для класифікації. # LogisticRegression
#     Розділіть датасет на ознаки (X) та цільову змінну (y).
#     Для регресії виключіть: new_cases, date, location.
#     Для класифікації виключіть: high_cases, new_cases, date, location.

# Завдання 2. Обробка категоріальних та числових змінних
#     Перетворіть continent у набір бінарних змінних за допомогою One-Hot Encoding.
#     Перетворіть iso_code у числовий формат за допомогою LabelEncoder.
#     Масштабуйте числові змінні (total_cases, total_deaths, total_vaccinations) за допомогою StandardScaler.

# Завдання 3. Розділення та балансування даних
#     Розділіть дані на train (80%) та test (20%) за допомогою train_test_split.
#     Для класифікації: якщо є дисбаланс класів, застосуйте SMOTE до тренувального набору.

# Завдання 4. Моделі регресії
    # Навчіть моделі: Linear Regression, Polynomial Regression (ступінь 2), Ridge Regression, Lasso Regression.
    # Для кожної моделі обчисліть MSE та R² на тестовому наборі.
    # Порівняйте результати та визначте найкращу модель.

# Завдання 5. Моделі класифікації
    # Навчіть моделі: Logistic Regression, Decision Tree, Random Forest, k-NN.
    # Для кожної моделі побудуйте матрицю плутанини та обчисліть Accuracy, Precision, Recall, F1.
    # Порівняйте результати та визначте найкращу модель.

# Завдання 6. Відбір ознак
    # Використайте SelectKBest для визначення топ-10 найважливіших ознак.
    # Перенавчіть найкращу модель класифікації тільки на цих 10 ознаках.
    # Порівняйте результати: чи покращилась продуктивність?

# Завдання 7. Аналітичний звіт для презентації
#     Напишіть звіт (400-500 слів), де опишете:
#     Процес підготовки даних (кодування, масштабування, балансування)
#     Які моделі ви навчили та їх результати
#     Яка модель виявилась найкращою і чому
#     Рекомендації для подальшого вдосконалення


new_df = pd.read_csv("new_df.csv")
df_ukr = pd.read_csv("df_ukr.csv")

y_reg = new_df['new_cases']
y_reg_ukr = df_ukr['new_cases']

# high_cases
y_class =  (new_df['new_cases'] > 1000).astype(int)
y_class_ukr = (df_ukr['new_cases'] > 1000).astype(int)


# print(new_df.columns.to_list())
# for col in new_df.columns.to_list():
#     print(col)

# new_cases, date, location
X = new_df.drop(columns=['new_cases', 'date', 'country'])
X_ukr = df_ukr.drop(columns=['new_cases', 'date', 'country'])

# for col in X_ukr.columns.to_list():
#     print(col)

# print(X_ukr['continent'].head())
# Перетворіть continent у набір бінарних змінних за допомогою One-Hot Encoding. Щоб дзвінок другу не робили))))

X = pd.get_dummies(X, columns=['continent'], drop_first=True, dtype=int)
X_ukr = pd.get_dummies(X_ukr, columns=['continent'], drop_first=True, dtype=int)

Encoder = LabelEncoder()

X['code'] = Encoder.fit_transform(X['code'].astype(str))
X_ukr['code'] = Encoder.fit_transform(X_ukr['code'].astype(str))

#Масштабуйте числові змінні (total_cases, total_deaths, total_vaccinations) за допомогою StandardScaler.

Scaler = StandardScaler()
num_cols = ['total_cases', 'total_deaths', 'total_vaccinations']
X[num_cols] = Scaler.fit_transform(X[num_cols])
X_ukr[num_cols] = Scaler.fit_transform(X_ukr[num_cols])

X = X.fillna(0)
X_ukr = X_ukr.fillna(0)

# print(X.head())# Зомбі апокаліпсіс
#  _==_==-
#   / (

X_reg_train, X_reg_test, y_reg_train, y_reg_test = train_test_split(X, y_reg, random_state=30, test_size=0.2)
X_ukr_reg_train, X_ukr_reg_test, y_reg_ukr_train, y_reg_ukr_test = train_test_split(X_ukr, y_reg_ukr, random_state=30, test_size=0.2)

X_cls_train, X_cls_test, y_class_train, y_class_test = train_test_split(X, y_class, random_state=30, test_size=0.2, stratify=y_class)
X_ukr_cls_train, X_ukr_cls_test, y_class_ukr_train, y_class_ukr_test = train_test_split(X_ukr, y_class_ukr, random_state=30, test_size=0.2, stratify=y_class_ukr)

smote = SMOTE(random_state=30)
X_cls_train, y_class_train = smote.fit_resample(X_cls_train, y_class_train)
X_ukr_cls_train, y_class_ukr_train = smote.fit_resample(X_ukr_cls_train, y_class_ukr_train)

# Навчіть моделі: Linear Regression, Polynomial Regression (ступінь 2), Ridge Regression, Lasso Regression.
# Для кожної моделі обчисліть MSE та R² на тестовому наборі.
# Порівняйте результати та визначте найкращу модель.

# model = LinearRegression()
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# print(f"{mean_squared_error(y_test, y_pred) = }")
# print(f"{mean_absolute_error(y_test, y_pred) = }")
# print(f"{r2_score(y_test, y_pred) = }")

# -------------------------------------------------------------------------------
# model = LinearRegression()
# model.fit(X_reg_train, y_reg_train)
# y_reg_pred = model.predict(X_reg_test)
# print(f"{mean_squared_error(y_reg_test, y_reg_pred) = }")
# print(f"{mean_absolute_error(y_reg_test, y_reg_pred) = }")
# print(f"{r2_score(y_reg_test, y_reg_pred) = }")

# mean_squared_error(y_reg_test, y_reg_pred) = 3516663796.6846657
# mean_absolute_error(y_reg_test, y_reg_pred) = 5354.592394070887
# r2_score(y_reg_test, y_reg_pred) = 0.7073605573420043
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
# model = LinearRegression()
# model.fit(X_ukr_reg_train, y_reg_ukr_train)
# y_ukr_reg_pred = model.predict(X_ukr_reg_test)
# print(f"{mean_squared_error(y_reg_ukr_test, y_ukr_reg_pred) = }")
# print(f"{mean_absolute_error(y_reg_ukr_test, y_ukr_reg_pred) = }")
# print(f"{r2_score(y_reg_ukr_test, y_ukr_reg_pred) = }")

# mean_squared_error(y_reg_ukr_test, y_ukr_reg_pred) = 0.018635517828188716
# mean_absolute_error(y_reg_ukr_test, y_ukr_reg_pred) = 0.07825825160304052
# r2_score(y_reg_ukr_test, y_ukr_reg_pred) = 0.9999999998488641
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
# numeric_col = ['total_cases', 'total_deaths', 'total_vaccinations']

# pipeline = make_pipeline(PolynomialFeatures(degree=2, include_bias=False), LinearRegression())
# pipeline.fit(X_reg_train[numeric_col], y_reg_train)
# y_reg_pred = pipeline.predict(X_reg_test[numeric_col])
# print(f"{r2_score(y_reg_test, y_reg_pred) = }")

# # r2_score(y_reg_test, y_reg_pred) = 0.24833794312686297

# pipeline = make_pipeline(PolynomialFeatures(degree=2, include_bias=False), LinearRegression())
# pipeline.fit(X_ukr_reg_train[numeric_col], y_reg_ukr_train)
# y_ukr_reg_pred = pipeline.predict(X_ukr_reg_test[numeric_col])
# print(f"{r2_score(y_reg_ukr_test, y_ukr_reg_pred) = }")

# r2_score(y_reg_ukr_test, y_ukr_reg_pred) = 0.05608509816539309
# -------------------------------------------------------------------------------

# numeric_col = ['total_cases', 'total_deaths', 'total_vaccinations']

# -------------------------------------------------------------------------------
# Ridge Regression
# model = Ridge()
# model.fit(X_reg_train, y_reg_train)
# y_reg_pred = model.predict(X_reg_test)
# # print(f"{mean_squared_error(y_reg_test, y_reg_pred) = }")
# # print(f"{mean_absolute_error(y_reg_test, y_reg_pred) = }")
# print(f"Ridge-{r2_score(y_reg_test, y_reg_pred) = }")
# # Ridge-r2_score(y_reg_test, y_reg_pred) = 0.7538915821568716

# model = Ridge()
# model.fit(X_reg_train[numeric_col], y_reg_train)
# y_reg_pred = model.predict(X_reg_test[numeric_col])
# print(f"Ridge-num-{r2_score(y_reg_test, y_reg_pred) = }")
# Ridge-num-r2_score(y_reg_test, y_reg_pred) = 0.18959055331673114

# model = Ridge()
# model.fit(X_ukr_reg_train, y_reg_ukr_train)
# y_ukr_reg_pred = model.predict(X_ukr_reg_test)
# # print(f"{mean_squared_error(y_reg_ukr_test, y_ukr_reg_pred) = }")
# # print(f"{mean_absolute_error(y_reg_ukr_test, y_ukr_reg_pred) = }")
# print(f"Ridge-ukr-{r2_score(y_reg_ukr_test, y_ukr_reg_pred) = }")
# # Ridge-ukr-r2_score(y_reg_ukr_test, y_ukr_reg_pred) = 0.9999999999999993

# Lasso Regression
model = Lasso()
model.fit(X_reg_train, y_reg_train)
y_reg_pred = model.predict(X_reg_test)
# print(f"{mean_squared_error(y_reg_test, y_reg_pred) = }")
# print(f"{mean_absolute_error(y_reg_test, y_reg_pred) = }")
print(f"Lasso-{r2_score(y_reg_test, y_reg_pred) = }")
# Lasso-r2_score(y_reg_test, y_reg_pred) = 0.753889298956713

# model = Lasso()
# model.fit(X_reg_train[numeric_col], y_reg_train)
# y_reg_pred = model.predict(X_reg_test[numeric_col])
# print(f"Lasso-num-{r2_score(y_reg_test, y_reg_pred) = }")
# # Lasso-num-r2_score(y_reg_test, y_reg_pred) = 0.18959102006047746

# model = Lasso()
# model.fit(X_ukr_reg_train, y_reg_ukr_train)
# y_ukr_reg_pred = model.predict(X_ukr_reg_test)
# # print(f"{mean_squared_error(y_reg_test, y_reg_pred) = }")
# # print(f"{mean_absolute_error(y_reg_test, y_reg_pred) = }")
# print(f"Lasso-ukr-{r2_score(y_ukr_reg_pred, y_reg_ukr_test) = }")
# # Lasso-ukr-r2_score(y_ukr_reg_pred, y_reg_ukr_test) = 0.9999999943564026
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# Завдання 5. Моделі класифікації
    # Навчіть моделі: Logistic Regression, Decision Tree, Random Forest, k-NN.
    # Для кожної моделі побудуйте матрицю плутанини та обчисліть Accuracy, Precision, Recall, F1.
    # Порівняйте результати та визначте найкращу модель.

# Logistic Regression
# model = LogisticRegression()
# model.fit(X_cls_train, y_class_train)
# y_class_pred = model.predict(X_cls_test)
# print(f"Logistic Regression-{accuracy_score(y_class_test, y_class_pred) = }") # 0.73
# print(f"Logistic Regression-{precision_score(y_class_test, y_class_pred) = }") #  0.25
# print(f"Logistic Regression-{recall_score(y_class_test, y_class_pred) = }") # 0.75
# print(f"Logistic Regression-{f1_score(y_class_test, y_class_pred) = }") # 0.38

# Decision Tree
# model = DecisionTreeClassifier()
# model.fit(X_cls_train, y_class_train)
# y_cls_pred = model.predict(X_cls_test)
# print(f"DesicionTree-{accuracy_score(y_cls_pred, y_class_test) = }") # 0.995
# print(f"DesicionTree-{precision_score(y_cls_pred, y_class_test) = }") # 0.987
# print(f"DesicionTree-{recall_score(y_cls_pred, y_class_test) = }") # 0.976
# print(f"DesicionTree-{f1_score(y_cls_pred, y_class_test) = }") # 0.981

# Random Forest
# model = RandomForestClassifier(random_state=30)
# model.fit(X_cls_train, y_class_train)
# y_class_pred = model.predict(X_cls_test)
# print(f"RandomForest-{accuracy_score(y_class_pred, y_class_test) = }") #
# print(f"RandomForest-{precision_score(y_class_pred, y_class_test) = }") #
# print(f"RandomForest-{recall_score(y_class_pred, y_class_test) = }") #
# print(f"RandomForest-{f1_score(y_class_pred, y_class_test) = }") #

# k-NN
# model = KNeighborsClassifier()
# model.fit(X_cls_train, y_class_train)
# y_class_pred = model.predict(X_cls_test)
# print(f"k-NN-{accuracy_score(y_class_pred, y_class_test) = }") # 0.96
# print(f"k-NN-{precision_score(y_class_pred, y_class_test) = }") # .93
# print(f"k-NN-{recall_score(y_class_pred, y_class_test) = }") # 0.80
# print(f"k-NN-{f1_score(y_class_pred, y_class_test) = }") # 0.86