# Зв’язний граф — це граф, у якому існує шлях між будь-якою парою вершин.

# def dfs(graph, start, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)
#     for neighbor in graph[start]:
#         if neighbor not in visited:
#             dfs(graph, neighbor, visited)
#     return visited

# def is_connected(graph):
#     start_vertex = next(iter(graph))
#     visited = dfs(graph, start_vertex)
#     return len(visited) == len(graph)

# graph_connected = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D'],
#     'C': ['A', 'D'],
#     'D': ['B', 'C']
# }
# print("Граф 1 зв'язаний:", is_connected(graph_connected))

# graph_disconnected = {
#     'A': ['B'],
#     'B': ['A'],
#     'C': ['D'],
#     'D': ['C']
# }
# print("Граф 2 зв'язаний:", is_connected(graph_disconnected))


# ---------------------------------------------------------
# Цикл у графі — це послідовність вершин, починаючи з однієї вершини і повертаючись до неї,

# def dfs_cycle(graph, node, visited, rec_stack):
#     visited.add(node)
#     rec_stack.add(node)
#     for neighbor in graph.get(node, []):
#         if neighbor not in visited:
#             if dfs_cycle(graph, neighbor, visited, rec_stack):
#                 return True
#         elif neighbor in rec_stack:
#             return True
#     rec_stack.remove(node)
#     return False

# def has_cycle(graph):
#     visited = set()
#     rec_stack = set()
#     for node in graph:
#         if node not in visited:
#             if dfs_cycle(graph, node, visited, rec_stack):
#                 return True
#     return False

# Приклад орієнтованого графа з циклом:
# Цикл: A -> B -> C -> A
# graph_with_cycle = {
#     'A': ['B'],
#     'B': ['C'],
#     'C': ['A'],
#     'D': ['E'],
#     'E': []
# }
# print("Граф 1 містить цикл:", has_cycle(graph_with_cycle))

# Приклад орієнтованого графа без циклів:
# graph_without_cycle = {
#     'A': ['B', 'C'],
#     'B': ['D'],
#     'C': ['D'],
#     'D': []
# }
# # print("Граф 2 містить цикл:", has_cycle(graph_without_cycle))

# ---------------------------------------------------------


# необхідно знайти всі можливі маршрути між двома точками (вузлами) у графі
#    A
#   / \\
#  B   C
#   \\   \\
#    D---E

# def dfs_all_paths(graph, current, destination, path, all_paths):
#     path.append(current)
#     if current == destination:
#         all_paths.append(list(path))
#     else:
#         for neighbor in graph.get(current, []):
#             if neighbor not in path:
#                 dfs_all_paths(graph, neighbor, destination, path, all_paths)
#     path.pop()

# def find_all_paths(graph, start, end):
#     all_paths = []
#     dfs_all_paths(graph, start, end, [], all_paths)
#     return all_paths


# graf = {
#     "A": ["B", "C"],
#     "B": ["A", "D"],
#     "C": ["A", "E"],
#     "D": ["B", "E"],
#     "E": ["C", "D"]
# }

# print(find_all_paths(graf, "A", "D"))


# ---------------------------------------------------------


# Точки розриву (або критичні вузли) — це такі вузли
# неорієнтованого графа, видалення яких збільшує кількість зв’язних компонент

# discovery time (disc): момент часу, коли вузол вперше відвіданий,
# low value (low): найменший discovery time, до якого можна дістатися з поточного вузла, враховуючи зворотні ребра.

# Напишемо функцію find_articulation_points(graph) ,
# яка знаходить точки розриву (articulation points) у неорієнтованому графі, використовуючи алгоритм DFS.

# def find_articulation_points(graph):
#     time = 0
#     disc = {}
#     low = {}
#     parent = {}
#     ap = set()
#     def dfs(u):
#         nonlocal time
#         children = 0
#         disc[u] = low[u] = time
#         time += 1

#         for v in graph[u]:
#             if v not in disc:
#                 parent[v] = u
#                 children += 1
#                 dfs(v)
#                 low[u] = min(low[u], low[v])
#                 if u in parent and low[v] >= disc[u]:
#                     ap.add(u)
#             elif v != parent.get(u, None):
#                 low[u] = min(low[u], disc[v])
#         if u not in parent and children > 1:
#             ap.add(u)

#     for u in graph:
#         if u not in disc:
#             dfs(u)

#     return ap


# Код алгоритму Тарʼяну:
# def tarjan_scc(graph):
#     index = 0
#     disc = {}
#     low = {}
#     stack = []
#     on_stack = set()
#     scc_list = []

