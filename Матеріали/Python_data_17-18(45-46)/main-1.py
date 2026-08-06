# Концепція FIFO - черги (First In, First Out - перший прийшов - перший вийшов)
# Лінійний алгоритм, де всі елементи обробляються в порядку надходження


# class Queue:
#     def __init__(self):
#         self.items = []

#     def enqueue(self, item):
#         self.items.append(item)

#     def dequeue(self):
#         if not self.is_empty():
#             return self.items.pop(0)
#         else:
#             return None

#     def is_empty(self):
#         return len(self.items) == 0

#     def peek(self):
#         if not self.is_empty():
#             return self.items[0]
#         else:
#             return None

#     def size(self):
#         return len(self.items)


# import time
# from collections import deque
# import random


# class Car:
#     def __init__(self, car_id):
#         self.car_id = car_id

#     def __str__(self):
#         return f"Car-{self.car_id}"


# class TrafficLight:
#     def __init__(self, green_time=3, red_time=3):
#         self.green_time = green_time
#         self.red_time = red_time
#         self.is_green = True
#         self.elapsed = 0

#     def update(self):
#         self.elapsed += 1
#         if self.is_green and self.elapsed >= self.green_time:
#             self.is_green = False
#             self.elapsed = 0
#         elif not self.is_green and self.elapsed >= self.red_time:
#             self.is_green = True
#             self.elapsed = 0


# def simulate_traffic(duration=100, car_arrival_probability=0.4):
#     queue = deque()
#     car_counter = 1
#     traffic_light = TrafficLight(green_time=3, red_time=2)

#     for second in range(duration):
#         if random.random() < car_arrival_probability:
#             car = Car(car_counter)
#             queue.append(car)
#             print(f"[Time={second}s] Car {car} arrived -> Queue size is {len(queue)}")
#             car_counter += 1

#         traffic_light.update()

#         if traffic_light.is_green and queue:
#             leaving_car = queue.popleft()
#             print(f"[Time={second}s] *** Car {leaving_car} PASSED the light *** -> Queue size is {len(queue)}")

#         time.sleep(0.5)


# if __name__ == "__main__":
#     simulate_traffic()


# ЗАВДАННЯ 1
# Уявімо, що ви розробляєте спрощену систему обробки звернень
# до служби підтримки. Кожен новий запит потрапляє у чергу,
# і оператор обробляє ці звернення по одному, у порядку надходження.
# class SupportQueue:
#     def __init__(self):
#         self.items = []

#     def enqueue(self, ticket):
#         # Додайте код для постановки ticket у кінець черги
#         ...

#     def dequeue(self):
#         # Додайте код для вилучення першого елемента з черги
#         ...

#     def is_empty(self):
#         return len(self.items) == 0

#     def size(self):
#         return len(self.items)

# support = SupportQueue()

# support.enqueue("Issue #101")
# support.enqueue("Issue #102")
# support.enqueue("Issue #103")
# print("Кількість запитів:", support.size())
# handled = support.dequeue()
# print("Оброблено:", handled)
# print("Залишилося:", support.size())


# ЗАВДАННЯ 2
# У корпоративному чаті повідомлення від
# користувачів надходять одне за одним і
# тимчасово складаються у буфер (чергу), перш
# ніж система їх розподілить. Необхідно
# реалізувати цю логіку із затримкою — наприклад,
# щоб кожне отримане повідомлення “прочиталося” за секунду.
# import time

# class MessageQueue:
#     def __init__(self):
#         self.queue = []

#     def enqueue(self, msg):
#         # Додайте нове повідомлення в кінець черги
#         ...

#     def dequeue(self):
#         # Якщо черга не порожня, поверніть перший елемент і вилучіть його
#         ...

#     def is_empty(self):
#         return len(self.queue) == 0

# chat_buffer = MessageQueue()
# # Додайте три повідомлення у різний час

# time.sleep(0.5)
# #
# time.sleep(0.5)
# #

# while not chat_buffer.is_empty():
#     msg = chat_buffer.dequeue()
#     print("Обробляємо:", msg)
#     time.sleep(1)


# ЗАВДАННЯ 3
# Припустимо, у нас є список завдань із різним
# «рівнем важливості».
# Однак спочатку нехай усі завдання обробляються
# просто в порядку надходження, без урахування пріоритету.
# За потреби потім можемо модифікувати, щоби завдання з
# вищим пріоритетом ішло раніше (але це вже інша
# структура — пріоритетна черга). Для початку ж —
# чистий FIFO.

# class Task:
#     def __init__(self, name, priority):
#         self.name = name
#         self.priority = priority

#     def __str__(self):
#         return f"Task({self.name}, priority={self.priority})"

# class TaskQueue:
#     def __init__(self):
#         self.items = []

#     def enqueue(self, task):
#         ...

#     def dequeue(self):
#         ...

#     def is_empty(self):
#         return len(self.items) == 0

# task_queue = TaskQueue()
# #Додайте завдання з різними priority 2,1,3

# while not task_queue.is_empty():
#     current_task = task_queue.dequeue()
#     print("Виконуємо:", current_task)


# ЗАВДАННЯ 4
# Є лабораторна система, де формується черга
# документів на аналіз. Наприклад, PDF-файли
# чи будь-які інші файли надходять послідовно
# та стають у чергу, поки не доходить черга
# до аналізатора, котрий бере перший документ і «перевіряє» його.

# import random

# class DocumentQueue:
#     def __init__(self):
#         self.docs = []

#     def enqueue(self, doc):
#         ...

#     def dequeue(self):
#         ...

#     def size(self):
#         return len(self.docs)

# doc_queue = DocumentQueue()
# doc_types = ["PDF", "DOC", "IMG", "TXT"]

# for i in range(5):
#     doc_type = random.choice(doc_types)
#     doc_name = f"File_{i}.{doc_type.lower()}"
#     doc_queue.enqueue(doc_name)
#     print("Надійшов документ:", doc_name)

# print("Загальна кількість документів:", doc_queue.size())

# while doc_queue.size() > 0:
#     current_doc = doc_queue.dequeue()
#     print(f"Обробляємо: {current_doc}")


