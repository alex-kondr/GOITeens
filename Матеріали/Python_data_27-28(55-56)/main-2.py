# Бінарне дерево пошуку (BST) — це спеціалізований тип бінарного дерева,
# в якому для кожного вузла виконуються наступні умови:

# Всі значення в лівому піддереві менші за значення вузла.
# Всі значення в правому піддереві більші або рівні за значення вузла.


# class BinaryNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None


# def insert(root, value):
#     if root is None:
#         return BinaryNode(value)
#     if value < root.value:
#         root.left = insert(root.left, value)
#     else:
#         root.right = insert(root.right, value)
#     return root


# def inorder_traversal(root):
#     if root is None:
#         return []
#     return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)


# values = [10, 5, 15, 2, 7, 12, 20]
# root = None
# for val in values:
#     root = insert(root, val)


# print("Симетричний обхід дерева:", inorder_traversal(root))

# ------------------------------------------------------------------------

# class BinaryNode:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right

# def bst_search(root, target):
#     if root is None:
#         return None
#     if root.value == target:
#         return root
#     elif target < root.value:
#         return bst_search(root.left, target)
#     else:
#         return bst_search(root.right, target)

# root = BinaryNode(
#     10,
#     BinaryNode(5, BinaryNode(2), BinaryNode(7)),
#     BinaryNode(15, None, BinaryNode(20))
# )

# result_node = bst_search(root, 7)
# if result_node:
#     print("Значення знайдено:", result_node.value)
# else:
#     print("Значення не знайдено")
# ------------------------------------------------------------


# ЗАВДАННЯ 1
# Напишіть функцію level_order_traversal(root),
# яка виконує обхід дерева за рівнями (BFS) і
# повертає список списків, де кожен внутрішній
# список містить значення вузлів одного рівня.

# Початковий код:
# def level_order_traversal(root):
#     # Ініціалізуйте чергу з кореня (якщо він не None)
#     # Використовуйте цикл while для обходу дерева
#     # Для кожного рівня створіть список значень
#     # Додайте дітей поточних вузлів до черги для наступного рівня
#     pass

# Тестування: використайте дерево з попередніх завдань або створіть нове


# Правильний код
# from collections import deque

# def level_order_traversal(root):
#     if root is None:
#         return []

#     result = []
#     queue = deque([root])
#     while queue:
#         level_size = len(queue)
#         current_level = []
#         for _ in range(level_size):
#             node = queue.popleft()
#             current_level.append(node.value)
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#         result.append(current_level)
#     return result

# class BinaryNode:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right

# root = BinaryNode(50,
#           BinaryNode(30, BinaryNode(20), BinaryNode(40)),
#           BinaryNode(70, BinaryNode(60), BinaryNode(80))
#          )

# print("Level-order traversal:", level_order_traversal(root))


# ЗАВДАННЯ 2
# Реалізуйте функцію tree_height(root), яка повертає
# висоту (максимальну глибину) BST. Висота визначається
# як кількість вузлів у найдовшому шляху від кореня до листя.

# Початковий код:
# def tree_height(root):
#     # Якщо root порожній, поверніть 0
#     # Рекурсивно обчисліть висоту лівого та правого піддерев
#     # Поверніть 1 + max(ліва висота, права висота)
#     pass

# Тестування: використайте побудоване дерево


# Правильний код
# class BinaryNode:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right

# root = BinaryNode(50,
#           BinaryNode(30, BinaryNode(20), BinaryNode(40)),
#           BinaryNode(70, BinaryNode(60), BinaryNode(80))
#          )

# def tree_height(root):
#     if root is None:
#         return 0
#     return 1 + max(tree_height(root.left), tree_height(root.right))

# print("Висота дерева:", tree_height(root))



# ЗАВДАННЯ 3
# Реалізуйте функцію is_valid_bst(root, min_val=-float('inf'), max_val=float('inf')),
# яка перевіряє, чи є задане дерево валідним BST. Функція повинна рекурсивно перевіряти,
# що всі вузли задовольняють умови: значення в лівому піддереві < поточного,
# а в правому – ≥ поточного.

# Початковий код
# def is_valid_bst(root, min_val=-float('inf'), max_val=float('inf')):
#     # Якщо root порожній, поверніть True
#     # Перевірте, чи лежить root.value між min_val і max_val
#     # Рекурсивно перевірте ліве піддерево з оновленим max_val і праве піддерево з оновленим min_val
#     pass

# Тестування: використайте дерево з попередніх завдань

# Правильний код
# def is_valid_bst(root, min_val=-float('inf'), max_val=float('inf')):
#     if root is None:
#         return True
#     if not (min_val <= root.value < max_val):
#         return False
#     return is_valid_bst(root.left, min_val, root.value) and is_valid_bst(root.right, root.value, max_val)

# print("Чи є дерево валідним BST?", is_valid_bst(root))

# ------------------------------------------------------------------

# def inorder_traversal(root):
#     if root is None:
#         return []
#     return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)

# def preorder_traversal(root):
#     if root is None:
#         return []
#     return [root.value] + preorder_traversal(root.left) + preorder_traversal(root.right)

# def postorder_traversal(root):
#     if root is None:
#         return []
#     return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.value]

# -----------------------------------------------------------------------


# ЗАВДАННЯ 1
# Напишіть функцію inorder_successor(root, target), яка знаходить in-order
# наступника вузла з заданим значенням. In-order наступник — це вузол з
# найменшим значенням, яке більше за target.

