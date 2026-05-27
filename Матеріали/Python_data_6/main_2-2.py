import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats
import plotly.express as px
import plotly.graph_objects as go


sns.set_theme(style="whitegrid")

df = pd.read_csv('data_clean.csv')

# annual_sales = df.groupby('Year')['Global_Sales'].sum().reset_index()
# coefficients = np.polyfit(annual_sales['Year'], annual_sales['Global_Sales'], 1)
# poly = np.poly1d(coefficients)
# trend_line = poly(annual_sales['Year'])
# plt.figure(figsize=(12, 6))
# sns.lineplot(data=annual_sales, x='Year', y='Global_Sales', marker='o', color='blue', label='Global Sales')
# # plt.plot(annual_sales['Year'], trend_line, color='red', linestyle='--', label='Трендова лінія')
# plt.title('Сумарні глобальні продажі відеоігор за роками з трендовою лінією')
# plt.xlabel('Рік')
# plt.ylabel('Продажі (мільйони одиниць)')
# plt.legend()
# plt.show()

# future_years = np.arange(annual_sales['Year'].max() + 1, annual_sales['Year'].max() + 6)
# future_sales = poly(future_years)

# future_df = pd.DataFrame({
#     'Year': future_years,
#     'Global_Sales': future_sales
# })

# plt.figure(figsize=(12, 6))
# sns.lineplot(data=annual_sales, x='Year', y='Global_Sales', marker='o', color='blue', label='Global Sales')
# plt.plot(annual_sales['Year'], trend_line, color='red', linestyle='--', label='Трендова лінія')
# sns.lineplot(data=future_df, x='Year', y='Global_Sales', marker='x', color='green', label='Прогноз продажів')
# plt.title('Сумарні глобальні продажі відеоігор за роками з трендовою лінією та прогнозом')
# plt.xlabel('Рік')
# plt.ylabel('Продажі (мільйони одиниць)')
# plt.legend()
# plt.show()
# ________________________________________________________

# genre_sales = df.groupby('Genre')['Global_Sales'].sum().reset_index()
# genre_sales_sorted = genre_sales.sort_values(by='Global_Sales', ascending=False)
# top_genres = genre_sales_sorted.head(10)

# plt.figure(figsize=(12, 8))
# sns.barplot(x='Global_Sales', y='Genre', data=top_genres, palette='viridis')
# plt.title('Топ 10 жанрів за сумарними продажами')
# plt.xlabel('Сумарні продажі (мільйони одиниць)')
# plt.ylabel('Жанр')
# plt.show()

# plt.figure(figsize=(12, 8))
# plt.barh(top_genres['Genre'], top_genres['Global_Sales'], color=sns.color_palette('viridis', len(top_genres)))
# plt.title('Топ 10 жанрів за сумарними продажами')
# plt.xlabel('Сумарні продажі (мільйони одиниць)')
# plt.ylabel('Жанр')
# plt.gca().invert_yaxis()
# plt.show()

# platform_sales = df.groupby('Platform')['Global_Sales'].sum().reset_index()
# platform_sales_sorted = platform_sales.sort_values(by='Global_Sales', ascending=False)
# top_platforms = platform_sales_sorted.head(10)

# plt.figure(figsize=(12, 8))
# sns.barplot(x='Global_Sales', y='Platform', data=top_platforms, palette='magma')
# plt.title('Топ 10 платформ за сумарними продажами')
# plt.xlabel('Сумарні продажі (мільйони одиниць)')
# plt.ylabel('Платформа')
# plt.show()
# _________________________________________________________

plt.figure(figsize=(14, 8))
sns.boxplot(x='Genre', y='Global_Sales', data=df, palette='Set3')
plt.title('Розподіл продажів за жанрами відеоігор')
plt.xlabel('Жанр')
plt.ylabel('Продажі (мільйони одиниць)')
plt.xticks(rotation=45)
plt.show()

# plt.figure(figsize=(14, 8))
# sns.boxplot(x='Platform', y='Global_Sales', data=df, palette='Set2')
# plt.title('Розподіл продажів за платформами відеоігор')
# plt.xlabel('Платформа')
# plt.ylabel('Продажі (мільйони одиниць)')
# plt.xticks(rotation=45)
# plt.show()