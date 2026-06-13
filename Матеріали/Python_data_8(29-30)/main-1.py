import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# df = px.data.gapminder()

# fig = px.scatter(
#     df[df['year'] == 2007],
#     x="gdpPercap",
#     y="lifeExp",
#     color="continent",
#     size="pop",
#     hover_name="country",
#     log_x=True,
#     title="Взаємозв'язок між ВВП і тривалістю життя (2007 р.)"
# )
# fig.show()


# df = pd.DataFrame({
#     'date': pd.date_range('2023-01-01', periods=7, freq='D'),
#     'sales': [100, 120, 90, 130, 150, 170, 160]
# })
# fig = px.line(df, x='date', y='sales', title='Продажі за тиждень')
# fig.show()

# values = np.random.normal(loc=50, scale=10, size=1000)
# df_values = pd.DataFrame({'value': values})
# fig = px.histogram(df_values, x='value', nbins=20, title='Розподіл випадкових значень')
# fig.show()

# df_categories = pd.DataFrame({
#     'category': ['A', 'B', 'C', 'D'],
#     'amount': [30, 45, 15, 10]
# })
# fig = px.pie(df_categories, names='category', values='amount', title='Співвідношення категорій')
# fig.show()

# title
#     Опис: задає заголовок усієї фігури (діаграми).
#     Приклад: title="Продажі за місяць"
# xaxis_title / yaxis_title
#     Опис: встановлює назви для осей X та Y відповідно.
#     Приклад: xaxis_title="Дата", yaxis_title="Кількість замовлень"
# labels (у модулі plotly.express)
#     Опис: словник, що дозволяє перейменовувати колонки DataFrame у підписах осей та легенд.
#     Приклад: labels={"sales": "Продажі", "date": "Дата"}
# layout
#     Опис: об’єкт або словник, у якому містяться детальні налаштування розміщення елементів, шрифтів, кольорів фону, тощо.
#     Приклад: fig.update_layout(width=800, height=600, paper_bgcolor='lightgray')
# legend
#     Опис: параметри керування легендою — позиція, орієнтація, шрифт.
#     Приклад: fig.update_layout(legend=dict(x=0.1, y=1.1))
# color_discrete_sequence / color_continuous_scale
#     Опис: задає кольорові палітри для категорійних або неперервних даних.
#     Приклад: color_discrete_sequence=["red", "green", "blue"]
# markers / marker_size / marker_color
#     Опис: стосується точок або стовпчиків; керує формою, кольором і розміром маркерів (у точкових діаграмах) чи шириною/кольором стовпців.
#     Прилад: fig.update_traces(marker=dict(size=12, color='orange'))
# hover_data / hover_name
#     Опис: які поля показувати при наведенні курсора на точку / стовпець, та яке поле використовувати як заголовок у ховер-картці.
#     Приклад: hover_data=["sales", "region"], hover_name="product_name"
# range_x / range_y
#     Опис: дозволяє вручну задати діапазон осей X і Y (мінімальне й максимальне значення).
#     Приклад: range_x=[0, 100]
# template
#     Опис: використання заздалегідь заданих тем (наприклад, "plotly_white", "ggplot2") для загального стилю.
#     Приклад: template="plotly_white"

# df = pd.DataFrame({
#     "month": ["Січень", "Лютий", "Березень", "Квітень"],
#     "sales": [100, 150, 130, 180]
# })
# fig = px.line(
#     df,
#     x="month",
#     y="sales",
#     title="Продажі за перший квартал",
#     labels={"month": "Місяць", "sales": "Кількість продажів"}
# )
# fig.update_layout(
#     width=700,
#     height=400,
#     paper_bgcolor="white",
#     plot_bgcolor="whitesmoke",
#     template="plotly_white",
#     title_font=dict(size=20)
# )
# fig.update_yaxes(range=[0, 200])
# fig.show()

