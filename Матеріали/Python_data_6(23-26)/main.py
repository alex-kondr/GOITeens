import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats



# https://github.com/ValdisW/datasets/blob/master/video-game-sales.csv
df = pd.read_csv('https://raw.githubusercontent.com/ValdisW/datasets/master/video-game-sales.csv')
# df = pd.read_csv('Video_Game_Sales.csv')
# df = df.convert_dtypes()
# df["Year"] = pd.to_datetime(df["Year"], errors='coerce', format='%Y')
# df["Rank"] = df["Rank"].astype(np.int8)
# print(df.info())
# print(df.head())
# df.describe()

# Визначте, які жанри, платформи або часові періоди мали найбільший вплив на ринкові тренди.
# genre = df.groupby("Genre")["Global_Sales"].sum().sort_values(ascending=False)
# print(genre)
# time_trends = df.groupby("Year")["Global_Sales"].sum().sort_values(ascending=False)
# print(time_trends)

# Виявіть можливі причини змін у продажах, такі як вихід нових технологій, зміни в споживацьких вподобаннях або економічні умови.
# Надайте рекомендації щодо того, як розробники можуть оптимізувати продажі, виходячи з виявлених трендів.
# Порадьте, на які платформи або жанри варто зосередитися для максимізації доходів.
# Використовуйте отримані дані для прогнозування майбутніх трендів в індустрії відеоігор.
# Розробіть стратегії, які допоможуть розробникам адаптуватися до можливих змін у ринкових умовах.

# Виявлення аномалій у даних про продажі відеоігор за допомогою Z-Score
df['Z_Score_Global_Sales'] = stats.zscore(df['Global_Sales'])
anomalies = df[(df['Z_Score_Global_Sales'] > 3) | (df['Z_Score_Global_Sales'] < -3)]
print("Аномальні записи за Z-Score:")
print(anomalies)

