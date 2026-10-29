# Алгоритм Хаффмана
# Першим кроком є сортування всіх активностей за їх часом завершення у зростаючому порядку.
# Ідея полягає в тому, що активність, яка завершується раніше, залишає більше часу для проведення наступних активностей.

# Приклад:
# Припустимо, у нас є 5 активностей з наступними часами початку та завершення:

# Активність 1: (1, 4)
# Активність 2: (3, 5)
# Активність 3: (0, 6)
# Активність 4: (5, 7)
# Активність 5: (8, 9)
# Спочатку відсортуємо активності за часом завершення:

# (1, 4)
# (3, 5)
# (0, 6)
# (5, 7)
# (8, 9)

# Вибираємо першу активність (1, 4). Далі, серед решти, перша активність,
# що починається не раніше за 4 — це (5, 7). Нарешті, (8, 9) починається після
# завершення (5, 7). Таким чином, оптимальний набір активностей — [(1, 4), (5, 7), (8, 9)].


# Алгоритм Хаффмана — це метод стиснення даних,
# який створює оптимальний префіксний код
# на основі частот символів у вхідних даних.
# Основна ідея алгоритму полягає в тому,
# щоб символи з більш високою частотою отримували
# коротші коди, а символи з низькою — довші,
# таким чином зменшуючи загальну довжину закодованого повідомлення.


# Реалізація алгоритму Хаффмана

import heapq
from collections import defaultdict


class HuffmanNode:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1

    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, merged)

    return heap[0] if heap else None


def build_codes(node, current_code="", codes={}):
    if node is None:
        return

    if node.char is not None:
        codes[node.char] = current_code
        return

    build_codes(node.left, current_code + "0", codes)
    build_codes(node.right, current_code + "1", codes)
    return codes


# Функція huffman_encode перетворює текст у
# його закодовану за Хаффманом форму, використовуючи словник кодів.
def huffman_encode(text, codes):
    return ''.join(codes[char] for char in text)


def huffman_decode(encoded_text, root):
    decoded_text = ""
    current = root
    for bit in encoded_text:
        if bit == '0':
            current = current.left
        else:
            current = current.right

        if current.char is not None:
            decoded_text += current.char
            current = root
    return decoded_text


# if __name__ == "__main__":
#     text = "this is an example for huffman encoding"
#     huffman_tree = build_huffman_tree(text)
#     codes = build_codes(huffman_tree)
#     print("Коди Хаффмана для символів:")
#     for char, code in codes.items():
#         print(f"'{char}': {code}")

#     encoded_text = huffman_encode(text, codes)
#     print("\nЗакодований текст:")
#     print(encoded_text)

#     decoded_text = huffman_decode(encoded_text, huffman_tree)
#     print("\nДекодований текст:")
#     print(decoded_text)


# ПРАКТИЧНЕ ЗАВДАННЯ 1
# Розробіть функцію, яка не лише знаходить мінімальну
# кількість монет для здачі суми, а й повертає кількість використаних монет кожного типу.

def coin_change(coins, amount):
    # Ініціалізуйте словник для підрахунку кількості монет кожного номіналу
    # Реалізуйте жадібний алгоритм, що зменшує amount і оновлює лічильник
    pass

# coins = [25, 10, 5, 1]
# amount = 63
# print("Монети для здачі:", coin_change(coins, amount))

# Правильний код
def coin_change(coins, amount):
    result = {}
    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count
    return result if amount == 0 else {}

# coins = [25, 10, 5, 1]
# amount = 63
# print("Монети для здачі:", coin_change(coins, amount))


# ПРАКТИЧНЕ ЗАВДАННЯ 2
# Розширте реалізацію алгоритму Хаффмана, додавши
# функцію для обчислення середньої довжини кодових слів на основі частот символів.

def average_code_length(text, codes):
    # Обчисліть сумарну довжину коду, помноживши довжину коду символа на його частоту
    pass

# text = "this is an example for huffman encoding"
# tree = build_huffman_tree(text)
# codes = build_codes(tree)
# avg_length = average_code_length(text, codes)
# print("Середня довжина кодового слова:", avg_length)

# Правильний код

# from collections import Counter

# def average_code_length(text, codes):
#     frequency = Counter(text)
#     total_chars = len(text)
#     total_bits = sum(len(codes[char]) * freq for char, freq in frequency.items())
#     return total_bits / total_chars

# text = "this is an example for huffman encoding"
# tree = build_huffman_tree(text)
# codes = build_codes(tree)
# avg_length = average_code_length(text, codes)
# print("Середня довжина кодового слова:", avg_length)



# ПРАКТИЧНЕ ЗАВДАННЯ 3
# Розробіть функцію select_projects(projects), яка приймає
# список проектів у вигляді кортежів (project_id, deadline, profit)
# та використовує жадібний алгоритм для вибору проектів із
# максимальним загальним прибутком. Додатково функція має виводити список обраних проектів з їх дедлайнами.

# def select_projects(projects):
#     # Сортуйте проекти за спаданням прибутку
#     # Використовуйте жадібний підхід для розміщення проектів в оптимальний розклад
#     pass

# # Тестовий приклад
# projects = [("P1", 4, 50), ("P2", 2, 30), ("P3", 1, 20), ("P4", 3, 40)]
# print("Вибрані проекти та загальний прибуток:", select_projects(projects))


# Правильний код

# def select_projects(projects):
#     projects.sort(key=lambda x: x[2], reverse=True)
#     max_deadline = max(project[1] for project in projects)
#     schedule = [None] * max_deadline
#     total_profit = 0
#     for project in projects:
#         project_id, deadline, profit = project
#         for slot in range(min(deadline, max_deadline)-1, -1, -1):
#             if schedule[slot] is None:
#                 schedule[slot] = project_id
#                 total_profit += profit
#                 break
#     return schedule, total_profit

# projects = [("P1", 4, 50), ("P2", 2, 30), ("P3", 1, 20), ("P4", 3, 40)]
# schedule, total_profit = select_projects(projects)
# print("Вибрані проекти:", schedule)
# print("Загальний прибуток:", total_profit)