# df2 = pd.DataFrame({
#     "region": ["Північ", "Південь", "Захід", "Схід", "Центр", "Київ"],
#     "profit": [300, 400, 100, 200, 350, 500],
#     "category": ["A", "B", "A", "B", "A", "C"]
# })
# fig2 = px.bar(
#     df2,
#     x="region",
#     y="profit",
#     color="category",
#     barmode="group",
#     title="Прибуток за регіонами",
#     labels={"region": "Регіон", "profit": "Прибуток, $", "category": "Категорія"},
#     # color_discrete_sequence=["#FF6F61", "#6B5B95", "#1f77b4"]
# )
# fig2.update_layout(
#     legend=dict(
#         x=0.02,
#         y=1.0,
#         title="Категорія",
#         bgcolor="rgba(255,255,255,0.8)"
#     )
# )
# fig2.update_traces(
#     marker=dict(line=dict(width=1, color="black"))
# )
# fig2.update_layout(
#     colorway=["#FF6F61", "#6B5B95", "#1f77b4"]
# )
# fig2.show()

# Щоб змінити розмір шрифту саме для заголовка
# fig.update_layout(
#     title=dict(
#         text="Прибуток за регіонами",
#         font=dict(
#             size=24  # Встановлюємо розмір шрифту
#         )
#     )
# )
# fig.update_layout(title_font_size=24)


# ЗАВДАННЯ 1
# Ви маєте Python-оточення (наприклад, Jupyter Notebook або Python 3.x в IDE).
# Завдання:
# Встановіть бібліотеку Plotly
# Створіть новий Python-файл (або Jupyter-ноутбук).
# Імпортуйте Plotly і виведіть його версію:
# print(plotly.__version__)
# Запустіть код і переконайтеся, що помилок немає, а версія Plotly виводиться у консолі.

# ЗАВДАННЯ 2. 
# Дні тижня: ['Понеділок', 'Вівторок', 'Середа', 'Четвер', 'П'ятниця']
# Кількість відвідувачів вашого веб-сайту: [120, 150, 90, 200, 180]
# Завдання:
# Створіть лінійну діаграму, де вісь X — це дні тижня, а вісь Y — кількість відвідувачів.
# Додайте заголовок «Відвідуваність веб-сайту за робочий тиждень».
# Використайте бібліотеку plotly.express і функцію px.line.
# Приклад початкового коду (допишіть, де потрібно):
# import plotly.express as px
# days = [...]
# visitors = [...]
# fig = px.line(x=days, y=visitors, title="...")
# fig.show()

# ЗАВДАННЯ 3.
# Випадкові значення (можна згенерувати 100 чисел) від 0 до 50, наприклад:
# import numpy as np
# np.random.seed(42)
# data = np.random.randint(0, 50, 100)
# Завдання:
# Створіть гістограму (px.histogram), де x=data.
# Додайте заголовок «Розподіл випадкових значень».
# Спробуйте змінити параметр nbins (наприклад, 10 або 20), щоб побачити різницю.

# ЗАВДАННЯ 4.
# Категорії товарів: ['Одяг', 'Взуття', 'Аксесуари', 'Інше']
# Продажі у відсотках: [40, 25, 20, 15]
# Завдання:
# Використайте px.pie, де names=... і values=....
# Додайте заголовок «Структура продажів».
# Спробуйте використати інший параметр кольорів (color_discrete_sequence) або шаблон (template), щоб змінити вигляд.
# Переконайтеся, що при наведенні курсора відображаються назви категорій і їх відсоткові частки.

# ЗАВДАННЯ 5.
# Час (години доби): [0, 1, 2, 3, ..., 23] (тобто 24 значення).
# Температура повітря (можна згенерувати випадково або задати руками).
# Завдання:
# Побудуйте лінійну діаграму px.line.
# Задайте розмір (ширину і висоту) фігури, колір фону, та тему (template="plotly_dark" або іншу).
# Додайте назви осей: «Година», «Температура (°C)».
# Обмежте вісь Y (наприклад, від -5 до 35, якщо це має сенс).
# Приклад ключових методів:
# fig.update_layout(width=800, height=400, paper_bgcolor="lightgray", ...)
# fig.update_yaxes(range=[-5, 35])

