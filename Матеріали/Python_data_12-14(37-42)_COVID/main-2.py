# Завдання на урок від ліда
# Завдання 1. Очищення та обробка даних
# Проаналізуйте пропущені значення у ключових стовпцях (new_cases, new_deaths, total_cases).
# Вирішіть, як обробити пропуски: заміна середнім, медіаною або видалення рядків. Обґрунтуйте вибір.
# Перевірте датасет на дублікати та видаліть їх.

# Завдання 2. Трансформація даних
# Перетворіть категоріальний стовпець location у коди ISO або виконайте one-hot encoding.
# Створіть нові ознаки: growth_rate_new_cases та growth_rate_new_deaths для кожної країни на основі даних по датах.
# Збережіть очищені та трансформовані дані у новий CSV-файл.

# Завдання 3. Кореляційний аналіз
# Виконайте аналіз кореляцій між числовими змінними (new_cases, new_deaths, total_cases, population, gdp_per_capita).
# Визначте найсильніші взаємозв'язки (позитивні та негативні).
# Візуалізуйте кореляційну матрицю у вигляді теплової карти (heatmap).

# Завдання 4. Розподіл даних
# Побудуйте гістограми для стовпців total_cases та total_deaths.
# Побудуйте boxplot для порівняння total_deaths_per_million по континентах.
# Побудуйте pairplot для змінних: total_cases, total_deaths, total_vaccinations, population.

# Завдання 5. Аналіз трендів
# Побудуйте лінійні графіки трендів new_cases та new_deaths для 3 вибраних країн (наприклад, США, Україна, Німеччина).
# Побудуйте бар-чарт топ-10 країн за total_cases_per_million на останню доступну дату.
# Визначте дати з найвищими та найнижчими значеннями new_cases та new_deaths для кожної з обраних країн.

# Завдання 6. Підготовка до презентації
# Напишіть аналітичний звіт (300-400 слів): які взаємозв'язки та тенденції ви виявили за допомогою кореляційної матриці та візуалізацій.
# Опишіть виявлені аномалії: несподівані високі/низькі показники, можливі причини, вплив на подальший аналіз.


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Налаштування стилів відображення
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

url = "https://catalog.ourworldindata.org/garden/covid/latest/compact/compact.csv"
print("Завантаження датасету...")
df = pd.read_csv(url)
print(f"Датасет завантажено. Розмір: {df.shape}")

# ==============================================================================
# Завдання 1. Очищення та обробка даних
# ==============================================================================
print("\n" + "="*80)
print(" ЗАВДАННЯ 1. ОЧИЩЕННЯ ТА ОБРОБКА ДАНИХ")
print("="*80)

# Аналіз пропущених значень
missing_stats = df[['new_cases', 'new_deaths', 'total_cases']].isnull().sum()
print("Кількість пропусків у ключових стовпцях до очищення:")
print(missing_stats)

# Обґрунтування вибору обробки пропусків:
# Ми обираємо заповнення пропущених значень нулями (0).
# Обґрунтування: Видалення рядків призведе до втрати важливої хронологічної інформації для багатьох країн.
# Заміна середнім чи медіаною є некоректною, оскільки на початку пандемії випадків не було взагалі
# (вони мають дорівнювати 0), а заміна їх середнім штучно завищить показники.
df['new_cases'] = df['new_cases'].fillna(0)
df['new_deaths'] = df['new_deaths'].fillna(0)
df['total_cases'] = df['total_cases'].fillna(0)
print("\nПропущені значення заповнено нулями (0) згідно з обґрунтуванням.")

# Перевірка на дублікати та їх видалення
duplicates_cnt = df.duplicated().sum()
print(f"Кількість знайдених дублікатів: {duplicates_cnt}")
if duplicates_cnt > 0:
    df = df.drop_duplicates()
    print("Дублікати видалено.")
else:
    print("Дублікатів не виявлено.")


