# Методи відкритого адресування

# Лінійне зондування
def linear_probe(hash_table, key, m):
    index = key % m
    for i in range(m):
        pos = (index + i) % m
        if hash_table[pos] is None:
            return pos
    return None

# Квадратичне зондування
def quadratic_probe(hash_table, key, m, c1=1, c2=3):
    index = key % m
    for i in range(m):
        pos = (index + c1 * i + c2 * i * i) % m
        if hash_table[pos] is None:
            return pos
    return None

# Подвійне гешування
def double_hashing(hash_table, key, m):
    h1 = key % m
    h2 = 1 + (key % (m - 1))
    for i in range(m):
        pos = (h1 + i * h2) % m
        if hash_table[pos] is None:
            return pos
    return None


# ЗАВДАННЯ 1
# Реалізуйте функцію mod_hash_list(keys, m),
# яка приймає список чисел та параметр m (розмір геш‑таблиці).
# Обчисліть хеш‑значення для кожного ключа за формулою: h(k) = k mod m
# Проведіть тестування для заданого списку ключів.

def mod_hash_list(keys, m):
    # Обчисліть хеш‑значення для кожного ключа за формулою h(k) = k mod m
    pass

keys = [123, 456, 789, 101112, 131415, 161718]
m = 10
print("Модульне гешування (m=10):", mod_hash_list(keys, m))

# Правильний код:
def mod_hash_list(keys, m):
    return [key % m for key in keys]


# ЗАВДАННЯ 2
# Дано функцію analyze_mod_hash. Доповніть її так,
# щоб вона виводила всі ключі що колізують (мають однакове хеш-значення).

# import matplotlib.pyplot as plt

# def analyze_mod_hash(keys, m):
#     hash_values = [key % m for key in keys]

#     plt.hist(hash_values, bins=range(m + 1), edgecolor='black', align='left')
#     plt.title("Гістограма розподілу хеш-значень (модульне гешування)")
#     plt.xlabel("Хеш-значення")
#     plt.ylabel("Частота")
#     plt.show()

#     # Ваше завдання: знайдіть та виведіть колізії
#     # Підказка: використайте словник де ключ — хеш, значення — список ключів
#     collisions = {}
#     for key in keys:
#         h = key % m
#         # ... доповніть тут

#     for h, bucket in collisions.items():
#         if len(bucket) > 1:
#             print(f"h={h}: {bucket}")

# keys = list(range(1, 30))  # невеликий список щоб зручно читати
# m = 7
# analyze_mod_hash(keys, m)


# class HashTable:
#     def __init__(self, size=10):
#         self.size = size
#         self.table = [None] * self.size
#         self.count = 0
#         self.load_factor_threshold = 0.7

#     def _hash(self, key):
#         return hash(key) % self.size

#     def _probe(self, key):
#         idx = self._hash(key)
#         for i in range(self.size):
#             slot = (idx + i) % self.size
#             if self.table[slot] is None or self.table[slot] == "DELETED":
#                 return slot
#             if self.table[slot][0] == key:
#                 return slot
#         return None

#     def _resize(self):
#         old_table = self.table
#         self.size *= 2
#         self.table = [None] * self.size
#         self.count = 0
#         print(f"  [resize] таблицю розширено до {self.size}")
#         for slot in old_table:
#             if slot is not None and slot != "DELETED":
#                 self.insert(slot[0], slot[1])

#     def insert(self, key, value):
#         if self.count / self.size >= self.load_factor_threshold:
#             self._resize()

#         idx = self._hash(key)
#         slot = self._probe(key)

#         if slot is None:
#             raise Exception("Хеш-таблиця переповнена")

#         if self.table[slot] is None or self.table[slot] == "DELETED":
#             if self.table[idx] is not None and self.table[idx] != "DELETED" \
#                     and self.table[idx][0] != key:
#                 print(f"  [колізія] '{key}' → слот {idx} зайнятий '{self.table[idx][0]}', "
#                       f"розміщено у слоті {slot}")
#             self.table[slot] = (key, value)
#             self.count += 1
#         else:
#             self.table[slot] = (key, value)

