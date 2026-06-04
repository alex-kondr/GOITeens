import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats
import plotly.express as px
import plotly.graph_objects as go


sns.set_theme(style="whitegrid")

# df = pd.read_csv('data_clean.csv', parse_dates=['Year'], index_col='Year')
df = pd.read_csv('data_clean.csv')
# print(annual_sales.head())

# x = sales.index.year
# y = sales['Global_Sales']

# # coefficients = np.polyfit(x, y, 1)
# # poly = np.poly1d(coefficients)
# # trend_line = poly(x)

# plt.figure(figsize=(12, 6))
# sns.lineplot(x=x, y=y, marker='o', label='Global Sales')
# # plt.plot(x, trend_line, color='red', linestyle='--', label='Trend Line')
# plt.title('Сумарні глобальні продажі відеоігор за роками з трендовою лінією')
# plt.xlabel('Рік')
# plt.ylabel('Продажі (мільйони одиниць)')
# plt.legend()
# plt.show()

# Аналіз трендів:
# Початок 1990-х: Сплеск продажів може бути
# пов'язаний з появою таких платформ як Super
# Nintendo та Sega Genesis, які ввели нові
# стандарти якості графіки та геймплею.

# Середина 2000-х: Пік продажів може відображати
# популярність платформ PlayStation 2 і Xbox,
# а також успіх таких ігор як GTA, Call of Duty
# та інших великих франшиз.

# Зниження після 2010 року: Спад може бути
# пов'язаний зі зростаючою популярністю
# мобільних ігор, що змінили споживацькі переваги,
# а також із збільшенням використання цифрових
# дистрибуційних платформ, що може не повністю
# відображатися у традиційних вимірах продажів "в коробці".

# _______________________________________________________
# Завдання:
# 1. Використайте Seaborn barplot() або Matplotlib bar()
# для створення стовпчикових діаграм, які порівнюють
# продажі за різними жанрами та платформами.
# 2. Візуалізуйте топові жанри та платформи за обсягами
# продажів, забезпечуючи кожному стовпчику унікальний колір.

# print(df[['Genre', 'Platform']].isnull().sum())

# genre_sales = df.groupby('Genre')['Global_Sales'].sum().reset_index()
# genre_sales_sorted = genre_sales.sort_values(by='Global_Sales', ascending=False)
# top_genres = genre_sales_sorted.head(10)
# print(top_genres)

# plt.figure(figsize=(12, 8))
# sns.barplot(x='Global_Sales', y='Genre', data=top_genres, palette='viridis')
# plt.title('Топ-10 жанрів за продажами')
# plt.xlabel('Продажі (мільйони одиниць)')
# plt.ylabel('Жанр')
# plt.show()

# plt.figure(figsize=(12, 8))
# plt.barh(top_genres['Genre'], top_genres['Global_Sales'], color=sns.color_palette('viridis', len(top_genres)))
# plt.title('Топ 10 жанрів за сумарними продажами')
# plt.xlabel('Сумарні продажі (мільйони одиниць)')
# plt.ylabel('Жанр')
# plt.gca().invert_yaxis()
# plt.show()

# colors_genres = sns.color_palette('Set2', len(top_genres))

# plt.figure(figsize=(12, 8))
# plt.barh(top_genres['Genre'], top_genres['Global_Sales'], color=colors_genres)
# plt.title('Топ 10 жанрів за сумарними продажами з унікальними кольорами')
# plt.xlabel('Сумарні продажі (мільйони одиниць)')
# plt.ylabel('Жанр')
# plt.gca().invert_yaxis()
# plt.show()

# platform_sales = df.groupby('Platform')['Global_Sales'].sum().reset_index()
# platform_sales_sorted = platform_sales.sort_values(by='Global_Sales', ascending=False)
# top_platforms = platform_sales_sorted.head(10)
# print(top_platforms)

# plt.figure(figsize=(12, 8))
# sns.barplot(x='Global_Sales', y='Platform', data=top_platforms, palette='viridis')
# plt.title('Топ-10 платформ за продажами')
# plt.xlabel('Продажі (мільйони одиниць)')
# plt.ylabel('Платформа')
# plt.show()


# colors_platforms = sns.color_palette('Set2', len(top_platforms))

# plt.figure(figsize=(12, 8))
# plt.barh(top_platforms['Platform'], top_platforms['Global_Sales'], color=colors_platforms)
# plt.title('Топ 10 платформ за сумарними продажами з унікальними кольорами')
# plt.xlabel('Сумарні продажі (мільйони одиниць)')
# plt.ylabel('Платформа')
# plt.gca().invert_yaxis()
# plt.show()

# _______________________________________________________
# genre_sales = df.groupby('Genre')['Global_Sales'].apply(list).reset_index()
# print(genre_sales.head())

# plt.figure(figsize=(12, 8))
# sns.boxplot(x='Genre', y='Global_Sales', data=df, palette='Set3')
# plt.title('Розподіл продажів за жанрами')
# plt.xlabel('Жанр')
# plt.ylabel('Продажі (мільйони одиниць)')
# plt.xticks(rotation=45)
# plt.show()

# platform_sales = df.groupby('Platform')['Global_Sales'].apply(list).reset_index()
# print(platform_sales.head())

# plt.figure(figsize=(12, 8))
# sns.boxplot(x='Platform', y='Global_Sales', data=df, palette='Set2')
# plt.title('Розподіл продажів за платформами')
# plt.xlabel('Платформа')
# plt.ylabel('Продажі (мільйони одиниць)')
# plt.xticks(rotation=45)
# plt.show()
# ________________________________________________________________________________

# numerical_cols = ['Global_Sales', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']
# corr_matrix = df[numerical_cols].corr()
# plt.figure(figsize=(10, 8))
# sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
# plt.title('Кореляційна матриця продажів за регіонами')
# plt.show()
# ________________________________________________________________________________________
# annual_sales = df.groupby('Year')['Global_Sales'].sum().reset_index()

# fig = px.line(annual_sales, x='Year', y='Global_Sales',
#               title='Сумарні глобальні продажі відеоігор за роками',
#               labels={'Global_Sales': 'Продажі (мільйони одиниць)', 'Year': 'Рік'},
#               markers=True)

# z = np.polyfit(annual_sales['Year'], annual_sales['Global_Sales'], 1)
# p = np.poly1d(z)
# fig.add_traces(go.Scatter(x=annual_sales['Year'], y=p(annual_sales['Year']),
#                            mode='lines',
#                            name='Тренд',
#                            line=dict(color='red', dash='dash')))

# fig.show()

# genre_platform_sales = df.groupby(['Genre', 'Platform'])['Global_Sales'].sum().reset_index()
# sales_pivot = genre_platform_sales.pivot(index='Genre', columns='Platform', values='Global_Sales').fillna(0)

# fig = px.imshow(sales_pivot,
#                 labels=dict(x="Платформа", y="Жанр", color="Продажі (мільйони)"),
#                 x=sales_pivot.columns,
#                 y=sales_pivot.index,
#                 color_continuous_scale='Viridis',
#                 title='Теплова карта продажів за жанрами та платформами')

# fig.show()

fig = px.line(df, x='Year', y='Global_Sales', color='Genre',
              title='Продажі відеоігор за роками та жанрами',
              labels={'Global_Sales': 'Продажі (мільйони одиниць)', 'Year': 'Рік'},
              markers=True)

fig.update_layout(legend_title_text='Жанр')
fig.show()