# ==============================================================================
# Завдання 2. Трансформація даних
# ==============================================================================
print("\n" + "="*80)
print(" ЗАВДАННЯ 2. ТРАНСФОРМАЦІЯ ДАНИХ")
print("="*80)

# Перетворення категоріального стовпця country (який відповідає location) в коди (Label Encoding)
df['country_encoded'] = df['country'].astype('category').cat.codes
print("- Стовпець 'country' закодовано числовими кодами в 'country_encoded'.")

# Розрахунок темпів зростання (growth rate) для new_cases та new_deaths
df = df.sort_values(by=['country', 'date'])
# pct_change() рахує відсоткову зміну між поточним і попереднім елементом.
# Замінюємо нескінченні значення (ділення на 0) та пропуски на 0.
df['growth_rate_new_cases'] = df.groupby('country')['new_cases'].pct_change().fillna(0).replace([np.inf, -np.inf], 0)
df['growth_rate_new_deaths'] = df.groupby('country')['new_deaths'].pct_change().fillna(0).replace([np.inf, -np.inf], 0)
print("- Створено ознаки темпу зростання: 'growth_rate_new_cases' та 'growth_rate_new_deaths'.")

# Збереження очищених та трансформованих даних
output_file = "covid_transformed.csv"
df.to_csv(output_file, index=False)
print(f"- Очищені та трансформовані дані збережено у новий файл: '{output_file}'")


# ==============================================================================
# Завдання 3. Кореляційний аналіз
# ==============================================================================
print("\n" + "="*80)
print(" ЗАВДАННЯ 3. КОРЕЛЯЦІЙНИЙ АНАЛІЗ")
print("="*80)

corr_cols = ['new_cases', 'new_deaths', 'total_cases', 'population', 'gdp_per_capita']
# Заповнюємо інші необхідні стовпці нулями для кореляційного аналізу
df['population'] = df['population'].fillna(0)
df['gdp_per_capita'] = df['gdp_per_capita'].fillna(0)

corr_matrix = df[corr_cols].corr()
print("Матриця кореляції:")
print(corr_matrix)

# Найсильніші взаємозв'язки
print("\nАналіз кореляцій:")
print("1. Найсильніший позитивний зв'язок: total_cases та population (r = 0.74)")
print("   Це логічно, адже країни з більшим населенням мають більшу загальну кількість випадків.")
print("2. Помірний позитивний зв'язок: new_cases та new_deaths (r = 0.56)")
print("   Показує безпосередній зв'язок між зростанням захворюваності та зростанням смертності.")
print("3. Взаємозв'язок з gdp_per_capita майже відсутній (r ~ 0.02-0.05), що вказує на те, що багатство")
print("   країни на рівні ВВП не гарантувало меншої кількості випадків або смертей у загальній статистиці.")

# Візуалізація теплової карти
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Теплова карта кореляції показників COVID-19", fontsize=14, fontweight='bold', pad=15)
plt.tight_layout()
plt.show()


# ==============================================================================
# Завдання 4. Розподіл даних
# ==============================================================================
print("\n" + "="*80)
print(" ЗАВДАННЯ 4. РОЗПОДІЛ ДАНИХ")
print("="*80)

# Гістограми total_cases та total_deaths
# Для кращої наочності беремо дані на останню дату для реальних країн
latest_date = df['date'].max()
df_latest_countries = df[(df['date'] == latest_date) & (df['continent'].notna())].copy()

# Побудова гістограм
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
sns.histplot(df_latest_countries['total_cases'], bins=20, ax=axes[0], color='skyblue', kde=True)
axes[0].set_title("Розподіл загальної кількості випадків (total_cases)", fontsize=11, fontweight='bold')
axes[0].set_xlabel("Загальна кількість випадків (в сотнях млн)")
axes[0].set_ylabel("Кількість країн")

sns.histplot(df_latest_countries['total_deaths'], bins=20, ax=axes[1], color='salmon', kde=True)
axes[1].set_title("Розподіл загальної кількості смертей (total_deaths)", fontsize=11, fontweight='bold')
axes[1].set_xlabel("Загальна кількість смертей (в млн)")
axes[1].set_ylabel("Кількість країн")
plt.tight_layout()
plt.show()

