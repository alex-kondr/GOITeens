import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats
import time



# df = pd.read_csv('https://raw.githubusercontent.com/ValdisW/datasets/master/video-game-sales.csv')
# print(df.head())
# print(df.dtypes)



# dtypes = {
#     "Year": int,
#     "NA_Sales": np.float32,
#     "EU_Sales": np.float32,
#     "JP_Sales": np.float32,
#     "Other_Sales": np.float32,
#     "Global_Sales": np.float32,
#     "Genre": "category",
#     "Publisher": "category",
#     "Platform": "category"
# }
df = pd.read_csv('https://raw.githubusercontent.com/ValdisW/datasets/master/video-game-sales.csv')
numeric_cols = df.select_dtypes(include=['float64']).columns
df = df.dropna(subset=numeric_cols)

df["Year"] = df["Year"].astype(int)
# df_clean["Year"] = pd.to_datetime(df["Year"], errors="coerce", format="%Y").dt.year
df["NA_Sales"] = df["NA_Sales"].astype(np.float32)
df["EU_Sales"] = df["EU_Sales"].astype(np.float32)

df["Genre"] = df["Genre"].astype("category")
df["Publisher"] = df["Publisher"].astype("category")
df["Platform"] = df["Platform"].astype("category")

df["JP_Sales"] = df["JP_Sales"].astype(np.float32)
df["Other_Sales"] = df["Other_Sales"].astype(np.float32)
df["Global_Sales"] = df["Global_Sales"].astype(np.float32)
# print(df_clean.info())
# print(df_clean.describe())
# df_genreglobal = df.groupby('Genre')["Global_Sales"].sum().sort_values(ascending=False)
# df_genrejapan = df.groupby(['Genre', 'Year'])["JP_Sales"].sum().sort_values(ascending=False)
# df_genrejapan = df.groupby(['Genre', 'Year'])["EU_Sales"].sum().sort_values(ascending=False)
# df_genrena = df.groupby('Year')["Global_Sales"].mean()#.sort_values(ascending=False)
# df_genreglobal = df.groupby('Genre')["JP_Sales"].mean()
# df_genreg = df.groupby('Year')["Platform"].mean()
# print(df_genreglobal)

# plt.plot(df_genrena,  label="Глобальні продажі")
# plt.plot(df["Genre"],df["JP_Sales"] , label="Глобальні продажі")
# plt.plot(df_genreg, label="Глобальні продажі")
# sns.boxplot(df["Global_Sales"])
# plt.xlabel('Genre')
# plt.ylabel('Japan sales')
# plt.title(label="японські продажі")
# plt.legend()
# plt.show()

df["Anomaly"] = stats.zscore(df["Global_Sales"])
df = df[(df["Anomaly"] <= 3) & (df["Anomaly"] >= -3)]
df["Anomaly"] = stats.zscore(df["NA_Sales"])
df = df[(df["Anomaly"] <= 3) & (df["Anomaly"] >= -3)]

df["Anomaly"] = stats.zscore(df["JP_Sales"])
df = df[(df["Anomaly"] <= 3) & (df["Anomaly"] >= -3)]

df["Anomaly"] = stats.zscore(df["EU_Sales"])
df = df[(df["Anomaly"] <= 3) & (df["Anomaly"] >= -3)].reset_index()

df.drop(["Anomaly"], inplace=True, axis=1)
df.to_csv("data_clean.csv", index=False)
# print(df.info())

# df_grouped = df.groupby(['Genre', 'Platform']).agg(
#     total_sales=pd.NamedAgg("Global_Sales", "sum"),
#     mean_sales=pd.NamedAgg("Global_Sales", "mean"),
#     max_sales=pd.NamedAgg("Global_Sales", "max")
# ).reset_index()
# print(df_grouped)
# df_Genreglobal = df.groupby('Genre')["Global_Sales"].sum().sort_values(ascending=False).reset_index()

# print(df_Genreglobal.head(5))

# plt.figure(figsize=[10, 8])
# sns.barplot(x="Global_Sales", y="Genre", data=df_Genreglobal.head(5), hue="Genre", palette='viridis')
# plt.title(label="top5 продажів")
# plt.xlabel("Plaatform")
# plt.ylabel("Sales")
# plt.legend()
# plt.show()


# df_Genreglobal = df.groupby('Platform')["Global_Sales"].sum().sort_values(ascending=False).reset_index()

# plt.figure(figsize=[10, 8])
# sns.barplot(x="Global_Sales", y="Platform", data=df_Genreglobal.head(5), hue="Platform", palette='viridis')
# plt.title(label="top5 продажів")
# plt.xlabel("Sales")
# plt.ylabel("Platform")
# plt.legend()
# plt.show()

# df_Genreglobal = df.groupby('Genre')["Global_Sales"].mean().sort_values(ascending=False).reset_index()


# plt.figure(figsize=[10, 8])
# sns.barplot(x="Global_Sales", y="Genre", data=df_Genreglobal.head(5), hue="Genre", palette='viridis')
# plt.title(label="top5 продажів")
# plt.xlabel("Genre")
# plt.ylabel("Sales")
# plt.legend()
# plt.show()


# df_Genreglobal = df.groupby('Platform')["Global_Sales"].mean().sort_values(ascending=False).reset_index()

# plt.figure(figsize=[10, 8])
# sns.barplot(x="Global_Sales", y="Platform", data=df_Genreglobal, hue="Platform", palette='viridis')
# plt.title(label="top5 продажів")
# plt.xlabel("Mean Sales")
# plt.ylabel("Platform")
# plt.legend()
# plt.show()

# df["Sum"] =  df[["NA_Sales","EU_Sales","JP_Sales","Other_Sales"]].sum(axis=1)
# print(df)

# plt.figure(figsize=(10, 6))
# sns.barplot(x='Global_Sales', y='JP_Sales', data=df, palette='viridis', hue='JP_Sales')
# plt.title('Сумарні продажі за регіонами')
# plt.xlabel('Сумарні продажі (мільйони одиниць)')
# plt.ylabel('Регіон')
# plt.show()


# numerical_cols = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
# corr_matrix = df[numerical_cols].corr()
# print("Кореляційна матриця:")
# # print(corr_matrix)

# plt.figure(figsize=(8, 6))
# sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
# plt.title('Кореляційна матриця продажів за регіонами')
# plt.show()