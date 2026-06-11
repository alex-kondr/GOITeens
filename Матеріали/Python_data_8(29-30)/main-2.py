import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np


# Теплові карти (Heatmaps)
# Приклад 1
# np.random.seed(0)
# z = np.random.randint(0, 100, (10, 10))
# fig = go.Figure(data=go.Heatmap(z=z, colorscale='Viridis'))
# fig.update_layout(title='Базова теплова карта')
# fig.show()

# Приклад 2
# Теплова карта з анотаціями та кастомним кольоровим масштабом
# np.random.seed(1)
# z = np.random.randint(0, 100, (5, 5))
# x = ['A', 'B', 'C', 'D', 'E']
# y = ['W', 'X', 'Y', 'Z', 'V']
# fig = go.Figure(data=go.Heatmap(
#     z=z,
#     x=x,
#     y=y,
#     colorscale='Cividis',
#     text=z,
#     hoverinfo='text'
# ))
# fig.update_layout(title='Теплова карта з анотаціями')
# fig.show()

# Географічні карти (Geographical Maps)
# fig = go.Figure(go.Scattergeo(
#     lon = [-74, -118, 2.35, 139],
#     lat = [40.71, 34.05, 48.86, 35.69],
#     text = ['New York', 'Los Angeles', 'Paris', 'Tokyo'],
#     mode = 'markers',
#     marker = dict(
#         size = [10, 20, 15, 25],
#         color = [10, 20, 15, 25],
#         colorscale = 'Portland',
#         colorbar_title = "Масштаб"
#     )
# ))
# fig.update_layout(
#     title = 'Географічна карта міст',
#     geo_scope='world'
# )
# fig.show()

# Географічна карта з кластеризацією даних
# df = pd.DataFrame({
#     'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
#     'Latitude': [40.7128, 34.0522, 41.8781, 29.7604, 33.4484],
#     'Longitude': [-74.0060, -118.2437, -87.6298, -95.3698, -112.0740],
#     'Sales': [1000, 1500, 800, 1200, 900]
# })
# fig = go.Figure(go.Scattergeo(
#     lon = df['Longitude'],
#     lat = df['Latitude'],
#     text = df['City'] + '<br>Продажі: ' + df['Sales'].astype(str),
#     mode = 'markers',
#     marker = dict(
#         size = df['Sales'] / 100,
#         color = df['Sales'],
#         colorscale = 'Blues',
#         colorbar_title = "Продажі"
#     )
# ))
# fig.update_layout(
#     title = 'Продажі за містами',
#     geo = dict(
#         scope='usa',
#         projection_type='albers usa',
#         showland = True,
#         landcolor = 'rgb(217, 217, 217)',
#         subunitwidth=1,
#         countrywidth=1,
#         subunitcolor="rgb(255, 255, 255)",
#         countrycolor="rgb(255, 255, 255)"
#     )
# )
# fig.show()

# 3D-діаграми (3D Charts)
# np.random.seed(0)
# x = np.linspace(-10, 10, 100)
# y = np.sin(x)
# z = np.cos(y)

# fig = go.Figure(data=[go.Scatter3d(
#     x=x,
#     y=y,
#     z=z,
#     mode='lines',
#     line=dict(color='blue', width=4)
# )])
# fig.update_layout(
#     title='3D-Лінійна діаграма',
#     scene=dict(
#         xaxis_title='X',
#         yaxis_title='Y',
#         zaxis_title='Z'
#     ),
#     width=700,
#     height=700
# )
# fig.show()

# np.random.seed(0)
# x = np.linspace(-10, 10, 100)
# y = np.linspace(-10, 10, 100)
# X, Y = np.meshgrid(x, y)
# Z = np.square(X) - np.square(Y)
# fig = go.Figure(data=[go.Surface(
#     x=X,
#     y=Y,
#     z=Z,
#     colorscale='Viridis'
# )])
# fig.update_layout(
#     title='3D-Лінійна діаграма',
#     scene=dict(
#         xaxis_title='X',
#         yaxis_title='Y',
#         zaxis_title='Z'
#     ),
#     width=700,
#     height=700
# )
# fig.show()

