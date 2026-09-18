# Граф — це абстрактна структура даних,
# що складається з вузлів (вершин) (Nodes) та зв’язків між ними (ребер) (Edges)

# Ребра часто мають вагу, що може відображати силу
# зв'язку, відстань або інший показник, залежно від контексту застосування графа.

# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }

# graph_matrix = [
#     [0, 1, 1, 0, 0, 0],
#     [1, 0, 0, 1, 1, 0],
#     [1, 0, 0, 0, 0, 1],
#     [0, 1, 0, 0, 0, 0],
#     [0, 1, 0, 0, 0, 1],
#     [0, 0, 1, 0, 1, 0]
# ]


# class Graph:
#     def __init__(self):
#         self.adjacency: dict[str, list[str]] = {}

#     def add_vertex(self, vertex):
#         if vertex not in self.adjacency:
#             self.adjacency[vertex] = []

#     def add_edge(self, u, v, directed=False):
#         if u not in self.adjacency:
#             self.add_vertex(u)

#         if v not in self.adjacency:
#             self.add_vertex(v)

#         self.adjacency[u].append(v)
#         if not directed:
#             self.adjacency[v].append(u)

#     def get_neighbors(self, vertex):
#         return self.adjacency.get(vertex, [])

#     def __str__(self):
#         return "\n".join(f"{vertex}: {neighbors}" for vertex, neighbors in self.adjacency.items())


# g = Graph()
# g.add_edge('A', 'B')
# g.add_edge('A', 'C')
# g.add_edge('B', 'D')
# g.add_edge('C', 'D')
# g.add_edge('C', 'E')
# g.add_edge('E', 'F')
# g.add_edge('D', 'F')
# print("Graph representation (adjacency list):")
# print(g)

# ------------------------------------------------------------------------


# ЗАВДАННЯ 1
# Створіть клас Graph, який використовує
# список суміжності для представлення графа.
# Реалізуйте методи для додавання вершини та ребра.

# Початковий код:
# class Graph:
#     def __init__(self):
#         # Ініціалізуйте словник для зберігання списку суміжності
#         pass

#     def add_vertex(self, vertex):
#         # Якщо вершина відсутня у словнику, додайте її з порожнім списком
#         pass

#     def add_edge(self, u, v, directed=False):
#         # Додайте ребро від u до v
#         # Якщо граф не орієнтований, додайте ребро і від v до u
#         pass

# g = Graph()
# g.add_edge('A', 'B')
# g.add_edge('A', 'C')
# g.add_edge('B', 'D')
# g.add_edge('C', 'D')
# print("Список суміжності:")
# print(g.adjacency)


# ЗАВДАННЯ 2:
# Реалізуйте функцію to_adjacency_matrix(graph), яка
# приймає граф, представлений списком суміжності (словником),
# і повертає матрицю суміжності. Вершини повинні бути впорядковані за алфавітом.

# # Початковий код:
# def to_adjacency_matrix(graph):
#     # Отримайте список вершин, відсортований за алфавітом
#     # Ініціалізуйте матрицю розміром n x n, заповнену нулями
#     # Для кожного ребра встановіть відповідну позицію в матриці в 1
#     pass

# # Використовуйте граф g із завдання 1
# matrix = to_adjacency_matrix(g)
# print("Матриця суміжності:")
# for row in matrix:
#     print(row)


# Правильний код

# def to_adjacency_matrix(graph):
#     vertices = sorted(graph.adjacency.keys())
#     n = len(vertices)
#     matrix = [[0]*n for _ in range(n)]
#     index = {vertex: i for i, vertex in enumerate(vertices)}
#     for vertex, neighbors in graph.adjacency.items():
#         for neighbor in neighbors:
#             matrix[index[vertex]][index[neighbor]] = 1
#     return matrix

# matrix = to_adjacency_matrix(g)
# print("Матриця суміжності:")
# for row in matrix:
#     print(row)
# ----------------------------------------------------------------

# https://edu.goiteens.com/learn/18816179/24459685/46011038/training?blockId=47003820

# НЕОРІЄНТОВАНІ ГРАФИ
# Ребра не мають напрямку. Зв'язок між будь-якими
# двома вершинами відбувається в обох напрямках.


