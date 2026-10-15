# index = key % m - модульне хешування
# index = m * (k * A mod 1) - мультиплікативне хешування

# Створюємо клас HashTable, який реалізує геш-таблицю
# за допомогою методу ланцюгів (chaining) для вирішення колізій.
# class HashTable:
#     def __init__(self, size=10):
#         self.size = size
#         self.table = [[] for _ in range(self.size)]

#     def _hash(self, key):
#         return hash(key) % self.size

#     def insert(self, key, value):
#         idx = self._hash(key)
#         self.table[idx].append((key, value))

#     def search(self, key):
#         idx = self._hash(key)
#         for element in self.table[idx]:
#             if element[0] == key:
#                 return element[1]

#     def remove(self, key):
#         idx = self._hash(key)
#         for i in range(len(self.table[idx])):
#             if self.table[idx][i][0] == key:
#                 del self.table[idx][i]

#     def __str__(self):
#         return str(self.table)


# ht = HashTable(size=10)
# ht.insert("apple", 100)
# ht.insert("banana", 200)
# ht.insert("orange", 150)
# ht.insert("grape", 90)

# print("Геш-таблиця:")
# print(ht)

# print("\nПошук 'banana':", ht.search("banana"))
# print("Пошук 'cherry':", ht.search("cherry"))

# ht.remove("orange")
# print("\nПісля видалення 'orange':")
# print(ht)


# ЗАВДАННЯ 1
# Реалізуйте клас HashTable з мультиплікативним хешуванням та методами для роботи з таблицею.
# A = 0.6180339887
# Підказка:
# h(k) = math.floor(m × (k × A mod 1))

import math

class HashTable:
    def __init__(self, size=10) -> None:
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        k = abs(hash(key)) % (2**32)
        normalize_k = k / (2**32)
        return math.floor(self.size * ((normalize_k * 0.618) % 1))

    def insert(self, key, value):
        idx = self._hash(key)
        self.table[idx].append((key, value))

    def search(self, key):
        idx = self._hash(key)
        for el in self.table[idx]:
            if el[0] == key:
                return el[1]

    def delete(self, key):
        idx = self._hash(key)
        for i in range(len(self.table[idx])):
            if self.table[idx][i][0] == key:
                value = self.table[idx][i][1]
                del self.table[idx][i]
                return value

    def __str__(self):
        return str(self.table)

# ht = HashTable(size=10)
# ht.insert("apple", 100)
# ht.insert("banana", 200)
# ht.insert("orange", 150)
# ht.insert("grape", 90)

# print("Геш-таблиця:")
# print(ht)

# print("\nПошук 'banana':", ht.search("banana"))
# print("Пошук 'cherry':", ht.search("cherry"))

# print(ht.delete("orange"))
# print("\nПісля видалення 'orange':")
# print(ht)