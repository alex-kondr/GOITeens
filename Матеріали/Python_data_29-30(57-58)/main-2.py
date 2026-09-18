# Алгоритм обходу в ширину (BFS, Breadth-First Search) — це
# метод обходу або пошуку у графі чи дереві, який відвідує
# всі вузли одного рівня перед переходом до вузлів наступного рівня.

# Старт: Поміщаємо A у чергу. Поточна черга: [A].
# Крок 1: Видаляємо A з черги та відвідуємо її. Додаємо всіх сусідів A (наприклад, B і C) у чергу.
# Поточний порядок відвідування: [A].
# Поточна черга: [B, C].
# 3. Крок 2: Видаляємо B з черги та відвідуємо її. Додаємо невідвіданих сусідів B
# (наприклад, D і E) у чергу.
# Поточний порядок відвідування: [A, B].
# Поточна черга: [C, D, E].
# 4. Крок 3: Видаляємо C з черги та відвідуємо її. Додаємо її невідвіданих сусідів
# (наприклад, F) у чергу.
# Поточний порядок відвідування: [A, B, C].
# Поточна черга: [D, E, F].
# 5. Продовження: Процес повторюється для вузлів D, E, F тощо, поки черга не стане
# порожньою.


# from collections import deque

# def bfs(graph, start):
#     visited = set()
#     order = []
#     queue = deque([start])
#     visited.add(start)
#     while queue:
#         node = queue.popleft()
#         order.append(node)
#         for neighbor in graph[node]:
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 queue.append(neighbor)
#     return order

# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }
# result = bfs(graph, 'A')
# print(result)



# Алгоритм обходу в ширину (BFS) широко
# використовується для знаходження найкоротшого шляху

# from collections import deque

# def bfs_shortest_path(graph, start, goal):
#     if start == goal:
#         return [start]
#     queue = deque([[start]])
#     visited = set([start])

#     while queue:
#         path = queue.popleft()
#         node = path[-1]
#         if node == goal:
#             return path
#         for neighbor in graph.get(node, []):
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 new_path = list(path)
#                 new_path.append(neighbor)
#                 queue.append(new_path)
#     return None

# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E', 'G'],
#     'G': ['F']
# }
# start_node = 'A'
# goal_node = 'G'

# shortest_path = bfs_shortest_path(graph, start_node, goal_node)
# print(shortest_path)

# -------------------------------------------------------------

# Приклади лабіринтів і опис обходу

# Приклад 1
# Лабіринт:

# S 0 1 0
# 1 0 1 0
# 1 0 0 0
# 1 1 1 E

# S — стартова позиція (0,0).
# E — вихід (3,3).

# Обхід BFS:
# Починаємо з (0,0). Сусіди: (0,1).
# З (0,1) переходимо до (1,1).
# З (1,1) знаходимо (2,1).
# З (2,1) переходимо до (2,2), а з (2,2) до (2,3).
# З (2,3) переходимо до (3,3) — виходу.


# Приклад 2
# Лабіринт:

# S 0 0 1 0
# 1 1 0 1 0
# 0 0 0 0 0
# 0 1 1 1 0
# 0 0 0 E 1

# Обхід BFS:
# Старт: (0,0) → сусіди: (0,1).
# (0,1) → (0,2).
# (0,2) → (1,2) і (0,3) не прохід.
# (1,2) → (2,2) і (1,1) не прохід.
# (2,2) → (2,1), (2,3) та (3,2) (але (3,2) — стіна).
# (2,3) → (2,4) і (3,3) (але (3,3) — стіна).
# (2,4) → (3,4) -> (4,4) - стіна
# (2,1) → (2,0) -> (3,0) -> (4,0) -> (4,1) -> (4,2) -> (4,3) — вихід.


# Приклад 3
# Лабіринт:

# S 1 0 0 0
# 0 0 0 1 0
# 1 1 0 1 0
# 0 0 0 1 0
# 0 1 0 0 E

# Обхід BFS:
# Старт (0,0) → сусід: (1,0).
# (1,0) → (1,1).
# (1,1) → (1,2) та (2,1) (але (2,1) — стіна).
# (1,2) → (0,2) та (2,2).
# (2,2) → (3,2).
# (3,2) → (3,1) та (3,3) (але (3,3) — стіна).
# (3,1) → (4,1) (але (4,1) — стіна) та (3,0).
# (3,0) → (4,0).
# (4,0) → (4,2).
# (4,2) → (4,3) і (4,3) → (4,4) — вихід.


# Приклад 4
# Лабіринт:

# S 0 1 0 0 0
# 1 0 1 0 1 0
# 0 0 0 0 1 0
# 0 1 1 0 0 0
# 0 0 0 1 1 E