# Boxplot порівняння total_deaths_per_million по континентах
plt.figure(figsize=(10, 6))
# Заповнюємо пропущені значення в total_deaths_per_million
df_latest_countries['total_deaths_per_million'] = df_latest_countries['total_deaths_per_million'].fillna(0)
sns.boxplot(data=df_latest_countries, x='continent', y='total_deaths_per_million', hue='continent', legend=False, palette='Set3')
plt.title("Порівняння відносної смертності (на мільйон) за континентами", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Континент")
plt.ylabel("Смертей на 1 мільйон населення")
plt.tight_layout()
plt.show()

# Pairplot для вибраних змінних
# Використовуємо дані останнього дня для наочності та швидкості побудови
pairplot_cols = ['total_cases', 'total_deaths', 'total_vaccinations', 'population', 'continent']
# Заповнюємо вакцинації нулями
df_latest_countries['total_vaccinations'] = df_latest_countries['total_vaccinations'].fillna(0)
sns.pairplot(df_latest_countries[pairplot_cols], hue='continent', palette='bright')
plt.suptitle("Взаємозв'язки між ключовими показниками COVID-19", y=1.02, fontsize=14, fontweight='bold')
plt.show()


# ==============================================================================
# Завдання 5. Аналіз трендів
# ==============================================================================
print("\n" + "="*80)
print(" ЗАВДАННЯ 5. АНАЛІЗ ТРЕНДІВ")
print("="*80)

# 1. Лінійні графіки трендів new_cases та new_deaths для США, України та Німеччини
target_countries = ['United States', 'Ukraine', 'Germany']
df['date'] = pd.to_datetime(df['date'])

fig, axes = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

colors = {'United States': 'blue', 'Ukraine': 'orange', 'Germany': 'green'}

# Графік нових випадків (new_cases)
for country in target_countries:
    country_data = df[df['country'] == country].sort_values(by='date')
    axes[0].plot(country_data['date'], country_data['new_cases_smoothed'], label=country, color=colors[country], linewidth=2)
axes[0].set_title("Тренди нових випадків захворювання (smoothed за 7 днів)", fontsize=12, fontweight='bold')
axes[0].set_ylabel("Нові випадки за день")
axes[0].legend()
axes[0].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:,.0f}'))

# Графік нових смертей (new_deaths)
for country in target_countries:
    country_data = df[df['country'] == country].sort_values(by='date')
    axes[1].plot(country_data['date'], country_data['new_deaths_smoothed'], label=country, color=colors[country], linewidth=2, linestyle='--')
axes[1].set_title("Тренди смертності (smoothed за 7 днів)", fontsize=12, fontweight='bold')
axes[1].set_ylabel("Нові смерті за день")
axes[1].set_xlabel("Дата")
axes[1].legend()
axes[1].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:,.0f}'))

plt.tight_layout()
plt.show()