#     def search(self, key):
#         idx = self._hash(key)
#         for i in range(self.size):
#             slot = (idx + i) % self.size
#             if self.table[slot] is None:
#                 return None
#             if self.table[slot] != "DELETED" and self.table[slot][0] == key:
#                 return self.table[slot][1]
#         return None

#     def remove(self, key):
#         idx = self._hash(key)
#         for i in range(self.size):
#             slot = (idx + i) % self.size
#             if self.table[slot] is None:
#                 return False
#             if self.table[slot] != "DELETED" and self.table[slot][0] == key:
#                 self.table[slot] = "DELETED"
#                 self.count -= 1
#                 return True
#         return False

#     def __str__(self):
#         lines = []
#         for i, slot in enumerate(self.table):
#             if slot is not None and slot != "DELETED":
#                 lines.append(f"  [{i}] {slot[0]!r}: {slot[1]}")
#         return "\n".join(lines) if lines else "  (порожньо)"

# ht = HashTable(size=10)
# print("=== Вставка ===")
# ht.insert("apple", 100)
# ht.insert("banana", 200)
# ht.insert("orange", 150)
# ht.insert("grape", 90)
# ht.insert("gfjfj", 100)
# ht.insert("g44jfj", 100)
# ht.insert("gjfj", 100)

# print("\nГеш-таблиця:")
# print(ht)

# print("\n=== Пошук ===")
# print("Пошук 'orange':", ht.search("orange"))
# print("Пошук 'cherry':", ht.search("cherry"))

# print("\n=== Видалення ===")
# ht.remove("orange")
# print("Після видалення 'orange':")
# print(ht)




# =====================================================================
# ЗАДАЧІ ДЛЯ ЗАКРІПЛЕННЯ: ВІДКРИТЕ АДРЕСУВАННЯ
# (Лінійне зондування, Квадратичне зондування, Подвійне гешування)
# =====================================================================

# Задача 1. Вставка елемента за допомогою лінійного зондування
# Умова: Напишіть функцію insert_linear(table, key, m), яка знаходить вільний слот
# для ключа за формулою: pos = (key % m + i) % m і записує його в таблицю.
# Повертає індекс куди збережено ключ або -1, якщо таблиця повна.

def insert_linear(table: list, key: int, m: int) -> int:
    index = key % m
    for i in range(m):
        pos = (index + i) % m
        if table[pos] is None or table[pos] == "DELETED":
            table[pos] = key
            return pos
    return -1

# Тест:
# table1 = [None] * 5
# insert_linear(table1, 10, 5)  # 10 % 5 = 0 -> індекс 0
# insert_linear(table1, 15, 5)  # колізія в 0 -> йде у слот 1
# print("Задача 1. Таблиця після вставки:", table1)  # [10, 15, None, None, None]



# ?????????????????????????
# Задача 2. Підрахунок кількості колізій при лінійному зондуванні
# Умова: Напишіть функцію count_linear_collisions(keys, m), яка вставляє ключі
# та рахує сумарну кількість колізій (кроків зміщення, коли початковий слот уже зайнятий).

def count_linear_collisions(keys: list, m: int) -> int:
    table = [None] * m
    total_collisions = 0

    for key in keys:
        idx = key % m
        for i in range(m):
            pos = (idx + i) % m
            if table[pos] is None:
                table[pos] = key
                total_collisions += i  # i кроків зміщення = i колізій
                break
    return total_collisions

# Тест:
# print("Задача 2. Колізій:", count_linear_collisions([5, 10, 15], 5))  # 0 + 1 + 2 = 3 колізії



# Задача 3. Пошук ключа в хеш-таблиці з лінійним зондуванням
# Умова: Напишіть функцію search_linear(table, key, m), яка повертає індекс знайденого
# ключа або -1, якщо ключ відсутній. Пошук зупиняється, якщо зустріли порожній слот None.