# Обхід BFS:
# Починаємо з (0,0) → (0,1).
# (0,1) → (1,1).
# (1,1) → (2,1) та (1,0) вже відвіданий.
# (2,1) → (2,0), (2,2), (3,1) (але (3,1) — стіна).
# (2,2) → (2,3).
# (2,3) → (3,3).
# (3,3) → (3,4) та (4,3) (але (4,3) — стіна).
# (3,4) → (3,5) та (4,4) (але (4,4) — стіна).
# (3,5) → (4,5) — вихід.

# ----------------------------------------

# from collections import deque

# def bfs_labyrinth(maze, start, end):
#     rows, cols = len(maze), len(maze[0])
#     queue = deque([start])
#     visited = {start: None}
#     while queue:
#         current = queue.popleft()
#         if current == end:
#             break
#         row, col = current
#         for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#             r, c = row + dr, col + dc
#             if 0 <= r < rows and 0 <= c < cols and maze[r][c] == 0 and (r, c) not in visited:
#                 visited[(r, c)] = current
#                 queue.append((r, c))

#     path = []
#     current = end
#     if current not in visited:
#         return None
#     while current is not None:
#         path.append(current)
#         current = visited[current]
#     path.reverse()
    # return path

# maze1 = [
#     [0, 0, 1, 0],
#     [1, 0, 1, 0],
#     [1, 0, 0, 0],
#     [1, 1, 1, 0]
# ]
# start1 = (0, 0)
# end1 = (3, 3)
# path1 = bfs_labyrinth(maze1, start1, end1)
# print("Шлях для лабіринту 1:", path1)

# maze2 = [
#     [0, 0, 0, 1, 0],
#     [1, 1, 0, 1, 0],
#     [0, 0, 0, 0, 0],
#     [0, 1, 1, 1, 0],
#     [0, 0, 0, 0, 0]
# ]
# start2 = (0, 0)
# end2 = (4, 3)
# path2 = bfs_labyrinth(maze2, start2, end2)
# print("Шлях для лабіринту 2:", path2)

# maze3 = [
#     [0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0],
#     [1, 1, 0, 1, 0],
#     [0, 0, 0, 1, 0],
#     [0, 1, 0, 0, 0]
# ]
# start3 = (0, 0)
# end3 = (4, 4)
# path3 = bfs_labyrinth(maze3, start3, end3)
# print("Шлях для лабіринту 3:", path3)

# maze4 = [
#     [0, 0, 1, 0, 0, 0],
#     [1, 0, 1, 0, 1, 0],
#     [0, 0, 0, 0, 1, 0],
#     [0, 1, 1, 0, 1, 0],
#     [0, 0, 0, 1, 1, 0]
# ]
# start4 = (0, 0)
# end4 = (4, 5)
# path4 = bfs_labyrinth(maze4, start4, end4)
# print("Шлях для лабіринту 4:", path4)

# ----------------------------------------------------------------


# Задача розфарбування графа полягає у
# визначенні, чи можна призначити кожному
# вузлу графа один із двох кольорів таким
# чином, щоб жодна пара суміжних вузлів
# не мала однакового кольору. Це важливе
# завдання, яке застосовується для перевірки
# двохколірності графа.

# двоколірний
# {
#     'A': ['B', 'C'],
#     'B': ['A', 'D'],
#     'C': ['A', 'D'],
#     'D': ['B', 'C']
# }

# не двоколірний
# {
#     'A': ['B', 'C'],
#     'B': ['A', 'C'],
#     'C': ['A', 'B']
# }

# не двоколірний
# {
#     '1': ['2', '3'],
#     '2': ['1', '4', '5'],
#     '3': ['1', '6'],
#     '4': ['2'],
#     '5': ['2', '6'],
#     '6': ['3', '5']
# }

# двоколірний
# {
#     'X': ['Y'],
#     'Y': ['X', 'Z'],
#     'Z': ['Y']
# }

# from  collections import deque

# def is_bipartite(graph):
#     colors = {}
#     for node in graph:
#         if node not in colors:
#             queue = deque([node])
#             colors[node] = 0
#             while queue:
#                 current = queue.popleft()
#                 for neighbor in graph[current]:
#                     if neighbor not in colors:
#                         colors[neighbor] = 1 - colors[current]
#                         queue.append(neighbor)
#                     elif colors[neighbor] == colors[current]:
#                         return False, None
#     return True, colors

# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D'],
#     'C': ['A', 'D'],
#     'D': ['B', 'C']
# }
# result, colors = is_bipartite(graph)
# print("Граф двохколірний:", result, "| Розфарбування:", colors)
