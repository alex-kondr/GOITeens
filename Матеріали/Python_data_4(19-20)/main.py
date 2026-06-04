import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# pd.to_datetime(arg, errors='raise', dayfirst=False, yearfirst=False, utc=None, format=None, exact=True, unit=None, infer_datetime_format=False, origin='unix')
# 1. arg: Обов'язковий параметр. Дані, які потрібно конвертувати в datetime. Це може бути рядок, список, NumPy масив, серія або DataFrame.
# 2. errors: Опціональний параметр. Визначає, як поводитись з помилками при конвертації.
#     'raise' (за замовчуванням): Викидає помилку.
#     'coerce': Конвертує невірні значення в NaT (Not a Time).
#     'ignore': Повертає оригінальні дані без змін.
# 3. dayfirst: Опціональний параметр (булевий). Якщо встановлено True, то перший день місяця буде трактуватися як день, а не місяць (корисно для форматів DD/MM/YYYY).
# 4.yearfirst: Опціональний параметр (булевий). Якщо встановлено True, то перший елемент буде трактуватися як рік (корисно для форматів YYYY/MM/DD).
# 5.utc: Опціональний параметр. Якщо встановлено True, то результуючий об'єкт буде у UTC.
# 6.format: Опціональний параметр. Строка, що визначає формат вхідних дат за правилами strftime. Використовується для прискорення конвертації, коли формат відомий.
# 7.exact: Опціональний параметр (булевий). Якщо встановлено True, то вхідні рядки повинні точно відповідати формату. Якщо False, дозволяється часткова відповідність.
# 8.unit: Опціональний параметр. Визначає одиницю часу, якщо аргумент представлений як числове значення. Може бути 's' (секунди), 'ms' (мілісекунди), 'us' (мікросекунди), 'ns' (наносекунди).
# 9.infer_datetime_format: Опціональний параметр (булевий). Якщо встановлено True, Pandas намагається вивести формат дат автоматично, що може прискорити конвертацію.
# 10.origin: Опціональний параметр. Визначає точку відліку для числових значень часу. Може бути 'unix' (за замовчуванням), 'julian' або специфікований Timestamp.

# data = {
#     'Event': ['Start', 'Middle', 'End'],
#     'Date': ['2023-01-15', '15/02/2023', 'March 5, 2023']
# }
# df = pd.DataFrame(data)
# df['Date'] = pd.to_datetime(df['Date'], format='mixed')#, dayfirst=True)
# print(df)

# data = {
#     'Date': ['2023-01-15', '2023-02-20', '2023-03-25']
# }
# df = pd.DataFrame(data)
# df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
# print(df)
# '%Y/%m/%d %H:%M:%S' → 2023/05/07 14:30:00

# timestamps = pd.Series([1609459200, 1612137600, 1614556800])
# dates = pd.to_datetime(timestamps, unit='s', origin='unix')
# print(dates)

# Обробка Невірних Значень з errors='coerce'
# dates = pd.Series(['2023-01-15', 'not a date', '2023-03-05'])
# converted_dates = pd.to_datetime(dates, errors='coerce')
# print(converted_dates)

# DataFrame 1:
# events_df = pd.DataFrame({
#     'EventID': [1, 2, 3, 4],
#     'EventName': ['Conference', 'Workshop', 'Seminar', 'Webinar'],
#     'EventDate': ['2023-04-25', '25/05/2023', 'June 10, 2023', '2023-07-15']
# })

# DataFrame 2:
# timestamps_df = pd.DataFrame({
#     'TimestampID': [101, 102, 103, 104],
#     'UnixTimestamp': [1617184800, 1617271200, 1617357600, 1617444000]
# })

# DataFrame 3:
# mixed_dates_df = pd.DataFrame({
#     'RecordID': [201, 202, 203, 204, 205],
#     'DateString': ['2023-08-01', '08/02/2023', '2023/03/15', 'April 20, 2023', 'mixed_dates_df']
# })

