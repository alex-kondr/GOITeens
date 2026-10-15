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


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size
        self.count = 0
        self.load_factor_threshold = 0.7

    def _hash(self, key):
        return hash(key) % self.size

    def _probe(self, key):
        idx = self._hash(key)
        for i in range(self.size):
            slot = (idx + i) % self.size
            if self.table[slot] is None or self.table[slot] == "DELETED":
                return slot  # вільний слот
            if self.table[slot][0] == key:
                return slot  # ключ вже існує
        return None  # таблиця повна

    def _resize(self):
        old_table = self.table
        self.size *= 2
        self.table = [None] * self.size
        self.count = 0
        print(f"  [resize] таблицю розширено до {self.size}")
        for slot in old_table:
            if slot is not None and slot != "DELETED":
                self.insert(slot[0], slot[1])

    def insert(self, key, value):
        if self.count / self.size >= self.load_factor_threshold:
            self._resize()

        idx = self._hash(key)
        slot = self._probe(key)

        if slot is None:
            raise Exception("Хеш-таблиця переповнена")

        # Перевірка колізії — інший ключ займає початковий слот
        if self.table[slot] is None or self.table[slot] == "DELETED":
            if self.table[idx] is not None and self.table[idx] != "DELETED" \
                    and self.table[idx][0] != key:
                print(f"  [колізія] '{key}' → слот {idx} зайнятий '{self.table[idx][0]}', "
                      f"розміщено у слоті {slot}")
            self.table[slot] = (key, value)
            self.count += 1
        else:
            self.table[slot] = (key, value)

    def search(self, key):
        idx = self._hash(key)
        for i in range(self.size):
            slot = (idx + i) % self.size
            if self.table[slot] is None:
                return None  # ключ точно відсутній
            if self.table[slot] != "DELETED" and self.table[slot][0] == key:
                return self.table[slot][1]
        return None

    def remove(self, key):
        idx = self._hash(key)
        for i in range(self.size):
            slot = (idx + i) % self.size
            if self.table[slot] is None:
                return False
            if self.table[slot] != "DELETED" and self.table[slot][0] == key:
                self.table[slot] = "DELETED"  # ледаче видалення
                self.count -= 1
                return True
        return False

    def __str__(self):
        lines = []
        for i, slot in enumerate(self.table):
            if slot is not None and slot != "DELETED":
                lines.append(f"  [{i}] {slot[0]!r}: {slot[1]}")
        return "\n".join(lines) if lines else "  (порожньо)"

ht = HashTable(size=10)
print("=== Вставка ===")
ht.insert("apple", 100)
ht.insert("banana", 200)
ht.insert("orange", 150)
ht.insert("grape", 90)
ht.insert("gfjfj", 100)
ht.insert("g44jfj", 100)
ht.insert("gjfj", 100)

print("\nГеш-таблиця:")
print(ht)

print("\n=== Пошук ===")
print("Пошук 'orange':", ht.search("orange"))
print("Пошук 'cherry':", ht.search("cherry"))

print("\n=== Видалення ===")
ht.remove("orange")
print("Після видалення 'orange':")
print(ht)



