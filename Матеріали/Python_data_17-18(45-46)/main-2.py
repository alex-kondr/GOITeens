# Концепція LIFO (Last In, First Out) (остання дія — перша відміняється)
# Стек — це лінійна структура даних,
# що реалізує принцип «останній
# прийшов — перший пішов» (англійською LIFO: Last In, First Out).


# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         return None

#     def is_empty(self):
#         return len(self.items) == 0

#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
#         return None

#     def size(self):
#         return len(self.items)


# s = Stack()
# print("Порожній на початку?", s.is_empty())

# s.push("Перший")
# s.push("Другий")
# s.push("Третій")

# print("Розмір після додавання 3-х елементів:", s.size())
# print("Порожній зараз?", s.is_empty())
# print("Верхівка стека:", s.peek())

# top = s.pop()
# print("Зняли з вершини:", top)
# print("Нова верхівка:", s.peek())

# --------------------------------
# import time
# import random


# class TextAction:
#     def __init__(self, content):
#         self.content = content

#     def __str__(self):
#         return f"Action: {self.content}"


# class UndoStack:
#     def __init__(self):
#         self.items = []

#     def push(self, action):
#         self.items.append(action)

#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         return None

#     def is_empty(self):
#         return len(self.items) == 0

#     def size(self):
#         return len(self.items)


# def simulate_editor(duration=10, undo_probability=0.3):
#     stack = UndoStack()
#     line_counter = 1

#     for sec in range(duration):
#         if random.random() < undo_probability and not stack.is_empty():
#             undone_action = stack.pop()
#             print(f"[t={sec}s] UNDO -> {undone_action}")
#         else:
#             new_line = TextAction(f"Рядок {line_counter}")
#             stack.push(new_line)
#             print(f"[t={sec}s] Додано дію -> {new_line}")
#             line_counter += 1

#         time.sleep(0.5)

#     print("\\nЗалишилися дії у стеці (зверху вниз):")
#     while not stack.is_empty():
#         top = stack.pop()
#         print(top)
# --------------------------------


# ЗАВДАННЯ 1
# У браузері можна зберігати історію відвіданих
# сторінок у вигляді стека: коли ви переходите
# на нову сторінку, вона “накладається” поверх
# попередньої. Якщо натиснути “Назад” (Back),
# ми вилучимо з вершини останню сторінку й повернемося до тієї, що була раніше.

# class BrowserHistory:
#     def __init__(self):
#         self.history = []

#     def visit(self, url):
#         # Додайте код для "зайти" на нову сторінку (push)
#         ...

#     def back(self):
#         # Додайте код для повернення (pop) на попередню сторінку
#         ...

#     def current_page(self):
#         # Визначте, яка сторінка зараз на "верхівці" (peek) або None, якщо історія порожня
#         ...

#     def size(self):
#         return len(self.history)

# browser = BrowserHistory()
# browser.visit("google.com")
# browser.visit("wikipedia.org")
# browser.visit("stackoverflow.com")
# print("Поточна сторінка:", browser.current_page())
# browser.back()
# print("Після натискання BACK, сторінка:", browser.current_page())


# ЗАВДАННЯ 2
# У графічному редакторі кожен крок (наприклад,
# малювання лінії, заливка кольором) може зберігатися
# у стек. Кнопка «Undo» дозволяє видалити останню зроблену дію.

# class EditorAction:
#     def __init__(self, description):
#         self.description = description

#     def __str__(self):
#         return f"Action: {self.description}"

# class ActionStack:
#     def __init__(self):
#         self.stack = []

#     def push(self, action):
#         # Додайте операцію вставки зверху
#         ...

#     def pop(self):
#         # Вилучайте верхній елемент, якщо він існує
#         ...

#     def peek(self):
#         # Перевірте верхній елемент без вилучення
#         ...

#     def is_empty(self):
#         return len(self.stack) == 0
# actions = ActionStack()
# actions.push(EditorAction("Draw line"))
# actions.push(EditorAction("Fill color"))
# print("Остання дія:", actions.peek())
# last = actions.pop()
# print("Скасовано:", last)
# print("Нова верхівка:", actions.peek())


# ЗАВДАННЯ 3
# Коли викликається функція, її контекст
# додається у стек викликів. Коли функція
# завершується, цей контекст знімається з
# вершини. Нижче наведений “спрощений”
# код, де кожен виклик функції будемо
# вручну кладемо у стек, а завершення зніматиме його.

# import time

# class CallFrame:
#     def __init__(self, function_name, level):
#         self.function_name = function_name
#         self.level = level

#     def __str__(self):
#         return f"Call to {self.function_name}, recursion level={self.level}"

# class CallStack:
#     def __init__(self):
#         self.frames = []

#     def push(self, frame):
#         # Додайте frame у вершину
#         ...

#     def pop(self):
#         # Зніміть верхній фрейм
#         ...

#     def is_empty(self):
#         return len(self.frames) == 0

# def simulate_recursion(call_stack, func_name, depth):
#     if depth == 0:
#         return
#     frame = CallFrame(func_name, depth)
#     call_stack.push(frame)
#     print("Входимо у:", frame)
#     time.sleep(0.3)
#     simulate_recursion(call_stack, func_name, depth - 1)
#     returning = call_stack.pop()
#     print("Виходимо з:", returning)
#     time.sleep(0.3)

# stack_call = CallStack()
# simulate_recursion(stack_call, "Factorial", 3)


# ЗАВДАННЯ 4
# Уявімо модель, де кожен виняток (error) записується
# у стек, якщо у нас “ланцюжок винятків”.
# Після завершення обробки ми знімаємо помилки зверху.

# class Error:
#     def __init__(self, code, message):
#         self.code = code
#         self.message = message

#     def __str__(self):
#         return f"Error {self.code}: {self.message}"

# class ErrorStack:
#     def __init__(self):
#         self.errors = []

#     def push(self, err):
#         ...

#     def pop(self):
#         ...

#     def peek(self):
#         ...

#     def is_empty(self):
#         return len(self.errors) == 0

# err_stack = ErrorStack()
# err_stack.push(Error(404, "Not Found"))
# err_stack.push(Error(500, "Server Error"))
# print("Верхня помилка:", err_stack.peek())
# popped_err = err_stack.pop()
# print("Зняли помилку:", popped_err)
# print("Залишилася помилка:", err_stack.peek())