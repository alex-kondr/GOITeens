import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import dask.dataframe as dd
from sqlalchemy import create_engine


# Що таке ETL
# ETL (англ. Extract, Transform, Load) — це процес
# вилучення (Extract) даних із різних джерел,
# їх подальшої трансформації (Transform)
# у потрібний формат і завантаження (Load) до цільової системи

# data = {
#     'timestamp': [
#         '2026-06-01 10:00:00', 
#         '2026-06-02 11:15:00', 
#         '2026-06-03 12:30:00', 
#         '2026-06-04 14:45:00',
#         '2026-06-05 16:00:00'
#     ],
#     'value': [10.5, np.nan, 23.1, None, 45.7],
#     'sensor_id': ['A', 'B', 'A', 'C', 'B']
# }
# df_to_save = pd.DataFrame(data)
# df_to_save.to_csv('data.csv', index=False)

# df = pd.read_csv('data.csv')
# df['timestamp'] = pd.to_datetime(df['timestamp'])
# df = df.dropna(subset=['value'])
# engine = create_engine('sqlite:///goiteens.db', echo=True)
# df.to_sql('processed_data', engine, if_exists='replace', index=False)

# data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
# df = pd.DataFrame(data)
# df.to_csv('data.csv', index=False)
# df = pd.read_csv('data.csv')
# print(df)

# df.to_json('data.json', orient='records', lines=True)
# df = pd.read_json('data.json', orient='records', lines=True)
# print(df)

# import os
# print(f"CSV: {os.path.getsize('data.csv')} байт")
# print(f"Parquet: {os.path.getsize('data.parquet')} байт")
# print(f"Feather: {os.path.getsize('data.feather')} байт")

# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
#     handlers=[
#         logging.FileHandler("etl.log"),
#         logging.StreamHandler()
#     ]
# )