# ЗАВДАННЯ 6.
# Дати (наприклад, 7 днів): ['2023-01-01', '2023-01-02', ..., '2023-01-07']
# Дані по трьох серіях (A, B, C), наприклад:
# Серія А: [10, 12, 9, 14, 20, 18, 22]
# Серія B: [5, 7, 3, 10, 12, 11, 15]
# Серія C: [8, 6, 10, 9, 13, 17, 19]
# Завдання:
# Створіть go.Figure().
# Додайте 3 траси go.Scatter, де кожна має свій колір, mode='lines+markers' та назву серії в легенді.
# Додайте:
# Заголовок «Продажі трьох відділів за тиждень».
# Ось X з підписом «Дата», ось Y з підписом «Шт.».
# Легенду, розміщену вгорі (наприклад, x=0.1, y=1.2).
# Налаштуйте фон діаграми (paper_bgcolor і plot_bgcolor) та шрифт заголовка.
# import plotly.graph_objects as go
# dates = ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06', '2023-01-07']
# series_a = [10, 12, 9, 14, 20, 18, 22]
# series_b = [5, 7, 3, 10, 12, 11, 15]
# series_c = [8, 6, 10, 9, 13, 17, 19]
# fig = go.Figure()
# fig.add_trace(go.Scatter(
#     x=dates, 
#     y=series_a, 
#     mode='lines+markers', 
#     name='Серія А',
#     line=dict(color='#FF6F61', width=3),
#     marker=dict(size=8)
# ))
# fig.add_trace(go.Scatter(
#     x=dates, 
#     y=series_b, 
#     mode='lines+markers', 
#     name='Серія B',
#     line=dict(color='#6B5B95', width=3),
#     marker=dict(size=8)
# ))
# fig.add_trace(go.Scatter(
#     x=dates, 
#     y=series_c, 
#     mode='lines+markers', 
#     name='Серія C',
#     line=dict(color='#88B04B', width=3),
#     marker=dict(size=8)
# ))
# fig.update_layout(
#     title=dict(
#         text="Продажі трьох відділів за тиждень",
#         font=dict(
#             family="Arial, sans-serif",
#             size=22,
#             color="#333333"
#         )
#     ),
#     xaxis=dict(title="Дата", gridcolor="#E5E5E5"),
#     yaxis=dict(title="Шт.", gridcolor="#E5E5E5"),
#     legend=dict(
#         orientation="h",
#         x=0.1,
#         y=1.2,
#         bgcolor="rgba(255, 255, 255, 0.5)"
#     ),
#     paper_bgcolor="#F8F9FA",
#     plot_bgcolor="#FFFFFF"
# )
# fig.show()

# ЗАВДАННЯ 7
# Типи витрат: ['Оренда', 'Зарплата', 'Маркетинг', 'Інше']
# Суми: [3000, 4500, 1500, 500]
# Завдання:
# Побудуйте px.pie, де names=..., values=....
# Використайте fig.update_traces(...), щоб «відсунути» (pull) один сегмент діаграми (наприклад, найбільший сегмент) для акценту.
# Додайте заголовок «Структура витрат».
# Налаштуйте підписи textinfo='label+percent' і перевірте, як виглядають підказки.
# data = {
#     'Тип витрат': ['Оренда', 'Зарплата', 'Маркетинг', 'Інше'],
#     'Сума': [3000, 4500, 1500, 500]
# }
# df = pd.DataFrame(data)
# fig = px.pie(
#     df, 
#     names='Тип витрат', 
#     values='Сума', 
#     title='Структура витрат'
# )
# fig.update_traces(
#     textinfo='label+percent',
#     pull=[0, 0.1, 0, 0],
#     marker=dict(line=dict(color='#FFFFFF', width=2))
# )
# fig.update_traces(
#     hovertemplate="<b>%{label}</b><br>Сума: %{value} $<br>Частка: %{percent}<extra></extra>"
# )
# fig.show()


# МЕХАНІЗМИ BUTTONS І DROPDOWNS У PLOTLY
# Приклад 1.
# можливість змінювати дані на графіку
# x = [1, 2, 3, 4]
# y1 = [10, 20, 15, 25]
# y2 = [30, 10, 40, 5]
# fig = go.Figure()
# fig.add_trace(go.Scatter(x=x, y=y1, mode='lines', name='Серія 1'))
# fig.update_layout(
#     updatemenus=[
#         dict(
#             type="buttons",
#             buttons=[
#                 dict(
#                     label="Замінити дані",
#                     method="update",
#                     args=[{"y": [y2]}]
#                 )
#             ],
#             x=0.1,
#             y=1.15
#         )
#     ]
# )
# fig.show()