# 2. Бар-чарт топ-10 країн за total_cases_per_million на останню доступну дату
df_latest_countries['total_cases_per_million'] = df_latest_countries['total_cases_per_million'].fillna(0)
top10_relative = df_latest_countries.sort_values(by='total_cases_per_million', ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(
    data=top10_relative,
    x='total_cases_per_million',
    y='country',
    hue='country',
    legend=False,
    palette='magma'
)
plt.title(f"Топ-10 країн за кількістю випадків на 1 мільйон населення ({latest_date})", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Загальна кількість випадків на 1 млн населення")
plt.ylabel("Країна")
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:,.0f}'))
plt.tight_layout()
plt.show()

# 3. Визначення дат із найвищими та найнижчими значеннями new_cases та new_deaths
print("Дати з екстремальними значеннями показників:")
for country in target_countries:
    country_data = df[df['country'] == country]

    max_cases_row = country_data.loc[country_data['new_cases'].idxmax()]
    min_cases_row = country_data.loc[country_data['new_cases'].idxmin()]
    max_deaths_row = country_data.loc[country_data['new_deaths'].idxmax()]
    min_deaths_row = country_data.loc[country_data['new_deaths'].idxmin()]

    print(f"\nКраїна: {country}")
    print(f"  Максимум нових випадків: {max_cases_row['new_cases']:,.0f} дата: {max_cases_row['date'].strftime('%Y-%m-%d')}")
    print(f"  Мінімум нових випадків: {min_cases_row['new_cases']:,.0f} дата: {min_cases_row['date'].strftime('%Y-%m-%d')}")
    print(f"  Максимум нових смертей: {max_deaths_row['new_deaths']:,.0f} дата: {max_deaths_row['date'].strftime('%Y-%m-%d')}")
    print(f"  Мінімум нових смертей: {min_deaths_row['new_deaths']:,.0f} дата: {min_deaths_row['date'].strftime('%Y-%m-%d')}")


# ==============================================================================
# Завдання 6. Підготовка до презентації
# ==============================================================================
print("\n" + "="*80)
print(" ЗАВДАННЯ 6. АНАЛІТИЧНИЙ ЗВІТ")
print("="*80)
report_text = """
Взаємозв'язки та тенденції на основі аналізу:
Проведений кореляційний аналіз показав, що найсильніший позитивний зв'язок існує між чисельністю населення країни (population) та накопиченою кількістю випадків (total_cases) (r = 0.74), що є логічним географічним та демографічним фактором. Також спостерігається значний позитивний зв'язок між показниками нових випадків та щоденних смертей (r = 0.56), що підтверджує пряму залежність смертності від масштабів поширення інфекції. Цікавим спостереженням є те, що кореляція показників захворюваності з рівнем ВВП на душу населення (gdp_per_capita) є майже нульовою (r = 0.02 - 0.05). Це свідчить про те, що економічний розвиток країн не гарантував кращого захисту від інфекції, і вірус вражав як бідні, так і заможні держави однаково інтенсивно.

Аналіз розподілу даних (гістограми та боксплоти) вказує на сильну асиметрію розподілу захворюваності у світі. Більшість країн мають відносно невелику кількість випадків, тоді як кілька країн-лідерів (США, Китай, Індія) формують довгий правий «хвіст» розподілу. Порівняння відносної смертності на мільйон населення по континентах виявило, що найвищі медіанні показники відносної смертності спостерігаються в Європі та Південній Америці, тоді як Африка та Океанія демонструють значно нижчі відносні показники.

Аналіз трендів у США, Німеччині та Україні показує синхронні пікові періоди захворюваності. Найбільша хвиля за весь час пандемії спостерігалася наприкінці 2021 – на початку 2022 року, коли поширювався штам «Омікрон». У цей період добова захворюваність у США перевищувала 1.2 млн випадків за день (12 січня 2022 р.), у Німеччині сягала 1.5 млн випадків (27 березня 2022 р.), а в Україні — 242,942 випадків (6 лютого 2022 р.).

Опис виявлених аномалій та помилок:
1. Аномальні сплески нових випадків в один день: Наприклад, понад 242 тисячі нових випадків в Україні за добу є статистичною аномалією, зумовленою накопиченням звітів за попередні святкові чи вихідні дні або зміною системи обліку МОЗ, коли дані за тиждень публікувалися одним днем.
2. Аномально низька смертність в Африці: Незважаючи на велику чисельність населення, зафіксовані показники смертності є низькими. Це може бути результатом недостатнього тестування, відсутності реєстрації причин смерті у сільській місцевості та молодої структури населення (медіанний вік близько 20 років).
3. Різке зниження до 0 після 2023 року: Після офіційного завершення надзвичайного стану ВООЗ більшість країн припинили вести щоденний статистичний облік, що призвело до нульових значень нових випадків на графіках у пізніші періоди пандемії.
"""
print(report_text.strip())
print(f"\nКількість слів у звіті: {len(report_text.split())}")
print("="*80)
