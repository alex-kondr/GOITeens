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
# Ресемпліруємо дані до тижневої частоти, обчисливши суму продажів за кожен тиждень.
# dates = pd.date_range(start='2023-01-01', periods=14, freq='D')
# data = {'Sales': [200, 220, 250, 270, 300, 310, 330, 340, 360, 380, 400, 420, 450, 470]}
# df = pd.DataFrame(data, index=dates)
# weekly_sales = df.resample('W').sum()
# print(weekly_sales)

# Практика 2
# dates = pd.date_range(start='2023-06-01', periods=5, freq='D')
# data = {'Temperature': [22, 21, 23, 24, 25]}
# df = pd.DataFrame(data, index=dates)
# Зсунемо дані температури вперед на один день.
# df['Temp_Shifted_Forward'] = df['Temperature'].shift(1)
# Зсунемо дані температури назад на два дні
# df['Temp_Shifted_Backward'] = df['Temperature'].shift(-2)
# print(df)

# Практика 3
# dates = pd.date_range(start='2023-01-01', periods=90, freq='D')
# data = {'Sales': [200 + i*5 for i in range(90)]}
# df = pd.DataFrame(data, index=dates)
# Ресемплюємо дані до місячної частоти, обчисливши середнє значення продажів за кожен місяць
# monthly_avg = df.resample('M').mean()
# Зсунемо середні продажі на місяць вперед для створення прогнозу.
# monthly_avg['Sales_Predicted'] = monthly_avg['Sales'].shift(1)
# print(monthly_avg.head())

# Практика 4
# dates = pd.date_range(start='2023-01-01', periods=60, freq='D')
# data = {'Temperature': [30, 32, 31, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13,
#                         12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7,
#                         -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25]}
# df = pd.DataFrame(data, index=dates)
# print(df.head())
# Ресемплюємо дані до місячної частоти, обчисливши середню температуру за кожен місяць.
# monthly_avg = df.resample('ME').mean()
# Заповнимо пропущені значення методом "forward fill".
# monthly_avg_filled = monthly_avg.ffill()
# print(monthly_avg_filled.head())

# Практика 5
# dates = pd.date_range(start='2020-01-01', periods=365*3, freq='D')  # 3 роки
# data = {'Expenses': [100 + (i % 30)*2 for i in range(365*3)]}
# df = pd.DataFrame(data, index=dates)
# Використоваємо Grouper, групуємо дані за роками.
# # df.groupby(pd.Grouper(freq='YE')).sum()
# Обчислимо загальні витрати за кожен рік.
# annual_expenses = df.groupby(pd.Grouper(freq='YE')).sum() #- це те саме, що і df.resample('YE').sum()
# print(annual_expenses)

# Практика 6
# dates = pd.to_datetime(['2023-01-01 08:00', '2023-01-01 12:00', '2023-01-01 18:00',
#                         '2023-01-02 09:00', '2023-01-02 15:00'])
# data = {'Temperature': [22, 24, 23, 25, 26]}
# df = pd.DataFrame(data, index=dates)
# print(df)
# Ресемплюємо дані до щогодинної частоти.
# hourly_temp = df.resample('h').asfreq()
# Заповнимо пропущені значення методом "backward fill".
# hourly_temp_filled = hourly_temp.bfill()
# print(hourly_temp_filled)

# Завдання 1
# Ресемпліруйте дані до щотижневої частоти, обчисливши середню температуру за кожен тиждень.
# dates = pd.date_range(start='2023-01-01', periods=10, freq='D')
# data = {'Temperature': [22, 21, 23, 24, 25, 26, 24, 23, 22, 21]}
# df = pd.DataFrame(data, index=dates)
# # weekly_avg_temp = df.resample('W').mean()
# # print(weekly_avg_temp)

# Завдання 2
# Upsample дані до щохвилинної частоти та заповніть пропущені значення методом "forward fill".
# dates = pd.date_range(start='2023-01-01 00:00', periods=5, freq='H')
# data = {'Sales': [100, 150, 200, 250, 300]}
# df = pd.DataFrame(data, index=dates)
# # minute_sales = df.resample('T').ffill()
# # print(minute_sales)

# Завдання 3
# Змістіть дані витрат на один день вперед та обчисліть зміну витрат порівняно з попереднім днем.
# dates = pd.date_range(start='2022-01-01', periods=10, freq='D')
# data = {'Expenses': [500, 600, 550, 700, 650, 800, 750, 900, 850, 1000]}
# df = pd.DataFrame(data, index=dates)
# # df['Expenses_Shifted'] = df['Expenses'].shift(1)
# # df['Expenses_Change'] = df['Expenses'] - df['Expenses_Shifted']

