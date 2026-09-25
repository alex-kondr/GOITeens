# Алгоритм обходу в глибину (DFS) —
# це метод дослідження графа або дерева, при
# якому спочатку відвідується якнайглибший вузол

# DFS застосовується для:

# Виявлення всіх компонент зв’язності в графі.
# Пошуку циклів.
# Рішення задач топологічного сортування.
# Перебору простору станів у задачах, пов’язаних з пошуком (наприклад, у головоломках).



# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }

# def dfs(node, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(node)
#     print(node)
#     for neighbor in graph[node]:
#         if neighbor not in visited:
#             dfs(neighbor, visited)
#     return visited

# def dfs_recursive(node, graph, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(node)
#     print(node, end=" ")
#     for neighbor in graph[node]:
#         if neighbor not in visited:
#             dfs_recursive(neighbor, graph, visited)
#     return visited

# def dfs_iterative(start, graph):
#     visited = set()
#     stack = [start]
#     while stack:
#         node = stack.pop()
#         if node not in visited:
#             visited.add(node)
#             print(node, end=" ")
#             stack.extend(reversed(graph[node]))
#     return visited

# --------------------------------------------------------

# Пошук компонент зв’язності

# def dfs_component(node, graph, visited):
#     visited.add(node)
#     component = [node]
#     for neighbor in graph[node]:
#         if neighbor not in visited:
#             component.extend(dfs_component(neighbor, graph, visited))
#     return component

# def find_connected_components(graph):
#     visited = set()
#     components = []
#     for node in graph:
#         if node not in visited:
#             component = dfs_component(node, graph, visited)
#             components.append(component)
#     return components

# graph = {
#     'A': ['B'],
#     'B': ['A', 'C'],
#     'C': ['B'],
#     'D': ['E'],
#     'E': ['D'],
#     'F': []
# }


# --------------------------------------------------------

# Топологічне сортування

# def dfs_topological(node: str, graph: dict, visited: set, stack: list):
#     visited.add(node)
#     for neighbor in graph[node]:
#         if neighbor not in visited:
#             dfs_topological(neighbor, graph, visited, stack)
#     stack.append(node)

# def topological_sort(graph):
#     visited = set()
#     stack = []
#     for node in graph:
#         if node not in visited:
#             dfs_topological(node, graph, visited, stack)
#     return stack[::-1]

# graph_dag = {
#     'A': ['C', 'D'],
#     'B': ['D'],
#     'C': ['E'],
#     'D': ['F'],
#     'E': ['F'],
#     'F': []
# }

# order = topological_sort(graph_dag)
# print("Топологічне сортування:", order)

# -----------------------------------------------------------

# Виявлення циклів у графі

# def dfs_cycle(node, graph, visited, rec_stack):
#     visited.add(node)
#     rec_stack.add(node)
#     for neighbor in graph[node]:
#         if neighbor not in visited:
#             if dfs_cycle(neighbor, graph, visited, rec_stack):
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
#             if dfs_cycle(node, graph, visited, rec_stack):
#                 return True
#     return False

# graph_cycle = {
#     'A': ['B'],
#     'B': ['C'],
#     'C': ['A'],
#     'D': ['E'],
#     'E': []
# }

# print("Граф містить цикл:", has_cycle(graph_cycle))

# ---------------------------------------------------------------

# знайти шлях у лабіринті, який представлено матрицею

# def dfs_labyrinth(maze, start, end):
#     rows, cols = len(maze), len(maze[0])
#     stack = [start]
#     visited = {start: None}

#     while stack:
#         current = stack.pop()
#         if current == end:
#             break
#         row, col = current
#         for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#             r, c = row + dr, col + dc
#             if 0 <= r < rows and 0 <= c < cols and maze[r][c] == 0 and (r, c) not in visited:
#                 visited[(r, c)] = current
#                 stack.append((r, c))

#     path = []
#     if end not in visited:
#         return None
#     current = end
#     while current is not None:
#         path.append(current)
#         current = visited[current]
#     path.reverse()
#     return path

# ------------------------------------------------------------------

# Задача 1
# Реалізуйте DFS для лабіринту з можливістю виведення всієї послідовності відвіданих клітинок.

# лабіринт, представлено матрицею

# def dfs_labyrinth(maze, start, end):
#     rows, cols = len(maze), len(maze[0])
#     stack = [start]
#     visited = {start: None}