# Приклад 2.
# перемикатися між кількома наборами даних
# x = [1, 2, 3, 4]
# yA = [10, 15, 9, 20]
# yB = [5, 25, 10, 40]
# fig = go.Figure()
# fig.add_trace(go.Scatter(x=x, y=yA, mode='markers+lines', name='A'))
# fig.update_layout(
#     updatemenus=[
#         dict(
#             type="buttons",
#             buttons=[
#                 dict(
#                     label="Показати A",
#                     method="update",
#                     args=[{"y": [yA]}]
#                 ),
#                 dict(
#                     label="Показати B",
#                     method="update",
#                     args=[{"y": [yB]}]
#                 )
#             ],
#             x=0, y=1.2
#         )
#     ]
# )
# fig.show()

# Приклад 3.
# одну серію, іншу, або обидві одночасно
# x = [1, 2, 3, 4]
# trace1 = go.Scatter(x=x, y=[10, 15, 12, 18], mode='lines', name='Лінія 1')
# trace2 = go.Scatter(x=x, y=[30, 10, 40, 5], mode='lines', name='Лінія 2')
# fig = go.Figure(data=[trace1, trace2])
# fig.update_layout(
#     updatemenus=[
#         dict(
#             type="dropdown",
#             x=0.0,
#             y=1.15,
#             showactive=True,
#             active=0,
#             buttons=[
#                 dict(
#                     label="Показати обидві",
#                     method="update",
#                     args=[{"visible": [True, True]}]
#                 ),
#                 dict(
#                     label="Тільки Лінія 1",
#                     method="update",
#                     args=[{"visible": [True, False]}]
#                 ),
#                 dict(
#                     label="Тільки Лінія 2",
#                     method="update",
#                     args=[{"visible": [False, True]}]
#                 )
#             ]
#         )
#     ]
# )
# fig.show()

# Приклад 4.
# між різними типами графіків
# x = [1, 2, 3, 4]
# values = [10, 20, 15, 25]
# fig = go.Figure(data=[go.Scatter(x=x, y=values, mode='lines', name='Лінія')])
# fig.update_layout(
#     updatemenus=[
#         dict(
#             type="buttons",
#             buttons=[
#                 dict(
#                     label="Лінія",
#                     method="restyle",
#                     args=[{"type": "scatter", "mode": "lines"}]
#                 ),
#                 dict(
#                     label="Точки",
#                     method="restyle",
#                     args=[{"type": "scatter", "mode": "markers"}]
#                 ),
#                 dict(
#                     label="Стовпчики",
#                     method="restyle",
#                     args=[{"type": "bar"}]
#                 )
#             ],
#             x=0.0,
#             y=1.2
#         )
#     ]
# )
# fig.show()

# Приклад 5.
# змінювати кольори елементів графіка
# x = [10, 20, 30, 40, 50]
# y = [5, 15, 25, 35, 45]
# fig = go.Figure(data=[go.Scatter(x=x, y=y, mode="markers", marker=dict(size=10, color="blue"))])
# fig.update_layout(
#     updatemenus=[
#         dict(
#             type="dropdown",
#             x=0.0, y=1.15,
#             buttons=[
#                 dict(
#                     label="Синій",
#                     method="restyle",
#                     args=[{"marker.color": "blue"}]
#                 ),
#                 dict(
#                     label="Зелений",
#                     method="restyle",
#                     args=[{"marker.color": "green"}]
#                 ),
#                 dict(
#                     label="Червоний",
#                     method="restyle",
#                     args=[{"marker.color": "red"}]
#                 ),
#             ]
#         )
#     ]
# )
# fig.show()

# Приклад 6.
# можна використовувати кнопки, які оновлюють і дані, і параметри оформлення
# x = [1, 2, 3, 4]
# sales_2022 = [100, 150, 130, 180]
# sales_2023 = [120, 160, 140, 200]
# fig = go.Figure(data=[go.Bar(x=x, y=sales_2022, name="2022")])
# fig.update_layout(title="Продажі за 2022 р.")
# fig.update_layout(
#     updatemenus=[
#         dict(
#             type="buttons",
#             x=0, y=1.2,
#             buttons=[
#                 dict(
#                     label="2022",
#                     method="update",
#                     args=[
#                         {"y": [sales_2022]},
#                         {"title.text": "Продажі за 2022 р."}
#                     ]
#                 ),
#                 dict(
#                     label="2023",
#                     method="update",
#                     args=[
#                         {"y": [sales_2023]},
#                         {"title.text": "Продажі за 2023 р."}
#                     ]
#                 )
#             ]
#         )
#     ]
# )
# fig.show()