# ОРІЄНТОВАНІ ГРАФИ (ДІАГРАМИ)
# Ребра мають напрямок. Кожне ребро вказує від однієї
# вершини до іншої, що важливо для моделювання асиметричних відносин.


# Зважені графи
# Ребра мають асоційовані числові значення (ваги), що можуть
# представляти відстані, витрати або інші показники. Це
# дозволяє розглядати оптимізаційні задачі (наприклад,
# знаходження найкоротшого шляху).


# НЕВЗВАЖЕНІ ГРАФИ
# Ребра не мають ваг, і зв'язки між вершинами
# розглядаються як рівнозначні


# Циклічні графи
# Містять хоча б один цикл, тобто існує шлях, що
# починається і закінчується в одній вершині, пройшовши через інші.


# Ациклічні графи
# Не містять циклів. Особливий випадок — орієнтовані ациклічні
# графи (DAG), які широко використовуються для моделювання
# залежностей (наприклад, у плануванні задач або аналізі процесів).

# ---------------------------------------------------------------------


# ЗАВДАННЯ 1
# Реалізуйте клас для неорієнтованого графа
# з вагами ребер. Створіть методи для додавання
# вершин і ребер із зазначенням ваги ребра.

# Початковий код:
# class WeightedGraph:
#     def __init__(self):
#         # Ініціалізуйте словник для зберігання списку суміжності, де кожен елемент – (сусід, вага)
#         pass

#     def add_vertex(self, vertex):
#         # Додайте вершину, якщо вона ще не присутня
#         pass

#     def add_edge(self, u, v, weight):
#         # Додайте ребро з вагою weight від u до v і навпаки (неорієнтований)
#         pass
# wg = WeightedGraph()
# wg.add_edge('A', 'B', 3)
# wg.add_edge('A', 'C', 5)
# wg.add_edge('B', 'D', 2)
# print("Ваговий неорієнтований граф (Adjacency List):")
# print(wg.adjacency)


# Правильний код
# class WeightedGraph:
#     def __init__(self):
#         self.adjacency = {}

#     def add_vertex(self, vertex):
#         if vertex not in self.adjacency:
#             self.adjacency[vertex] = []

#     def add_edge(self, u, v, weight):
#         if u not in self.adjacency:
#             self.add_vertex(u)
#         if v not in self.adjacency:
#             self.add_vertex(v)
#         self.adjacency[u].append((v, weight))
#         self.adjacency[v].append((u, weight))

# wg = WeightedGraph()
# wg.add_edge('A', 'B', 3)
# wg.add_edge('A', 'C', 5)
# wg.add_edge('B', 'D', 2)
# print("Ваговий неорієнтований граф (Adjacency List):")
# print(wg.adjacency)


# ЗАВДАННЯ 2
# Реалізуйте клас для орієнтованого графа.
# Створіть методи для додавання вершин і
# ребер із зазначенням напрямку.

# Початковий код:
# class DirectedGraph:
#     def __init__(self):
#         # Ініціалізуйте словник для представлення графа
#         pass

#     def add_vertex(self, vertex):
#         # Додайте вершину, якщо вона відсутня
#         pass

#     def add_edge(self, u, v):
#         # Додайте орієнтоване ребро від u до v
#         pass

# dg = DirectedGraph()
# dg.add_edge('A', 'B')
# dg.add_edge('A', 'C')
# dg.add_edge('B', 'D')
# print("Орієнтований граф (Adjacency List):")
# print(dg.adjacency)


# Правильний код
# class DirectedGraph:
#     def __init__(self):
#         self.adjacency = {}

#     def add_vertex(self, vertex):
#         if vertex not in self.adjacency:
#             self.adjacency[vertex] = []

#     def add_edge(self, u, v):
#         if u not in self.adjacency:
#             self.add_vertex(u)
#         if v not in self.adjacency:
#             self.add_vertex(v)
#         self.adjacency[u].append(v)

# dg = DirectedGraph()
# dg.add_edge('A', 'B')
# dg.add_edge('A', 'C')
# dg.add_edge('B', 'D')
# print("Орієнтований граф (Adjacency List):")
# print(dg.adjacency)