# x = np.linspace(-5, 5, 50)
# y = np.linspace(-5, 5, 50)
# x, y = np.meshgrid(x, y)
# z = np.sin(np.sqrt(x**2 + y**2))
# fig = go.Figure(data=[go.Surface(x=x, y=y, z=z, colorscale='Jet')])
# fig.update_layout(
#     title='3D Surface Plot',
#     scene=dict(
#         xaxis_title='X',
#         yaxis_title='Y',
#         zaxis_title='Z'
#     ),
#     width=800,
#     height=800
# )
# fig.show()


# Завдання
# Ви хочете створити базову географічну карту з маркерами для чотирьох міст: Нью-Йорк, Лос-Анджелес, Париж та Токіо. Використати кольорову шкалу "Portland" для відображення значень продажів.
# Кількість продажів у кожному місті: [1000, 1500, 800, 1200].
# Координати міст:
# Нью-Йорк: (40.7128, -74.0060)
# Лос-Анджелес: (34.0522, -118.2437)
# Париж: (48.8566, 2.3522)
# Токіо: (35.6895, 139.6917)
# Завдання:
# Імпортувати необхідні бібліотеки.
# Створити DataFrame з даними про міста.
# Створити географічну карту за допомогою go.Scattergeo.
# Налаштувати розміри та кольори маркерів відповідно до продажів.
# Додати заголовок графіка.
# Відобразити графік.

# Завдання
# Ви бажаєте створити 3D Surface Plot з використанням даних, згенерованих за допомогою NumPy. Використати кольорову шкалу "Jet" для відображення висотних відмінностей.
# Матриці x, y, z, де z = sin(sqrt(x^2 + y^2)).
# Діапазон x та y від -5 до 5 з 50 точками.
# Завдання:
# Імпортувати необхідні бібліотеки.
# Згенерувати матриці x, y, z за допомогою numpy.
# Створити 3D Surface Plot за допомогою go.Surface.
# Задати кольорову шкалу "Jet".
# Додати заголовок та назви осей.
# Відобразити графік.


# ВИКОРИСТАННЯ PLOTLY З PANDAS
# df = pd.DataFrame({
#     'Category': ['A', 'B', 'C', 'D'],
#     'Values': [23, 17, 35, 29]
# })
# fig = px.bar(df, x='Category', y='Values', title='Стовпчаста діаграма з Pandas DataFrame')
# fig.show()


# ВИКОРИСТАННЯ PLOTLY З NUMPY
# x = np.random.randn(100)
# y = np.random.randn(100)
# z = np.random.randn(100)
# fig = go.Figure(data=[go.Histogram2d(
#     x=x,
#     y=y,
#     z=z,
#     colorscale='Blues'
# )])
# fig.update_layout(
#     title='3D Гістограма з NumPy даними',
#     scene=dict(
#         xaxis_title='X',
#         yaxis_title='Y',
#         zaxis_title='Z'
#     ),
#     width=700,
#     height=700
# )
# fig.show()

# x = np.random.randn(100)
# y = np.random.randn(100)
# z = np.random.randn(100)

# fig = go.Figure(data=[go.Scatter3d(
#     x=x,
#     y=y,
#     z=z,
#     mode='markers',
#     marker=dict(
#         size=6,
#         color=z,
#         colorscale='Blues',
#         opacity=0.8
#     )
# )])
# fig.update_layout(
#     title='3D Хмара точок (Альтернатива 3D Гістограмі)',
#     scene=dict(
#         xaxis_title='X',
#         yaxis_title='Y',
#         zaxis_title='Z'
#     ),
#     width=700,
#     height=700
# )
# fig.show()


# ВИКОРИСТАННЯ PLOTLY З ІНШИМИ БІБЛІОТЕКАМИ
# import plotly.express as px
# from sklearn.datasets import make_blobs
# from sklearn.cluster import KMeans
# import pandas as pd

# X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)
# df = pd.DataFrame(X, columns=['X', 'Y'])
# kmeans = KMeans(n_clusters=4)
# kmeans.fit(df)
# df['Cluster'] = kmeans.labels_
# fig = px.scatter(df, x='X', y='Y', color='Cluster', title='Кластеризація даних з K-Means')
# fig.show()


