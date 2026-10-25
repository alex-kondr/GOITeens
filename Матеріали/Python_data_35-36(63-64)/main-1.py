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




# Задача 1. Підрахунок частоти символів у рядку
# Умова: Напишіть функцію, яка приймає рядок і повертає словник, де ключами є символи, а значеннями — кількість їх входжень у рядок.
# Приклад: "hello" -> {'h': 1, 'e': 1, 'l': 2, 'o': 1}

def count_characters(s: str) -> dict:
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count
# Тест:
print(count_characters("hello"))
# Виведе: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
# Чому хеш-таблиця: Пошук та оновлення кількості для кожного символу відбувається в середньому за $O(1)$, тому загальний час — $O(N)$.



# Задача 2. Пошук першого неповторюваного символу
# Умова: Знайдіть перший символ у рядку, який зустрічається лише один раз. Якщо такого немає — поверніть None.
# Приклад: "swiss" -> 'w'

def first_unique_char(s: str):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1

    for char in s:
        if counts[char] == 1:
            return char
    return None
# Тест:
print(first_unique_char("swiss"))  # 'w'
print(first_unique_char("aabb"))   # None



# Задача 3. Перевірка наявності дублікатів у списку
# Умова: Перевірте, чи містить список хоча б одне число, яке повторюється.
# Приклад: [1, 2, 3, 1] -> True, [1, 2, 3, 4] -> False

def has_duplicates(nums: list) -> bool:
    seen = set()  # Множина побудована на базі хеш-таблиці
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
# Тест:
print(has_duplicates([1, 2, 3, 1]))  # True
print(has_duplicates([1, 2, 3, 4]))  # False



# Задача 4. Сума двох чисел (Two Sum)
# Умова: Дано список цілих чисел nums і ціле число target. Знайдіть індекси двох чисел, сума яких дорівнює target.
# Приклад: nums = [2, 7, 11, 15], target = 9 -> (0, 1)

def two_sum(nums: list, target: int):
    prev_map = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in prev_map:
            return (prev_map[diff], i)

        prev_map[num] = i
    return None
# Тест:
print(two_sum([2, 7, 11, 15], 9))  # (0, 1)
# Чому хеш-таблиця: Замість вкладеного циклу з часом $O(N^2)$, перевірка diff in prev_map займає $O(1)$, що скорочує час виконання до $O(N)$.


# ????????????
# Задача 5. Перевірка на анаграму
# Умова: Напишіть функцію, яка перевіряє, чи є два рядки анаграмами (чи складаються з однакових літер у тій самій кількості).
# Приклад: "listen" і "silent" -> True

def is_anagram(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    counts = {}
    for char in s1:
        counts[char] = counts.get(char, 0) + 1

    for char in s2:
        if char not in counts or counts[char] == 0:
            return False
        counts[char] -= 1

    return True
# Тест:
print(is_anagram("listen", "silent"))  # True
print(is_anagram("rat", "car"))        # False



# Задача 6. Перетин двох списків (Спільні унікальні елементи)
# Умова: Знайдіть спільні елементи двох списків за лінійний час $O(N + M)$.
# Приклад: [1, 2, 2, 1] і [2, 2] -> [2]

def intersection(nums1: list, nums2: list) -> list:
    set1 = set(nums1)
    res = set()
    for num in nums2:
        if num in set1:
            res.add(num)
    return list(res)
# Тест:
print(intersection([1, 2, 2, 1], [2, 2]))  # [2]

#######################################################################################################

# Задача 7. Групування слів за довжиною
# Умова: Дано список слів. Згрупуйте їх у словник за кількістю літер.
# Приклад: ["cat", "dog", "apple", "home", "car"]
# -> {3: ['cat', 'dog', 'car'], 5: ['apple'], 4: ['home']}
def group_by_length(words: list) -> dict:
    groups = {}
    for word in words:
        length = len(word)
        if length not in groups:
            groups[length] = []
        groups[length].append(word)
    return groups
# Тест:
words = ["cat", "dog", "apple", "home", "car"]
print(group_by_length(words))



# Задача 8. Визначення переможця голосування
# Умова: Масив містить імена кандидатів, за яких віддали голоси. Знайдіть кандидата, який набрав найбільшу кількість голосів.
# Приклад: ["Олена", "Ігор", "Олена", "Андрій", "Ігор", "Олена"] -> "Олена"

def find_winner(votes: list) -> str:
    tally = {}
    for candidate in votes:
        tally[candidate] = tally.get(candidate, 0) + 1

    winner = max(tally, key=tally.get)
    return winner
# Тест:
votes = ["Олена", "Ігор", "Олена", "Андрій", "Ігор", "Олена"]
print(find_winner(votes))  # "Олена"



# Задача 9. Словник-перекладач (Заміна слів у реченні)
# Умова: Дано словник синонімів/перекладів. Замініть у реченні всі відомі слова відповідно до словника.
# Приклад:
# Словник: {"cat": "кіт", "dog": "пес"}
# Речення: "my cat and your dog" -> "my кіт and your пес"
def translate_sentence(sentence: str, dictionary: dict) -> str:
    words = sentence.split()
    translated_words = [dictionary.get(word, word) for word in words]
    return " ".join(translated_words)
# Тест:
vocab = {"cat": "кіт", "dog": "пес"}
text = "my cat and your dog"
print(translate_sentence(text, vocab))  # "my кіт and your пес"



# Задача 10. Телефонна книга (Клас з базовими операціями хеш-таблиці)
# Умова: Реалізуйте простий клас PhoneBook з методами add_contact(name, phone), get_phone(name) та delete_contact(name).
# Усі операції мають працювати за $O(1)$.

class PhoneBook:
    def __init__(self):
        self._book = {}

    def add_contact(self, name: str, phone: str):
        self._book[name] = phone

    def get_phone(self, name: str):
        return self._book.get(name, "Контакт не знайдено")

    def delete_contact(self, name: str) -> bool:
        if name in self._book:
            del self._book[name]
            return True
        return False
# Тест:
pb = PhoneBook()
pb.add_contact("Олексій", "+380501234567")
print(pb.get_phone("Олексій"))  # "+380501234567"
pb.delete_contact("Олексій")
print(pb.get_phone("Олексій"))  # "Контакт не знайдено"