# ЗАВДАННЯ 3
# Реалізуйте функцію, що приймає граф у вигляді
# списку суміжності (словник) та повертає
# матрицю суміжності. Вершини впорядковано за алфавітом.

# Початковий код:
# def to_adjacency_matrix(graph):
#     # Отримайте впорядкований список вершин
#     # Ініціалізуйте матрицю розміром n x n, заповнену нулями
#     # Для кожного ребра встановіть відповідне значення (1)
#     pass

# matrix = to_adjacency_matrix(dg.adjacency)
# print("Матриця суміжності:")
# for row in matrix:
#     print(row)


# # Правильний код
# def to_adjacency_matrix(graph):
#     vertices = sorted(graph.keys())
#     n = len(vertices)
#     matrix = [[0] * n for _ in range(n)]
#     index = {vertex: i for i, vertex in enumerate(vertices)}
#     for vertex, neighbors in graph.items():
#         for neighbor in neighbors:
#             matrix[index[vertex]][index[neighbor]] = 1
#     return matrix

# matrix = to_adjacency_matrix(dg.adjacency)
# print("Матриця суміжності:")
# for row in matrix:
#     print(row)


# ЗАВДАННЯ 4
# Реалізуйте клас MultiGraph, який дозволяє додавати кілька
# ребер між двома вершинами. Представлення здійснюється
# через список суміжності, де значення ребра може повторюватися.

# Початковий код:
# class MultiGraph:
#     def __init__(self):
#         # Ініціалізуйте словник для представлення мультиграфа
#         pass

#     def add_vertex(self, vertex):
#         # Додайте вершину, якщо її немає
#         pass

#     def add_edge(self, u, v):
#         # Додайте ребро від u до v (без видалення повторень)
#         pass

# mg = MultiGraph()
# mg.add_edge('A', 'B')
# mg.add_edge('A', 'B')
# mg.add_edge('B', 'C')
# print("Мультиграф (Adjacency List):")
# print(mg.adjacency)


# Правильний код
# class MultiGraph:
#     def __init__(self):
#         self.adjacency = {}

#     def add_vertex(self, vertex):
#         if vertex not in self.adjacency:
#             self.adjacency[vertex] = []

#     def add_edge(self, u, v):
#         if u not in self.adjacency:
#             self.add_vertex(u)
#         if v not in self.adjacency:
#             self.add_vertex(v)
#         self.adjacency[u].append(v)
#         self.adjacency[v].append(u)

# mg = MultiGraph()
# mg.add_edge('A', 'B')
# mg.add_edge('A', 'B')
# mg.add_edge('B', 'C')
# print("Мультиграф (Adjacency List):")
# print(mg.adjacency)


# ЗАВДАННЯ 5
# Реалізуйте клас WeightedDirectedGraph, який
# представляє орієнтований граф із вагами ребер.
# Реалізуйте методи для додавання вершин і ребер із зазначенням ваги.

# Початковий код:
# class WeightedDirectedGraph:
#     def __init__(self):
#         # Ініціалізуйте словник для представлення графа
#         pass

#     def add_vertex(self, vertex):
#         # Додайте вершину, якщо вона відсутня
#         pass

#     def add_edge(self, u, v, weight):
#         # Додайте орієнтоване ребро від u до v з вагою
#         pass

# # Тестові дані:
# wdg = WeightedDirectedGraph()
# wdg.add_edge('A', 'B', 4)
# wdg.add_edge('A', 'C', 6)
# wdg.add_edge('B', 'D', 5)
# print("Зважений орієнтований граф (Adjacency List):")
# print(wdg.adjacency)


# Правильний код
# class WeightedDirectedGraph:
#     def __init__(self):
#         self.adjacency = {}

#     def add_vertex(self, vertex):
#         if vertex not in self.adjacency:
#             self.adjacency[vertex] = []

#     def add_edge(self, u, v, weight):
#         if u not in self.adjacency:
#             self.add_vertex(u)
#         if v not in self.adjacency:
#             self.add_vertex(v)
#         self.adjacency[u].append((v, weight))