#     def dfs(u):
#         nonlocal index
#         disc[u] = low[u] = index
#         index += 1
#         stack.append(u)
#         on_stack.add(u)

#         for v in graph[u]:
#             if v not in disc:
#                 dfs(v)
#                 low[u] = min(low[u], low[v])
#             elif v in on_stack:
#                 low[u] = min(low[u], disc[v])

#         if low[u] == disc[u]:
#             scc = []
#             while True:
#                 w = stack.pop()
#                 on_stack.remove(w)
#                 scc.append(w)
#                 if w == u:
#                     break
#             scc_list.append(scc)

#     for node in graph:
#         if node not in disc:
#             dfs(node)
#     return scc_list

# graph = {'A': ['B'], 'B': ['C'], 'C': ['A']}
# print(tarjan_scc(graph))


# Приклад 1
#     A
#    / \\
#   B   C
#  / \\
# D   E
#      \\
#       F

# У цьому невеликому графі точкою розриву є вершина B (видалення B розділяє граф на дві частини).
# graph1 = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['E']
# }


# Приклад 2
#       A
#      / \\
#     B   C
#    /   / \\
#   D   E   F
#        \\
#         G

# Тут критичними можуть бути A та C, оскільки їх видалення розділяє граф. Приклад:
# graph2 = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D'],
#     'C': ['A', 'E', 'F'],
#     'D': ['B'],
#     'E': ['C', 'G'],
#     'F': ['C'],
#     'G': ['E']
# }


# Приклад 3
#     1 — 2 — 3
#      \\  |
#        4

# У цьому графі видалення 2 розділяє вузли 1 та 3 від 4, тому 2 є точкою розриву.
# graph3 = {
#     '1': ['2', '4'],
#     '2': ['1', '3', '4'],
#     '3': ['2'],
#     '4': ['1', '2']
# }


# Приклад 4
# graph4 = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F', 'G'],
#     'D': ['B', 'H'],
#     'E': ['B', 'I'],
#     'F': ['C', 'J'],
#     'G': ['C', 'K'],
#     'H': ['D'],
#     'I': ['E'],
#     'J': ['F'],
#     'K': ['G', 'L'],
#     'L': ['K']
# }

# ---------------------------------------------------------

# Алгоритм Косараджу:
# Виконується повний обхід графа з використанням DFS для визначення порядку завершення відвідування вершин.
# Створюється транспонований граф (усі напрямки ребер змінюються на протилежні).
# Виконується другий обхід графа, але на транспонованому графі, використовуючи порядок вершин, отриманий на
# першому кроці. Кожний DFS-пошук, який не перетинається з іншими, утворює окрему компоненту сильної зв'язності.

# Алгоритм Тар'яна:
# Працює за допомогою однократного DFS, де зберігаються додаткові значення (індекси, "низькі" значення) для
# кожної вершини, що дозволяє виявити моменти завершення рекурсивного обходу і таким чином ідентифікувати компоненти сильної зв'язності.

# def dfs(graph, node, visited, stack):
#     visited.add(node)
#     for neighbor in graph[node]:
#         if neighbor not in visited:
#             dfs(graph, neighbor, visited, stack)
#     stack.append(node)

# def dfs_transposed(t_graph, node, visited, component):
#     visited.add(node)
#     component.append(node)
#     for neighbor in t_graph[node]:
#         if neighbor not in visited:
#             dfs_transposed(t_graph, neighbor, visited, component)

# # Функція kosaraju_scc(graph) реалізує алгоритм Косараджу для пошуку компонент сильної зв’язності (SCC).
# def kosaraju_scc(graph):
#     visited = set()
#     stack = []

#     for node in graph:
#         if node not in visited:
#             dfs(graph, node, visited, stack)

#     t_graph = transpose_graph(graph)
#     visited.clear()
#     scc = []
#     while stack:
#         node = stack.pop()
#         if node not in visited:
#             component = []
#             dfs_transposed(t_graph, node, visited, component)
#             scc.append(component)
#     return scc

# # Функція transpose_graph(graph) створює транспонований граф.
# def transpose_graph(graph):
#     t_graph = {node: [] for node in graph}
#     for node in graph:
#         for neighbor in graph[node]:
#             t_graph[neighbor].append(node)
#     return t_graph

# graph_example = {
#     'A': ['B'],
#     'B': ['C', 'E', 'F'],
#     'C': ['D', 'G'],
#     'D': ['C', 'H'],
#     'E': ['A', 'F'],
#     'F': ['G'],
#     'G': ['F'],
#     'H': ['D', 'G']
# }
# print(kosaraju_scc(graph_example))