# ВІЗУАЛІЗАЦІЯ ДАНИХ З TENSORFLOW ТА PLOTLY
# import plotly.express as px
# import tensorflow as tf
# import numpy as np
# import pandas as pd

# np.random.seed(0)
# data = np.random.randn(100, 3)
# df = pd.DataFrame(data, columns=['Feature1', 'Feature2', 'Feature3'])
# model = tf.keras.Sequential([
#     tf.keras.layers.Dense(2, activation='relu', input_shape=(3,))
# ])
# model.compile(optimizer='adam', loss='mse')
# model.fit(df, np.random.randn(100, 2), epochs=10, verbose=0)
# predictions = model.predict(df)
# df['Pred1'] = predictions[:, 0]
# df['Pred2'] = predictions[:, 1]
# fig = px.scatter_3d(df, x='Feature1', y='Feature2', z='Feature3', color='Pred1', title='3D Scatter з TensorFlow прогнозами')
# fig.show()

# ЗБЕРЕЖЕННЯ ГРАФІКІВ У СТАТИЧНИХ ТА ІНТЕРАКТИВНИХ ФОРМАТАХ
# df = pd.DataFrame({
#     'Category': ['A', 'B', 'C', 'D'],
#     'Values': [23, 17, 35, 29]
# })
# fig = px.bar(df, x='Category', y='Values', title='Стовпчаста діаграма для поділу та публікації')
# fig.write_html("bar_chart.html")
# fig.write_image("bar_chart.png")

# Використання Plotly Chart Studio для публікації графіків онлайн
# import plotly.express as px
# import pandas as pd
# import chart_studio
# import chart_studio.plotly as py

# chart_studio.tools.set_credentials_file(username='your_username', api_key='your_api_key')
# df = pd.DataFrame({
#     'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
#     'Sales': [1000, 1500, 800, 1200, 900]
# })
# fig = px.bar(df, x='City', y='Sales', title='Продажі за містами')
# py.plot(fig, filename='sales_by_city', auto_open=True)

# Створення інтерактивних веб-додатків з Dash
# import dash
# from dash import dcc, html
# from dash.dependencies import Input, Output
# import plotly.express as px
# import pandas as pd

# app = dash.Dash(__name__)
# df = pd.DataFrame({
#     'Month': ['January', 'February', 'March', 'April'],
#     'Sales': [5000, 7000, 6000, 8000],
#     'Expenses': [3000, 4000, 3500, 4500]
# })
# app.layout = html.Div([
#     html.H1("Дашборд Продажів та Витрат"),
#     dcc.Dropdown(
#         id='department-dropdown',
#         options=[
#             {'label': 'Продажі', 'value': 'Sales'},
#             {'label': 'Витрати', 'value': 'Expenses'}
#         ],
#         value='Sales',
#         clearable=False
#     ),
#     dcc.Graph(id='bar-chart')
# ])

# @app.callback(
#     Output('bar-chart', 'figure'),
#     [Input('department-dropdown', 'value')]
# )
# def update_chart(selected_metric):
#     fig = px.bar(df, x='Month', y=selected_metric, title=f'{selected_metric} за Місяцями')
#     return fig

# if __name__ == '__main__':
#     app.run(debug=True)

# Використання Plotly для вбудовування графіків у веб-сайти
# df = pd.DataFrame({
#     'Age': [25, 30, 35, 40, 45, 50, 55, 60],
#     'Income': [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000]
# })

# fig = px.scatter(df, x='Age', y='Income', trendline='ols', title='Зв’язок між віком та доходом')
# fig.write_html("age_income_scatter.html")
# fig.write_image("age_income_scatter.png")
# <iframe src="age_income_scatter.html" width="800" height="600"></iframe>