#     while stack:
#         current = stack.pop()
#         if current == end:
#             break
#         row, col = current
#         for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#             r, c = row + dr, col + dc
#             if 0 <= r < rows and 0 <= c < cols and maze[r][c] == 0 and (r, c) not in visited:
#                 visited[(r, c)] = current
#                 print(current, end=" ")
#                 stack.append((r, c))

#     path = []
#     if end not in visited:
#         return None
#     current = end
#     while current is not None:
#         path.append(current)
#         current = visited[current]
#     path.reverse()
#     return path

# # Приклад лабіринту:
# # 0 - вільна клітинка
# # 1 - стіна
# labyrinth = [
#     [0, 1, 0, 0, 0],
#     [0, 1, 0, 1, 0],
#     [0, 0, 0, 1, 0],
#     [0, 1, 1, 1, 0],
#     [0, 0, 0, 0, 0]
# ]

# start = (0, 0)   # верхній лівий кут
# end = (4, 4)     # нижній правий кут

# print("Пошук шляху в лабіринті за допомогою DFS:")
# dfs_labyrinth(labyrinth, start, end)


# Задача 2
# Розширте функцію DFS, щоб вона повертала не лише шлях, але й кількість зроблених кроків.
# def dfs_labyrinth_steps(maze, start, end):
#     rows, cols = len(maze), len(maze[0])
#     stack = [start]
#     visited = {start: None}
#     steps_count = 0

#     while stack:
#         current = stack.pop()
#         steps_count += 1
#         if current == end:
#             break
#         row, col = current
#         for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#             r, c = row + dr, col + dc
#             if 0 <= r < rows and 0 <= c < cols and maze[r][c] == 0 and (r, c) not in visited:
#                 visited[(r, c)] = current
#                 print(current, end=" ")
#                 stack.append((r, c))

#     path = []
#     if end not in visited:
#         return None, steps_count
#     current = end
#     while current is not None:
#         path.append(current)
#         current = visited[current]
#     path.reverse()

#     steps_in_path = len(path) - 1
#     return path, steps_in_path


# Задача 3
# Змініть алгоритм DFS для лабіринту, щоб він знаходив найкоротший шлях (з використанням додаткового контролю глибини).

# def dfs_shortest_path(maze, start, end):
#     rows, cols = len(maze), len(maze[0])

#     def dls(current, depth_limit, visited_path):
#         if current == end:
#             return visited_path
#         if len(visited_path) - 1 >= depth_limit:
#             return None

#         row, col = current
#         for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#             r, c = row + dr, col + dc
#             if 0 <= r < rows and 0 <= c < cols and maze[r][c] == 0:
#                 next_cell = (r, c)
#                 if next_cell not in visited_path:
#                     res = dls(next_cell, depth_limit, visited_path + [next_cell])
#                     if res is not None:
#                         return res
#         return None

#     max_possible_depth = rows * cols
#     for limit in range(max_possible_depth):
#         path = dls(start, limit, [start])
#         if path is not None:
#             return path
#     return None


# Задача 4
# Реалізуйте DFS для лабіринту, представивши результати у вигляді графічної візуалізації шляху.

# def visualize_path_dfs(maze, path):
#     rows, cols = len(maze), len(maze[0])
#     visual_maze = [row[:] for row in maze]

#     if path:
#         for r, c in path:
#             if (r, c) != path[0] and (r, c) != path[-1]:
#                 visual_maze[r][c] = 2

#     print("Лабіринт з позначеним шляхом (0 - вільна клітинка, 1 - стіна, 2 - шлях):")
#     for row in visual_maze:
#         print(" ".join(map(str, row)))


# Задача 5
# Напишіть функцію, яка перевіряє, чи існує шлях у лабіринті, використовуючи DFS, і повертає булеве значення.

# def has_path_dfs(maze, start, end):
#     rows, cols = len(maze), len(maze[0])
#     stack = [start]
#     visited = {start}

#     while stack:
#         current = stack.pop()
#         if current == end:
#             return True
#         row, col = current
#         for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#             r, c = row + dr, col + dc
#             if 0 <= r < rows and 0 <= c < cols and maze[r][c] == 0 and (r, c) not in visited:
#                 visited.add((r, c))
#                 stack.append((r, c))
#     return False

# Задача 6
# Застосуйте DFS для пошуку циклів у графоподібному лабіринті.

# def has_cycle_dfs(maze):
#     rows, cols = len(maze), len(maze[0])
#     visited = set()
#     visiting = set()

#     def dfs(r, c, parent=None):
#         visited.add((r, c))
#         visiting.add((r, c))