# Завдання 4
# Ресемплюйте дані до місячної частоти, обчисливши середні продажі за кожен місяць.
# Зсунути середні продажі на місяць вперед для створення прогнозу.
# Візуалізуйте фактичні та прогнозовані середні місячні продажі на одному графіку.
# dates = pd.date_range(start='2023-01-01', periods=365, freq='D')
# data = {'Sales': [100 + (i % 30)*3 for i in range(365)]}
# df = pd.DataFrame(data, index=dates)
# # monthly_avg = df.resample('ME').mean()
# # monthly_avg['Sales_Predicted'] = monthly_avg['Sales'].shift(1)
# # plt.figure(figsize=(10, 6))
# # plt.plot(monthly_avg.index, monthly_avg['Sales'], label='Actual Sales', marker='o')
# # plt.plot(monthly_avg.index, monthly_avg['Sales_Predicted'], label='Predicted Sales', marker='o')
# # plt.title('Actual vs Predicted Monthly Sales')
# # plt.xlabel('Date')
# # plt.ylabel('Sales')
# # plt.legend()
# # plt.show()

# Завдання 5
# Створіть колонку Close_Lag1, яка містить ціну закриття на день перед поточним.
# Створіть колонку Close_Lag2, яка містить ціну закриття за два дні до поточного.
# Видаліть рядки з пропущеними значеннями після створення лагів.
# dates = pd.date_range(start='2023-01-01', periods=5, freq='D')
# data = {'Close': [150, 152, 151, 153, 155]}
# df = pd.DataFrame(data, index=dates)
# # df['Close_Lag1'] = df['Close'].shift(-1)
# # df['Close_Lag2'] = df['Close'].shift(-2)
# # df.dropna(inplace=True)
# # print(df)

# Групування за днями
# dates = pd.date_range(start='2023-01-01', periods=48, freq='h')
# data = {'Sales': [100 + i*5 for i in range(48)]}
# df = pd.DataFrame(data, index=dates)
# daily_sales = df.groupby(pd.Grouper(freq='D')).sum()
# print(daily_sales)

# Групування за тижнями
# dates = pd.date_range(start='2023-01-01', periods=14, freq='D')
# data = {'Expenses': [500, 600, 550, 700, 650, 800, 750, 900, 850, 1000, 950, 1100, 1050, 1200]}
# df = pd.DataFrame(data, index=dates)
# weekly_avg_expenses = df.groupby(pd.Grouper(freq='W')).mean()

# Групування за місяцями
# dates = pd.date_range(start='2023-01-01', periods=90, freq='D')
# data = {'Sales': [200 + i*5 for i in range(90)]}
# df = pd.DataFrame(data, index=dates)
# monthly_avg_sales = df.groupby(pd.Grouper(freq='M')).mean()
# print(monthly_avg_sales)

# Використання pd.Grouper для групування за датами
# pd.Grouper(freq='Частота', key='Стовпець_з_датою')

# data = {
#     'Date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
#     'Expenses': [500, 600, 550, 700, 650, 800, 750, 900, 850, 1000]
# }
# df = pd.DataFrame(data)
# weekly_sum_expenses = df.groupby(pd.Grouper(key='Date', freq='W')).sum()

# Використання dt accessor для створення нових стовпців
# dates = pd.date_range(start='2023-01-01', periods=10, freq='D')
# data = {'Sales': [100, 150, 200, 250, 300, 350, 400, 450, 500, 550]}
# df = pd.DataFrame(data, index=dates)
# df['Year'] = df.index.year
# df['Month'] = df.index.month
# grouped = df.groupby(['Year', 'Month']).sum()
# print(grouped)

# Використання resample() замість groupby()
# dates = pd.date_range(start='2023-01-01', periods=10, freq='D')
# data = {'Expenses': [500, 600, 550, 700, 650, 800, 750, 900, 850, 1000]}
# df = pd.DataFrame(data, index=dates)
# weekly_sum_expenses = df.resample('W').sum()
# print(weekly_sum_expenses)

# Завдання 1
# Групуйте дані за місяцями та обчисліть середній обсяг продажів за кожен місяць.
# data = {
#     'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
#     'Sales': [200, 220, 250, 270, 300]
# }
# df = pd.DataFrame(data)
# df['Date'] = pd.to_datetime(df['Date'])
# df = df.set_index('Date')
# # monthly_avg_sales = df.groupby(pd.Grouper(freq='M')).mean()
# # print(monthly_avg_sales)