# Приклад 7
# змінювати кольорові шкали на тепловій карті
# np.random.seed(42)
# z_data = np.random.rand(5, 5) * 100
# x_labels = ['A', 'B', 'C', 'D', 'E']
# y_labels = ['Показник 1', 'Показник 2', 'Показник 3', 'Показник 4', 'Показник 5']
# fig = go.Figure(data=go.Heatmap(
#     z=z_data,
#     x=x_labels,
#     y=y_labels,
#     colorscale="Viridis",
#     colorbar=dict(title="Значення")
# ))
# fig.update_layout(
#     updatemenus=[
#         dict(
#             type="dropdown",
#             x=0, y=1.1,
#             buttons=[
#                 dict(
#                     label="Viridis",
#                     method="restyle",
#                     args=[{"colorscale": "Viridis"}]
#                 ),
#                 dict(
#                     label="Cividis",
#                     method="restyle",
#                     args=[{"colorscale": "Cividis"}]
#                 ),
#                 dict(
#                     label="Plasma",
#                     method="restyle",
#                     args=[{"colorscale": "Plasma"}]
#                 )
#             ]
#         )
#     ]
# )
# fig.show()

# Приклад 8
# перемикатися між різними фільтрами даних у DataFrame
# df = px.data.gapminder()
# df_filtered = df[df['year'].isin([1952, 2007])].sort_values(by='year')
# fig = px.scatter(
#     df_filtered,
#     x="gdpPercap",
#     y="lifeExp",
#     animation_frame="year",
#     animation_group="country",
#     hover_name="country",
#     color="continent",
#     size="pop",
#     log_x=True,
#     title="Динаміка розвитку країн",
#     labels={"gdpPercap": "ВВП на душу населення", "lifeExp": "Тривалість життя"},
#     size_max=55
# )
# fig.show()


# ЗМІНА ТЕМ, КОЛЬОРІВ, СТИЛІВ ШРИФТІВ
# Приклад 1
# побудувати лінійну діаграму з кастомним стилем і темою
# x_values = [1, 2, 3, 4, 5]
# y_values = [3, 10, 5, 8, 12]
# fig = px.line(
#     x=x_values,
#     y=y_values,
#     title="Лінійна діаграма з темою plotly_white",
#     template="plotly_white"
# )
# fig.update_layout(
#     width=700,
#     height=400,
#     font=dict(family="Arial", size=14, color="black"),
#     paper_bgcolor="white",
#     plot_bgcolor="whitesmoke"
# )
# fig.show()

# Приклад 2
# Для візуалізації стовпчастих даних спочатку
# categories = ["A", "B", "C", "D"]
# values = [10, 25, 15, 30]
# fig = px.bar(
#     x=categories,
#     y=values,
#     title="Стовпчаста діаграма з ggplot2",
#     template="ggplot2"
# )
# fig.update_layout(
#     # width=600,
#     # height=400,
#     font=dict(family="Verdana", size=12, color="navy")
# )
# fig.show()

# Приклад 3
# завантажуємо дані gapminder і відбираємо записи для року 2007 та континенту "Asia".
# df = px.data.gapminder().query("year == 2007 and continent == 'Asia'")
# fig = px.pie(
#     df,
#     values="pop",
#     names="country",
#     title="Кругова діаграма у темі plotly_dark",
#     template="plotly_dark"
# )
# fig.update_layout(
#     # width=700,
#     # height=500,
#     font=dict(family="Courier New", size=16, color="white")
# )
# fig.show()

# Приклад 4
# z = np.random.randint(0, 100, (6, 6))
# fig = go.Figure(
#     data=[go.Heatmap(z=z, colorscale="Viridis")]
# )
# fig.update_layout(
#     title="Теплова мапа з Viridis",
#     template="seaborn",
#     width=600,
#     height=500,
#     font=dict(family="Times New Roman", size=14, color="#333"),
#     paper_bgcolor="#fafafa",
#     plot_bgcolor="#eeeeee"
# )
# fig.show()