#         for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#             nr, nc = r + dr, c + dc
#             if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
#                 neighbor = (nr, nc)
#                 if neighbor == parent:
#                     continue
#                 if neighbor in visiting:
#                     return True
#                 if neighbor not in visited:
#                     if dfs(nr, nc, (r, c)):
#                         return True
#         visiting.remove((r, c))
#         return False

#     for r in range(rows):
#         for c in range(cols):
#             if maze[r][c] == 0 and (r, c) not in visited:
#                 if dfs(r, c):
#                     return True
#     return False

# Задача 7
# Реалізуйте DFS для знаходження всіх можливих шляхів у невеликому лабіринті, повертаючи список усіх можливих шляхів.

# def find_all_paths_dfs(maze, start, end):
#     rows, cols = len(maze), len(maze[0])
#     all_paths = []

#     def dfs(r, c, current_path):
#         if (r, c) == end:
#             all_paths.append(current_path + [(r, c)])
#             return

#         current_path.append((r, c))
#         row, col = r, c

#         for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#             nr, nc = row + dr, col + dc
#             if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0 and (nr, nc) not in current_path:
#                 dfs(nr, nc, current_path)

#         current_path.pop()

#     dfs(start[0], start[1], [])
#     return all_paths

# ------------------------------------------------------------------------------------------


# ЗАВДАННЯ 1
# Реалізуйте рекурсивну функцію dfs_recursive(root) для обходу бінарного дерева.
# Функція має повертати список значень вузлів у порядку обходу DFS.
# Виведіть отриманий список.

# Початковий код:
# def dfs_recursive(root):
#     # Якщо вузол порожній, поверніть порожній список
#     # Інакше, поверніть список: [root.value] + рекурсивний обхід лівого піддерева + рекурсивний обхід правого піддерева
#     pass

# # Приклад дерева
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right

# tree = Node(10,
#             Node(5, Node(2), Node(7)),
#             Node(15, None, Node(20))
#            )

# result = dfs_recursive(tree)
# print("DFS рекурсивний обхід:", result)

# Правильний код
# def dfs_recursive(root):
#     if root is None:
#         return []
#     return [root.value] + dfs_recursive(root.left) + dfs_recursive(root.right)

# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right

# tree = Node(10,
#             Node(5, Node(2), Node(7)),
#             Node(15, None, Node(20))
#            )

# result = dfs_recursive(tree)
# print("DFS рекурсивний обхід:", result)

# ------------------------------------------------------------------------------------------


# ЗАВДАННЯ 2
# Реалізуйте ітеративну функцію dfs_iterative(root) для обходу бінарного дерева з використанням стека.
# Функція має повертати список значень вузлів у порядку обходу DFS.
# Виведіть отриманий список.

# Початковий код:
# def dfs_iterative(root):
#     # Ініціалізуйте стек з кореня
#     # Ініціалізуйте порожній список для збереження результатів
#     # Поки стек не порожній, дістаньте вузол, додайте його значення до результату
#     # Додайте спочатку праве, потім ліве піддерево у стек
#     pass

# # Використайте клас Node з попереднього завдання
# result = dfs_iterative(tree)
# print("DFS ітеративний обхід:", result)

# Правильний код
# def dfs_iterative(root):
#     if root is None:
#         return []
#     stack = [root]
#     result = []
#     while stack:
#         node = stack.pop()
#         result.append(node.value)
#         if node.right:
#             stack.append(node.right)
#         if node.left:
#             stack.append(node.left)
#     return result

# result = dfs_iterative(tree)
# print("DFS ітеративний обхід:", result)

# ------------------------------------------------------------------------------------------

# ЗАВДАННЯ 3
# Реалізуйте функцію dfs_graph(graph, start, visited) для обходу графа, представленого списком суміжності.
# Функція має повертати список вузлів, відвіданих у порядку обходу.
# Використовуйте рекурсивний підхід.

# Початковий код:
# def dfs_graph(graph, start, visited=None):
#     # Якщо visited порожній, створіть порожню множину
#     # Додайте start у visited
#     # Для кожного сусіда вузла, який не відвіданий, викликайте dfs_graph рекурсивно
#     # Поверніть список відвіданих вузлів
#     pass

# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }

# result = dfs_graph(graph, 'A')
# print("DFS обхід графа (рекурсивний):", result)

# Правильний код
# def dfs_graph(graph, start, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)
#     result = [start]
#     for neighbor in graph[start]:
#         if neighbor not in visited:
#             result.extend(dfs_graph(graph, neighbor, visited))
#     return result

# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }

# result = dfs_graph(graph, 'A')
# print("DFS обход графа (рекурсивний):", result)

# ------------------------------------------------------------------------------------------


# ЗАВДАННЯ 4
# Реалізуйте функцію dfs_graph_iterative(graph, start) для обходу графа ітеративно з використанням стека.
# Функція має повертати список вузлів у порядку обходу.
# Використовуйте стек для збереження стану обходу.

# Початковий код:
# def dfs_graph_iterative(graph, start):
#     # Ініціалізуйте стек з вузла start
#     # Ініціалізуйте порожню множину visited і список result
#     # Поки стек не порожній, дістаньте вузол, якщо він не відвіданий – додайте в visited і результат
#     # Додайте сусідів цього вузла до стека
#     pass

# result = dfs_graph_iterative(graph, 'A')
# print("DFS обход графа (ітеративний):", result)

# Правильний код
# def dfs_graph_iterative(graph, start):
#     stack = [start]
#     visited = set()
#     result = []
#     while stack:
#         node = stack.pop()
#         if node not in visited:
#             visited.add(node)
#             result.append(node)
#             for neighbor in reversed(graph[node]):
#                 if neighbor not in visited:
#                     stack.append(neighbor)
#     return result

# result = dfs_graph_iterative(graph, 'A')
# print("DFS обход графа (ітеративний):", result)

# ------------------------------------------------------------------------------------------


# ЗАВДАННЯ 5
# Реалізуйте функцію is_bipartite(graph) для перевірки, чи можна розфарбувати граф двома кольорами.
# Використовуйте DFS для обходу графа та присвоєння кольорів.
# Якщо під час обходу виявлено, що два сусідні вузли мають однаковий колір, поверніть False, інакше – True.

# Початковий код:
# def is_bipartite(graph):
#     # Ініціалізуйте словник для зберігання кольорів вузлів
#     # Реалізуйте DFS для присвоєння кольорів, починаючи з будь-якого вузла
#     # Якщо сусідній вузол має такий же колір, поверніть False
#     # Якщо обходу графа пройдено успішно, поверніть True
#     pass

# graph_bip = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D'],
#     'C': ['A', 'D'],
#     'D': ['B', 'C']
# }

# print("Граф двохколірний:", is_bipartite(graph_bip))

# Правильний код
# def is_bipartite(graph):
#     colors = {}
#     def dfs(node, color):
#         colors[node] = color
#         for neighbor in graph[node]:
#             if neighbor in colors:
#                 if colors[neighbor] == color:
#                     return False
#             else:
#                 if not dfs(neighbor, 1 - color):
#                     return False
#         return True
#     for node in graph:
#         if node not in colors:
#             if not dfs(node, 0):
#                 return False
#     return True

# graph_bip = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D'],
#     'C': ['A', 'D'],
#     'D': ['B', 'C']
# }

# print("Граф двохколірний:", is_bipartite(graph_bip))

# ------------------------------------------------------------------------------------------


# ЗАВДАННЯ 6
# Реалізуйте функцію dfs_count(graph, start) для обходу графа і підрахунку кількості відвіданих вузлів.
# Використовуйте ітеративний підхід з використанням стека.
# Функція має повертати кількість унікальних вузлів, які були відвідані.
# Виведіть отримане число.

# Початковий код:
# def dfs_count(graph, start):
#     # Ініціалізуйте стек з вузла start, порожню множину visited та лічильник count
#     # Поки стек не порожній, дістаньте вузол і, якщо він не відвіданий, додайте до visited і збільшіть лічильник
#     # Додайте сусідів вузла до стека
#     pass

# graph = {
#     'A': ['B', 'C'],
#     'B': ['D'],
#     'C': ['E', 'F'],
#     'D': [],
#     'E': [],
#     'F': []
# }

# result = dfs_count(graph, 'A')
# print("Кількість відвіданих вузлів:", result)

# # Правильний код
# def dfs_count(graph, start):
#     stack = [start]
#     visited = set()
#     count = 0
#     while stack:
#         node = stack.pop()
#         if node not in visited:
#             visited.add(node)
#             count += 1
#             for neighbor in graph[node]:
#                 if neighbor not in visited:
#                     stack.append(neighbor)
#     return count

# graph = {
#     'A': ['B', 'C'],
#     'B': ['D'],
#     'C': ['E', 'F'],
#     'D': [],
#     'E': [],
#     'F': []
# }

# result = dfs_count(graph, 'A')
# print("Кількість відвіданих вузлів:", result