def search_linear(table: list, key: int, m: int) -> int:
    idx = key % m
    for i in range(m):
        pos = (idx + i) % m
        if table[pos] is None:
            return -1
        if table[pos] == key:
            return pos
    return -1

# Тест:
# t3 = [10, 15, None, None, 4]
# print("Задача 3. Пошук 15:", search_linear(t3, 15, 5))  # індекс 1
# print("Задача 3. Пошук 20:", search_linear(t3, 20, 5))  # -1 (немає)



# Задача 4. Генерація послідовності індексів для квадратичного зондування
# Умова: Напишіть функцію get_quadratic_probe_sequence(key, m, c1, c2, steps),
# яка повертає список із перших steps індексів за формулою:
# pos = (key % m + c1 * i + c2 * i^2) % m

def get_quadratic_probe_sequence(key: int, m: int, c1: int = 1, c2: int = 3, steps: int = 5) -> list:
    idx = key % m
    sequence = []
    for i in range(steps):
        pos = (idx + c1 * i + c2 * i * i) % m
        sequence.append(pos)
    return sequence

# Тест:
# print("Задача 4. Послідовність індексів:", get_quadratic_probe_sequence(key=7, m=11, c1=1, c2=3, steps=4))
# i=0: 7; i=1: (7+1+3)%11=0; i=2: (7+2+12)%11=10; i=3: (7+3+27)%11=4 -> [7, 0, 10, 4]



# Задача 5. Вставка з квадратичним зондуванням
# Умова: Реалізуйте функцію insert_quadratic(table, key, m, c1, c2), яка вставляє ключ
# за квадратичним правилом і повертає кінцевий індекс або -1, якщо вільний слот не знайдено.

def insert_quadratic(table: list, key: int, m: int, c1: int = 1, c2: int = 1) -> int:
    idx = key % m
    for i in range(m):
        pos = (idx + c1 * i + c2 * i * i) % m
        if table[pos] is None or table[pos] == "DELETED":
            table[pos] = key
            return pos
    return -1

# Тест:
# t5 = [None] * 7
# insert_quadratic(t5, 7, 7, c1=1, c2=1)   # 7 % 7 = 0 -> слот 0
# insert_quadratic(t5, 14, 7, c1=1, c2=1)  # 14 % 7 = 0 -> i=1: (0 + 1 + 1) % 7 = 2
# print("Задача 5. Таблиця (квадратичне зондування):", t5)  # [7, None, 14, None, None, None, None]



# Задача 6. Обчислення кроку для подвійного гешування
# Умова: При подвійному гешуванні h2(k) визначає розмір кроку і не повинен дорівнювати 0.
# Напишіть функцію get_hash2_step(key, R), де h2(k) = R - (key % R).
# Перевірте, чи результат завжди знаходиться в діапазоні [1, R].

def get_hash2_step(key: int, R: int) -> int:
    return R - (key % R)

# Тест:
# print("Задача 6. Кроки h2 для R=7:")
# for k in [7, 14, 15, 20]:
#     print(f"  key={k} -> крок={get_hash2_step(k, 7)}")
# Завжди >= 1, отже зациклення на одному місці неможливе!



# Задача 7. Вставка методом подвійного гешування
# Умова: Реалізуйте insert_double_hashing(table, key, m).
# h1(k) = k % m
# h2(k) = 1 + (key % (m - 1))
# pos = (h1 + i * h2) % m

def insert_double_hashing(table: list, key: int, m: int) -> int:
    h1 = key % m
    h2 = 1 + (key % (m - 1))
    for i in range(m):
        pos = (h1 + i * h2) % m
        if table[pos] is None or table[pos] == "DELETED":
            table[pos] = key
            return pos
    return -1

# Тест:
# t7 = [None] * 7
# insert_double_hashing(t7, 7, 7)   # h1 = 0, h2 = 1 + (7%6) = 2 -> слот 0
# insert_double_hashing(t7, 14, 7)  # h1 = 0 (колізія), h2 = 1 + (14%6) = 3 -> i=1: (0 + 3) % 7 = 3
# print("Задача 7. Таблиця (подвійне гешування):", t7)  # [7, None, None, 14, None, None, None]



