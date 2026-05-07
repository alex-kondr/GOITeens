import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# Денні дані до місячних
# dates = pd.date_range(start='2023-01-01', periods=90, freq='D')
# data = {'Sales': [200 + i*5 for i in range(90)]}
# df = pd.DataFrame(data, index=dates)
# df = df.asfreq('D')
# # print(df)
# # Зміна частоти даних з денних на місячні
# monthly_data = df.resample('ME').mean()
# print(monthly_data)

# Денні дані до годинних
# Ресемплінг до годинної частоти та заповнення пропусків методом 'ffill'
# dates = pd.date_range(start='2023-01-01', periods=5, freq='D')
# data = {'Temperature': [30, 32, 31, 29, 28]}
# df = pd.DataFrame(data, index=dates)
# hourly_temp = df.resample('h').ffill()
# print(hourly_temp)

# Агрегація з використанням різних функцій
# dates = pd.date_range(start='2023-01-01', periods=30, freq='D')
# data = {'Sales': [100 + i*10 for i in range(30)]}
# df = pd.DataFrame(data, index=dates)
# weekly_avg = df.resample('W').mean()
# weekly_sum = df.resample('W').sum()
# weekly_max = df.resample('W').max()
# print("Weekly Average:\n", weekly_avg)
# print("\nWeekly Sum:\n", weekly_sum)
# print("\nWeekly Max:\n", weekly_max)


# SHIFTING (ЗМІЩЕННЯ)
# Зміщення даних вперед на один період
# dates = pd.date_range(start='2023-01-01', periods=5, freq='D')
# data = {'Sales': [200, 220, 250, 270, 300]}
# df = pd.DataFrame(data, index=dates)
# df['Sales_Shifted'] = df['Sales'].shift(1)
# print(df)

# Розрахунок змін у продажах порівняно з попереднім періодом
# dates = pd.date_range(start='2023-01-01', periods=5, freq='D')
# data = {'Sales': [200, 220, 250, 270, 300]}
# df = pd.DataFrame(data, index=dates)
# df['Sales_Lag1'] = df['Sales'].shift(1)
# df['Sales_Change'] = df['Sales'] - df['Sales_Lag1']
# print(df)

# Зміщення даних назад на два періоди
# dates = pd.date_range(start='2023-01-01', periods=5, freq='D')
# data = {'Sales': [200, 220, 250, 270, 300]}
# df = pd.DataFrame(data, index=dates)
# df['Sales_Shifted_Back2'] = df['Sales'].shift(-2)
# print(df)

# Комбінування Resampling та Shifting
# dates = pd.date_range(start='2023-01-01', periods=90, freq='D')
# data = {'Sales': [200 + i*5 for i in range(90)]}
# df = pd.DataFrame(data, index=dates)
# monthly_avg = df.resample('ME').mean()
# monthly_avg['Sales_Shifted'] = monthly_avg['Sales'].shift(1)
# print(monthly_avg)


# Практика 1
# dates = pd.date_range(start='2023-01-01', periods=14, freq='D')
# data = {'Sales': [200, 220, 250, 270, 300, 310, 330, 340, 360, 380, 400, 420, 450, 470]}
# df = pd.DataFrame(data, index=dates)
# weekly_sales = df.resample('W').sum()
# print(weekly_sales)

# Практика 2
# dates = pd.date_range(start='2023-06-01', periods=5, freq='D')
# data = {'Temperature': [22, 21, 23, 24, 25]}
# df = pd.DataFrame(data, index=dates)
# df['Temp_Shifted_Forward'] = df['Temperature'].shift(1)
# df['Temp_Shifted_Backward'] = df['Temperature'].shift(-2)
# print(df)

# Практика 3
# dates = pd.date_range(start='2023-01-01', periods=90, freq='D')
# data = {'Sales': [200 + i*5 for i in range(90)]}
# df = pd.DataFrame(data, index=dates)
# monthly_avg = df.resample('M').mean()
# monthly_avg['Sales_Predicted'] = monthly_avg['Sales'].shift(1)
# print(monthly_avg.head())

# Практика 4
# dates = pd.date_range(start='2023-01-01', periods=60, freq='D')
# data = {'Temperature': [30, 32, 31, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13,
#                         12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7,
#                         -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25]}
# df = pd.DataFrame(data, index=dates)
# print(df.head())
# monthly_avg = df.resample('ME').mean()
# monthly_avg_filled = monthly_avg.fill()
# print(monthly_avg_filled.head())

# Практика 5
# dates = pd.date_range(start='2020-01-01', periods=365*3, freq='D')  # 3 роки
# data = {'Expenses': [100 + (i % 30)*2 for i in range(365*3)]}
# df = pd.DataFrame(data, index=dates)
# # df.groupby(pd.Grouper(freq='Y'))
# annual_expenses = df.groupby(pd.Grouper(freq='YE')).sum()
# print(annual_expenses)

# Практика 6
# dates = pd.to_datetime(['2023-01-01 08:00', '2023-01-01 12:00', '2023-01-01 18:00',
#                         '2023-01-02 09:00', '2023-01-02 15:00'])
# data = {'Temperature': [22, 24, 23, 25, 26]}
# df = pd.DataFrame(data, index=dates)
# print(df)
# hourly_temp = df.resample('h').asfreq()
# hourly_temp_filled = hourly_temp.bfill()
# print(hourly_temp_filled)