# df = pd.read_csv('data/sales_data.csv')
# fig = px.bar(df, x='Category', y='Sales', color='Region', title='Продажі за категоріями та регіонами')
# fig.write_html("sales_dashboard.html", include_plotlyjs='cdn', full_html=False)
# <html>
# <head>
#     <title>Дашборд Продажів</title>
#     <script src="<https://cdn.plot.ly/plotly-latest.min.js>"></script>
# </head>
# <body>
#     <h1>Інтерактивний Дашборд Продажів</h1>
#     <div id="plotly-div"></div>
#     <script>
#         fetch('sales_dashboard.html')
#             .then(response => response.text())
#             .then(html => {
#                 document.getElementById('plotly-div').innerHTML = html;
#             });
#     </script>
# </body>
# </html>


# Розробка інтерактивних дашбордів для аналізу реальних даних
# import dash
# from dash import dcc, html
# from dash.dependencies import Input, Output
# import plotly.express as px
# import pandas as pd

# app = dash.Dash(__name__)

# df = pd.read_csv('sales_data.csv')

# app.layout = html.Div([
#     html.H1("Інтерактивний Дашборд Продажів"),
#     html.Div([
#         html.Label("Виберіть Регіони:"),
#         dcc.Dropdown(
#             id='region-dropdown',
#             options=[{'label': region, 'value': region} for region in df['Region'].unique()],
#             value=df['Region'].unique().tolist(),
#             multi=True
#         )
#     ], style={'width': '48%', 'display': 'inline-block'}),
#     html.Div([
#         html.Label("Виберіть Продукти:"),
#         dcc.Dropdown(
#             id='product-dropdown',
#             options=[{'label': product, 'value': product} for product in df['Product'].unique()],
#             value=df['Product'].unique().tolist(),
#             multi=True
#         )
#     ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),
#     dcc.Graph(id='sales-graph'),
#     dcc.Graph(id='profit-graph')
# ])

# @app.callback(
#     [Output('sales-graph', 'figure'),
#      Output('profit-graph', 'figure')],
#     [Input('region-dropdown', 'value'),
#      Input('product-dropdown', 'value')]
# )
# def update_graphs(selected_regions, selected_products):
#     filtered_df = df[
#         df['Region'].isin(selected_regions) &
#         df['Product'].isin(selected_products)
#     ]
#     sales_fig = px.bar(filtered_df, x='Month', y='Sales', color='Region', title='Продажі за Місяцями')
#     profit_fig = px.line(filtered_df, x='Month', y='Profit', color='Product', title='Прибуток за Місяцями')
#     return sales_fig, profit_fig

# if __name__ == '__main__':
#     app.run(debug=True)

# import dash
# from dash import dcc, html
# from dash.dependencies import Input, Output, State
# import plotly.express as px
# import pandas as pd
# import io
# import base64

# app = dash.Dash(__name__)

# app.layout = html.Div([
#     html.H1("Дашборд з Завантаженням Даних"),
#     dcc.Upload(
#         id='upload-data',
#         children=html.Div([
#             'Перетягніть або ',
#             html.A('виберіть файли')
#         ]),
#         style={
#             'width': '100%',
#             'height': '60px',
#             'lineHeight': '60px',
#             'borderWidth': '1px',
#             'borderStyle': 'dashed',
#             'borderRadius': '5px',
#             'textAlign': 'center',
#             'margin': '10px'
#         },
#         multiple=False
#     ),
#     dcc.Graph(id='uploaded-graph')
# ])

# def parse_contents(contents, filename):
#     content_type, content_string = contents.split(',')
#     decoded = base64.b64decode(content_string)
#     try:
#         if 'csv' in filename:
#             df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
#         elif 'xls' in filename:
#             df = pd.read_excel(io.BytesIO(decoded))
#         else:
#             return None
#     except Exception:
#         return None
#     return df

# @app.callback(
#     Output('uploaded-graph', 'figure'),
#     [Input('upload-data', 'contents')],
#     [State('upload-data', 'filename')]
# )
# def update_output(contents, filename):
#     if contents is not None:
#         df = parse_contents(contents, filename)
#         if df is not None and 'X' in df.columns and 'Y' in df.columns:
#             fig = px.scatter(df, x='X', y='Y', title='Завантажений Графік')
#             return fig
#     return {}

# if __name__ == '__main__':
#     app.run(debug=True)