# events_df['Year'] = events_df['EventDate'].dt.year
# events_df['Month'] = events_df['EventDate'].dt.month
# events_df['Day'] = events_df['EventDate'].dt.day


# СТВОРЕННЯ ЧАСОВОГО ІНДЕКСУ
# data = {
#     'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
#     'Value': [10, 20, 30]
# }
# df = pd.DataFrame(data)
# df['Date'] = pd.to_datetime(df['Date'])
# df = df.set_index('Date')
# print(df)

# Можна встановити часовий індекс під час створення DataFrame за допомогою параметра index.
# dates = pd.date_range(start='2023-01-01', periods=3, freq='D')
# data = {'Value': [10, 20, 30]}
# df = pd.DataFrame(data, index=dates)
# print(df)

# data = {
#     'Timestamp': ['2023-01-01 08:00', '2023-01-02 09:30', '2023-01-03 11:45'],
#     'Value': [100, 200, 300]
# }
# df = pd.DataFrame(data)
# df['Timestamp'] = pd.to_datetime(df['Timestamp'])
# df = df.set_index('Timestamp')

# Встановлення часової зони:
# df.index = df.index.tz_localize('Europe/Kiev')
# df.index = df.index.tz_convert('Asia/Tokyo')

# Використання pd.Grouper для групування за місяцями:
# dates = pd.date_range(start='2023-01-01', periods=3, freq='D')
# df = pd.DataFrame({'Value': [10, 20, 30]}, index=dates)
# df = df.asfreq('D')
# # grouped = df.groupby(pd.Grouper(freq='M')).sum() #"'M' is no longer supported for offsets. Please use 'ME' instead."
# grouped = df.groupby(pd.Grouper(freq='ME')).sum()
# # print(grouped)
# Зміна частоти даних (наприклад, з денних на місячні).
# monthly_data = df.resample('ME').mean()
# print(monthly_data)

# Вибір Діапазону Дат
# subset = df['2023-01-01':'2023-01-02']

# Агрегація
# Обчислення статистичних показників за різними часовими інтервалами.
# daily_sum = df.resample('D').sum()

# Створимо DataFrame з частковими датами та заповнимо відсутні частини дати.
# partial_dates = {
#     'RecordID': [101, 102, 103],
#     'PartialDate': ['2023-05', 'June 2023', '2023']
# }
# df_partial = pd.DataFrame(partial_dates)
# df_partial['PartialDate'] = pd.to_datetime(df_partial['PartialDate'], errors='coerce')
# df_partial['PartialDate'] = df_partial['PartialDate'].fillna(pd.to_datetime(df_partial['PartialDate'], format='%Y', errors='coerce'))
# df_partial['PartialDate'] = df_partial['PartialDate'].dt.normalize()
# df_partial = df_partial.set_index('PartialDate')
# print(df_partial)

# Форматування Дат у Рядки
# %Y — рік з чотирма цифрами (наприклад, 2023)
# %m — місяць з двома цифрами (01-12)
# %d — день місяця з двома цифрами (01-31)
# %H — година (00-23)
# %M — хвилини (00-59)
# %S — секунди (00-59)

# data = {
#     'Date': ['2023-04-25', '2023-05-30', '2023-06-15'],
#     'Value': [100, 200, 300]
# }
# df = pd.DataFrame(data)
# df['Date'] = pd.to_datetime(df['Date'])
# df['FormattedDate'] = df['Date'].dt.strftime('%d-%m-%Y')

# data = {
#     'Timestamp': ['2023-04-25 14:30:00', '2023-05-30 09:15:00', '2023-06-15 18:45:00']
# }
# df = pd.DataFrame(data)
# df['Timestamp'] = pd.to_datetime(df['Timestamp'])
# df['Formatted'] = df['Timestamp'].dt.strftime('%d/%m/%Y %H:%M')