# Початковий код:
# def inorder_successor(root, target):
#     # Використовуйте in-order обхід, щоб отримати впорядкований список
#     # Знайдіть позицію target у списку
#     # Якщо наступного елемента немає, поверніть None
#     pass

# Тестування: використайте дерево та знайдіть наступника для заданого елемента

# Правильний код
# def inorder_successor(root, target):
#     def inorder(root):
#         return inorder(root.left) + [root.value] + inorder(root.right) if root else []

#     sorted_values = inorder(root)
#     for i, value in enumerate(sorted_values):
#         if value == target and i < len(sorted_values) - 1:
#             return sorted_values[i + 1]
#     return None

# print("In-order наступник для 40:", inorder_successor(root, 40))


# ЗАВДАННЯ 2
# Реалізуйте функцію delete_node(root, target),
# яка видаляє вузол із заданим значенням у BST,
# зберігаючи властивості дерева.
# Підказка: розгляньте три випадки: вузол є листям, має одного нащадка, або має двох нащадків.

# Початковий код:
# def delete_node(root, target):
#     # Якщо дерево порожнє, поверніть None
#     # Якщо target менше root.value, рекурсивно видаляйте з лівого піддерева
#     # Якщо target більше root.value, рекурсивно видаляйте з правого піддерева
#     # Якщо target дорівнює root.value, обробіть випадки видалення (без дітей, з одним, з двома)
#     pass

# Правильний код
# def delete_node(root, target):
#     if root is None:
#         return None

#     if target < root.value:
#         root.left = delete_node(root.left, target)
#     elif target > root.value:
#         root.right = delete_node(root.right, target)
#     else:
#         if root.left is None:
#             return root.right
#         if root.right is None:
#             return root.left
#         temp = root.right
#         while temp.left:
#             temp = temp.left
#         root.value = temp.value
#         root.right = delete_node(root.right, temp.value)
#     return root

# new_root = delete_node(root, 30)
# print("In-order traversal після видалення 30:", inorder_traversal(new_root))


# Завдання 3
# Напишіть функцію count_leaves(root), яка
# повертає кількість листових вузлів у BST.

# Початковий код:
# def count_leaves(root):
#     # Якщо root порожній, поверніть 0
#     # Якщо root не має дітей, поверніть 1
#     # Інакше рекурсивно підрахуйте листя у лівому та правому піддереві
#     pass

# Правильний код
# def count_leaves(root):
#     if root is None:
#         return 0
#     if root.left is None and root.right is None:
#         return 1
#     return count_leaves(root.left) + count_leaves(root.right)

# print("Кількість листових вузлів:", count_leaves(root))



# ЗАВДАННЯ 4
# Напишіть функцію, яка:
# Використовуючи in-order обхід, перетворює BST у відсортований список.
# На основі цього списку будує збалансоване BST.

# Початковий код
# def bst_to_sorted_list(root):
#     # Виконайте in-order обхід для отримання відсортованого списку
#     pass

# def sorted_list_to_bst(lst):
#     # Якщо список порожній, поверніть None
#     # Знайдіть середній елемент списку
#     # Рекурсивно побудуйте ліве та праве піддерево з відповідних частин списку
#     pass

# sorted_values = bst_to_sorted_list(root)
# balanced_root = sorted_list_to_bst(sorted_values)
# print("In-order traversal збалансованого BST:", inorder_traversal(balanced_root))

# Правильний код
# def bst_to_sorted_list(root):
#     if root is None:
#         return []
#     return bst_to_sorted_list(root.left) + [root.value] + bst_to_sorted_list(root.right)

# def sorted_list_to_bst(lst):
#     if not lst:
#         return None
#     mid = len(lst) // 2
#     root = BinaryNode(lst[mid])
#     root.left = sorted_list_to_bst(lst[:mid])
#     root.right = sorted_list_to_bst(lst[mid+1:])
#     return root

# sorted_values = bst_to_sorted_list(root)
# balanced_root = sorted_list_to_bst(sorted_values)
# print("In-order traversal збалансованого BST:", inorder_traversal(balanced_root))



# Завдання 5
# Реалізуйте функцію bfs_traversal(root), яка виконує
# обход дерева за рівнями, використовуючи чергу (FIFO).
# Функція має повертати список списків, де кожен
# внутрішній список містить значення вузлів відповідного рівня.

# Початковий код:
# def bfs_traversal(root):
#     # Ініціалізуйте порожню чергу (наприклад, з використанням collections.deque)
#     # Якщо корінь не None, додайте його до черги
#     # Використовуйте цикл while, поки черга не порожня:
#     #   - Отримайте кількість вузлів поточного рівня
#     #   - Створіть порожній список для поточного рівня
#     #   - Для кожного вузла цього рівня:
#     #       - Видаліть вузол з черги
#     #       - Додайте його значення до списку поточного рівня
#     #       - Якщо лівий або правий дочірній вузол існує, додайте їх до черги
#     #   - Додайте список поточного рівня до результату
#     pass


# Правильний код
# from collections import deque

# def bfs_traversal(root):
#     if root is None:
#         return []
#     result = []
#     queue = deque([root])
#     while queue:
#         level_size = len(queue)
#         level_nodes = []
#         for _ in range(level_size):
#             node = queue.popleft()
#             level_nodes.append(node.value)
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#         result.append(level_nodes)
#     return result

# class BinaryNode:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right

# root = BinaryNode(50,
#           BinaryNode(30, BinaryNode(20), BinaryNode(40)),
#           BinaryNode(70, BinaryNode(60), BinaryNode(80))
#          )

# print("BFS traversal (рівневий обхід):", bfs_traversal(root))