# wdg = WeightedDirectedGraph()
# wdg.add_edge('A', 'B', 4)
# wdg.add_edge('A', 'C', 6)
# wdg.add_edge('B', 'D', 5)
# print("Зважений орієнтований граф (Adjacency List):")
# print(wdg.adjacency)


# ЗАВДАННЯ 6
# Створіть клас EdgeListGraph, який зберігає
# граф як список ребер. Реалізуйте метод для
# перетворення цього представлення у список суміжності.

# Початковий код:
# class EdgeListGraph:
#     def __init__(self):
#         # Ініціалізуйте список для зберігання ребер
#         pass

#     def add_edge(self, u, v):
#         # Додайте ребро як кортеж (u, v) до списку ребер
#         pass

# def edge_list_to_adjacency(edge_list):
#     # Отримайте всі унікальні вершини з edge_list
#     # Створіть словник, де кожна вершина має порожній список
#     # Для кожного ребра (u, v) додайте v до списку сусідів u, і для неорієнтованого графа – і u до списку сусідів v
#     pass

# elg = EdgeListGraph()
# elg.add_edge('A', 'B')
# elg.add_edge('A', 'C')
# elg.add_edge('B', 'D')
# adjacency = edge_list_to_adjacency(elg.edge_list)
# print("Список суміжності з edge list:")
# print(adjacency)


# Правильний код
# class EdgeListGraph:
#     def __init__(self):
#         self.edge_list = []

#     def add_edge(self, u, v):
#         self.edge_list.append((u, v))

# def edge_list_to_adjacency(edge_list):
#     vertices = set()
#     for u, v in edge_list:
#         vertices.add(u)
#         vertices.add(v)
#     adjacency = {vertex: [] for vertex in vertices}
#     for u, v in edge_list:
#         adjacency[u].append(v)
#         adjacency[v].append(u)
#     return adjacency

# elg = EdgeListGraph()
# elg.add_edge('A', 'B')
# elg.add_edge('A', 'C')
# elg.add_edge('B', 'D')
# adjacency = edge_list_to_adjacency(elg.edge_list)
# print("Список суміжності з edge list:")
# print(adjacency)
# -------------------------------------------------------


# ЗАВДАННЯ 1
# Реалізуйте два графи за допомогою класу Graph:
# один орієнтований та один неорієнтований.
# Використовуйте однакові вершини та ребра
# для обох. Виведіть списки суміжності для обох
# графів, щоб показати різницю у представленні.

# Початковий код:
# Створіть два об’єкти класу Graph: oriented_graph та undirected_graph
# Для кожного додайте вершини A, B, C, D
# Додайте ребра: A -> B, B -> C, C -> D, D -> A
# Для undirected_graph використовуйте неорієнтоване додавання ребер
# Виведіть списки суміжності для обох графів
# ---------------------------------------------------------

# Розглянути

# Завдання 1
# Реалізуйте функцію is_connected(graph), яка перевіряє,
# чи є граф зв’язним. Використовуйте BFS з використанням
# черги (FIFO) для обходу всіх вершин, починаючи з довільної.
# from collections import deque

# def is_connected(graph):
#     if not graph.adjacency:
#         return True
#     start = next(iter(graph.adjacency))
#     visited = set([start])
#     queue = deque([start])
#     while queue:
#         vertex = queue.popleft()
#         for neighbor in graph.adjacency[vertex]:
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 queue.append(neighbor)
#     return len(visited) == len(graph.adjacency)

# print("Граф зв'язний?", is_connected(g))


# ЗАВДАННЯ 2
# Реалізуйте функцію dfs(graph, start), яка виконує
# глибокий пошук (DFS) у графі, представленому списком
# суміжності. Функція повинна повертати список вершин у порядку обходу.

# def dfs(graph, start):
#     visited = set()
#     stack = [start]
#     result = []
#     while stack:
#         vertex = stack.pop()
#         if vertex not in visited:
#             visited.add(vertex)
#             result.append(vertex)
#             stack.extend(reversed(graph.adjacency[vertex]))
#     return result

# print("DFS обход:", dfs(dg, 'A'))