# data = {
#     'Timestamp': ['2023-04-25 14:30:00', '2023-05-30 09:15:00', '2023-06-15 18:45:00']
# }
# df = pd.DataFrame(data)
# df['Timestamp'] = pd.to_datetime(df['Timestamp']).dt.tz_localize('Europe/Kiev')
# df['Timestamp_Tokyo'] = df['Timestamp'].dt.tz_convert('Asia/Tokyo')
# df['Formatted_Tokyo'] = df['Timestamp_Tokyo'].dt.strftime('%d-%m-%Y %H:%M:%S %Z')
# print(df)


# Завдання 1
# Форматуйте стовпець Timestamp у рядковий формат день-місяць-рік, використовуючи метод dt.strftime().
# data = {
#     'Timestamp': ['2023-04-25 14:30:00', '2023-05-30 09:15:00', '2023-06-15 18:45:00']
# }
# df = pd.DataFrame(data)
# df['Timestamp'] = pd.to_datetime(df['Timestamp'])
# print(df["Timestamp"].dt.strftime("%d-%m-%Y"))

# Завдання 2
# Конвертуйте стовпець DateString у об'єкти datetime, використовуючи формат '%d-%m-%Y' та обробіть невірні дати шляхом перетворення їх у NaT.
# data = {
#     'RecordID': [1, 2, 3],
#     'DateString': ['25-04-2023', '31-02-2023', '15-06-2023']
# }
# df = pd.DataFrame(data)
# # df['DateString'] = pd.to_datetime(df['DateString'], format='%d-%m-%Y', errors='coerce')

# Завдання 3
# Відокремте дату та час у нові стовпці Date та Time відповідно
# data = {
#     'Timestamp': ['2023-04-25 14:30:00', '2023-05-30 09:15:00', '2023-06-15 18:45:00']
# }
# df = pd.DataFrame(data)
# df['Timestamp'] = pd.to_datetime(df['Timestamp'])
# # df['Date'] = df['Timestamp'].dt.date
# # df['Time'] = df['Timestamp'].dt.time
# # print(df)

# Завдання 4
# Форматуйте стовпець Timestamp у формат день/місяць/рік година:хвилина
# data = {
#     'Timestamp': ['2023-04-25 14:30:00', '2023-05-30 09:15:00', '2023-06-15 18:45:00']
# }
# df = pd.DataFrame(data)
# df['Timestamp'] = pd.to_datetime(df['Timestamp'])
# # df['Formatted'] = df['Timestamp'].dt.strftime('%d/%m/%Y %H:%M')

# Завдання 5
# Конвертуйте часову зону стовпця Timestamp з 'Europe/Kiev' на 'Asia/Tokyo' та відформатуйте у вигляді день-місяць-рік година:хвилина:секунда Часова_зона
# data = {
#     'Timestamp': ['2023-04-25 14:30:00+03:00', '2023-05-30 09:15:00+03:00', '2023-06-15 18:45:00+03:00']
# }
# df = pd.DataFrame(data)
# df['Timestamp'] = pd.to_datetime(df['Timestamp'])
# # df['Timestamp_Tokyo'] = df['Timestamp'].dt.tz_convert('Asia/Tokyo')
# # df['Formatted_Tokyo'] = df['Timestamp_Tokyo'].dt.strftime('%d-%m-%Y %H:%M:%S %Z')
# # print(df)

# Завдання 6
# Форматуйте стовпець Timestamp у формат рік/місяць/день година:хвилина (наприклад, 2023/04/25 14:30)
# data = {
#     'Timestamp': ['2023-04-25 14:30:00', '2023-05-30 09:15:00', '2023-06-15 18:45:00']
# }
# df = pd.DataFrame(data)
# # df['Timestamp'] = pd.to_datetime(df['Timestamp'])
# # df['Formatted'] = df['Timestamp'].dt.strftime('%Y/%m/%d %H:%M')
# # print(df)