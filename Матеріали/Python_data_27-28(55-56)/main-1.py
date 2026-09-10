# Бінарне дерево

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print("    " * level + f"{node.data}")
        print_tree(node.left, level + 1)

root = Node(10,
            Node(5, Node(2), Node(7)),
            Node(15, None, Node(20))
           )

# print_tree(root)



# n-арне дерево

class NaryNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def print_nary_tree(node, level=0):
    if node:
        print("    " * level + str(node.data))
        for child in node.children:
            print_nary_tree(child, level + 1)

root = NaryNode("A")
nodeB = NaryNode("B")
nodeC = NaryNode("C")
nodeD = NaryNode("D")
root.children = [nodeB, nodeC, nodeD]
nodeB.children = [NaryNode("E"), NaryNode("F")]
nodeD.children = [NaryNode("G")]

# print_nary_tree(root)


# ЗАВДАННЯ 1
# Створіть клас TreeNode для представлення вузла дерева,
# який містить значення та список дітей. Реалізуйте
# побудову дерева, де корінь має кілька нащадків,
# а деякі з них мають своїх дітей (листя).

# Початковий код:
# class TreeNode:
#     def __init__(self, value):
#         # Ініціалізуйте вузол з даним value та порожнім списком дітей
#         pass

# # Побудуйте дерево:
# #         "A"
# #        / | \\
# #      "B" "C" "D"
# #       |      / \\
# #     "E"    "F" "G"
# def build_tree():
#     pass

# root = build_tree()
# # Викличте функцію для виводу дерева (наприклад, рекурсивно з відступами)
# def print_tree(node, level=0):
#     pass

# print_tree(root)

# Правильний код
# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.children = []

# def build_tree():
#     root = TreeNode("A")
#     nodeB = TreeNode("B")
#     nodeC = TreeNode("C")
#     nodeD = TreeNode("D")
#     root.children = [nodeB, nodeC, nodeD]
#     nodeE = TreeNode("E")
#     nodeB.children.append(nodeE)
#     nodeF = TreeNode("F")
#     nodeG = TreeNode("G")
#     nodeD.children = [nodeF, nodeG]
#     return root

# def print_tree(node, level=0):
#     if node:
#         print("    " * level + str(node.value))
#         for child in node.children:
#             print_tree(child, level + 1)

# root = build_tree()
# print_tree(root)



# ЗАВДАННЯ 2
# Реалізуйте функцію inorder_traversal(root), яка
# виконує симетричний (inorder) обхід бінарного
# дерева та повертає список значень. Для цього
# створіть клас BinaryNode з атрибутами value, left і right.

# # Початковий код:
# class BinaryNode:
#     def __init__(self, value, left=None, right=None):
#         # Ініціалізуйте вузол з value, left та right
#         pass

# def inorder_traversal(root):
#     # Використовуйте рекурсію для симетричного обходу дерева
#     pass

# Побудова бінарного дерева:
#         10
#        /  \\
#       5    15
#      / \\     \\
#     2   7     20
# def build_binary_tree():
#     pass

# root = build_binary_tree()
# result = inorder_traversal(root)
# print("Симетричний обхід:", result)

# Правильний код
# class BinaryNode:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right

# def inorder_traversal(root):
#     if root is None:
#         return []
#     return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)

# def build_binary_tree():
#     root = BinaryNode(10)
#     root.left = BinaryNode(5, BinaryNode(2), BinaryNode(7))
#     root.right = BinaryNode(15, None, BinaryNode(20))
#     return root

# root = build_binary_tree()
# result = inorder_traversal(root)
# print("Симетричний обхід:", result)



# ЗАВДАННЯ 3
# Реалізуйте функцію tree_height(root),
# яка обчислює висоту дерева. Висота
# визначається як кількість вузлів у
# найдовшому шляху від кореня до листя.

# Початковий код:
# def tree_height(root):
#     # Якщо вузол порожній, поверніть 0
#     # Рекурсивно обчисліть висоту для кожного піддерева та поверніть 1 + максимальну висоту
#     pass

# # Використайте дерево з Завдання 1
# root = build_tree()
# height = tree_height(root)
# print("Висота дерева:", height)


# Правильний код
# def tree_height(root):
#     if root is None:
#         return 0
#     if not root.children:
#         return 1
#     return 1 + max(tree_height(child) for child in root.children)


# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.children = []

# def build_tree():
#     root = TreeNode("A")
#     nodeB = TreeNode("B")
#     nodeC = TreeNode("C")
#     nodeD = TreeNode("D")
#     root.children = [nodeB, nodeC, nodeD]
#     nodeE = TreeNode("E")
#     nodeB.children.append(nodeE)
#     nodeF = TreeNode("F")
#     nodeG = TreeNode("G")
#     nodeD.children = [nodeF, nodeG]
#     return root

# root = build_tree()
# height = tree_height(root)
# print("Висота дерева:", height)



# ЗАВДАННЯ 4
# Реалізуйте функцію count_leaves(root), яка
# підраховує кількість листових вузлів (без дітей)
# у дереві. Використайте дерево, побудоване в Завданні 1.

# Початковий код:
# def count_leaves(root):
#     # Якщо вузол порожній, поверніть 0
#     # Якщо вузол не має дітей, поверніть 1
#     # Інакше рекурсивно підрахуйте листя для кожного нащадка
#     pass

# root = build_tree()
# leaves = count_leaves(root)
# print("Кількість листів у дереві:", leaves)

# Правильний код
# def count_leaves(root):
#     if root is None:
#         return 0
#     if not root.children:
#         return 1
#     return sum(count_leaves(child) for child in root.children)

# root = build_tree()
# leaves = count_leaves(root)
# print("Кількість листів у дереві:", leaves)