# Задача 8. Порівняння розподілу трьох методів при однакових колізіях
# Умова: Маємо m = 11 і ключі [11, 22, 33], що мають однаковий h(k) = 0.
# Напишіть функцію compare_methods(keys, m), яка показує позиції для кожного методу.

def compare_methods(keys: list, m: int):
    # 1. Лінійне: (0 + i) % m
    lin_slots = []
    t_lin = [None] * m
    for k in keys:
        for i in range(m):
            pos = (k % m + i) % m
            if t_lin[pos] is None:
                t_lin[pos] = k
                lin_slots.append(pos)
                break

    # 2. Квадратичне: (0 + 1*i + 1*i^2) % m
    quad_slots = []
    t_quad = [None] * m
    for k in keys:
        for i in range(m):
            pos = (k % m + i + i * i) % m
            if t_quad[pos] is None:
                t_quad[pos] = k
                quad_slots.append(pos)
                break

    # 3. Подвійне: (0 + i * (1 + k % (m - 1))) % m
    double_slots = []
    t_double = [None] * m
    for k in keys:
        h1 = k % m
        h2 = 1 + (k % (m - 1))
        for i in range(m):
            pos = (h1 + i * h2) % m
            if t_double[pos] is None:
                t_double[pos] = k
                double_slots.append(pos)
                break

    return {"Лінійне": lin_slots, "Квадратичне": quad_slots, "Подвійне": double_slots}

# Тест:
print("Задача 8. Порівняння слотів для ключів [11, 22, 33]:")
res = compare_methods([11, 22, 33], 11)
for method, slots in res.items():
    print(f"  {method}: {slots}")



# Задача 9. Видалення елемента з лінійним зондуванням (маркер "DELETED")
# Умова: Напишіть функцію delete_linear(table, key, m). Якщо знайдено ключ,
# замініть його на "DELETED" і поверніть True. Не можна ставити None,
# інакше розірветься ланцюг пошуку для інших елементів!

def delete_linear(table: list, key: int, m: int) -> bool:
    idx = key % m
    for i in range(m):
        pos = (idx + i) % m
        if table[pos] is None:
            return False  # дійшли до порожнього слота — елемента немає
        if table[pos] == key:
            table[pos] = "DELETED"
            return True
    return False

# Тест:
# t9 = [10, 15, 20, None, None]  # 15 та 20 колізували на слоті 0 і пішли далі
# delete_linear(t9, 15, 5)
# print("Задача 9. Таблиця після видалення 15:", t9)  # [10, 'DELETED', 20, None, None]
# # Перевірка пошуку 20 крізь 'DELETED':
# print("  Чи знайдено 20 після видалення 15?:", search_linear(t9, 20, 5) != -1)



# Задача 10. Розрахунок коефіцієнта завантаження (Load Factor)
# Умова: Напишіть функцію check_load_factor(table, threshold=0.7), яка рахує
# коефіцієнт завантаження α = count / size (де count — кількість реальних ключів,
# без None та DELETED) і повідомляє, чи потрібне розширення (resize/rehash).

def check_load_factor(table: list, threshold: float = 0.7) -> dict:
    total_slots = len(table)
    occupied_slots = sum(1 for slot in table if slot is not None and slot != "DELETED")
    load_factor = occupied_slots / total_slots if total_slots > 0 else 0.0
    needs_resize = load_factor >= threshold

    return {
        "occupied": occupied_slots,
        "total": total_slots,
        "load_factor": round(load_factor, 2),
        "needs_resize": needs_resize
    }

# Тест:
# t10 = [1, 2, "DELETED", 4, None, None, None, None, None, None]  # 3 елементи з 10
# print("Задача 10. Аналіз завантаження 1:", check_load_factor(t10))
# t10_full = [1, 2, 3, 4, 5, 6, 7, None, None, None]             # 7 з 10 (0.7)
# print("Задача 10. Аналіз завантаження 2:", check_load_factor(t10_full))