# Завдання 2
# Групуйте дані за днями та обчисліть максимальне виробництво за кожен день.
# data = {
#     'Timestamp': [
#         '2023-03-01 08:00:00', '2023-03-01 09:00:00', '2023-03-01 10:00:00',
#         '2023-03-01 11:00:00', '2023-03-01 12:00:00'
#     ],
#     'Production': [100, 150, 200, 250, 300]
# }
# df = pd.DataFrame(data)
# df['Timestamp'] = pd.to_datetime(df['Timestamp'])
# df = df.set_index('Timestamp')
# # daily_max_production = df.groupby((pd.Grouper(freq="D"))).max()
# # print(daily_max_production)

# Завдання 3
# Конвертуйте стовпець PartialDate у об'єкти datetime, заповніть відсутні частини дати (день) значенням 1, і встановіть його як індекс
# partial_dates = {
#     'RecordID': [101, 102, 103, 104],
#     'PartialDate': ['2023-05', 'June 2023', '2023', '2023-07']
# }
# df_partial = pd.DataFrame(partial_dates)
# # df_partial['PartialDate'] = pd.to_datetime(df_partial['PartialDate'], errors='coerce', format='%Y-%m')
# # df_partial['PartialDate'] = pd.to_datetime(df_partial['PartialDate'], errors='coerce', format='%B %Y')
# # df_partial['PartialDate'] = pd.to_datetime(df_partial['PartialDate'], errors='coerce', format='%Y')
# # df_partial['PartialDate'] = pd.to_datetime(df_partial['PartialDate'], errors='coerce')
# # df_partial.set_index('PartialDate', inplace=True)

# Завдання 4
# Ресемплюйте дані до щомісячної частоти, обчисливши середні продажі за кожен місяць.
# Заповніть пропущені значення методом "forward fill".
# Візуалізуйте середні місячні продажі після заповнення пропусків.
# dates = pd.date_range(start='2023-01-01', periods=365, freq='D')
# data = {'Sales': [100 + (i % 30)*3 for i in range(365)]}
# df = pd.DataFrame(data, index=dates)
# # monthly_avg = df.resample('ME').mean()
# # monthly_avg_filled = monthly_avg.ffill()

# Завдання 5
# Ресемплюйте дані до щогодинної частоти.
# Заповніть пропущені значення методом "backward fill".
# dates = pd.to_datetime(['2023-01-01 08:00', '2023-01-01 12:00', '2023-01-01 18:00',
#                         '2023-01-02 09:00', '2023-01-02 15:00'])
# data = {'Temperature': [22, 24, 23, 25, 26]}
# df = pd.DataFrame(data, index=dates)
# # hourly_temp = df.resample('h').asfreq()
# # hourly_temp_filled = hourly_temp.bfill()


# ВІЗУАЛІЗАЦІЯ ЧАСОВИХ РЯДІВ

# Лінійні графіки (Line Plots)
# dates = pd.date_range(start='2023-01-01', periods=100, freq='D')
# data = {'Sales': [100 + i*2 + (i%10)*5 for i in range(100)]}
# df = pd.DataFrame(data, index=dates)
# df['Sales'].plot(figsize=(12, 6))
# plt.title('Щоденні Продажі')
# plt.xlabel('Дата')
# plt.ylabel('Продажі')
# plt.grid(True)
# plt.show()

# Стовпчикові графіки (Bar Charts)
# df['Sales'].plot(kind='bar', figsize=(12, 6))
# plt.title('Щоденні Продажі')
# plt.xlabel('Дата')
# plt.ylabel('Продажі')
# plt.show()

# Box Plot (Коробковий графік)
# Використовується для відображення розподілу даних за різними категоріями часу, наприклад, за місяцями або днями тижня.
# Допомагає виявити медіану, квартилі та аномалії.
# df['Month'] = df.index.month
# df.boxplot(column='Sales', by='Month', figsize=(12, 6))
# plt.title('Розподіл Продажів за Місяцями')
# plt.suptitle('')
# plt.xlabel('Місяць')
# plt.ylabel('Продажі')
# plt.show()

# Heatmap (Теплова карта)
# df['DayOfWeek'] = df.index.day_name()
# df['Hour'] = df.index.hour
# heatmap_data = df.pivot_table(values='Sales', index='DayOfWeek', columns='Hour', aggfunc='mean')
# plt.figure(figsize=(14, 7))
# sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap='YlGnBu')
# plt.title('Середні Продажі за Днями Тижня та Годинами')
# plt.xlabel('Година')
# plt.ylabel('День Тижня')
# plt.show()