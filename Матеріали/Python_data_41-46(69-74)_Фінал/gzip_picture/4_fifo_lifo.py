class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def size(self):
        return len(self.items)


class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        else:
            return None

    def size(self):
        return len(self.data)

    def is_empty(self):
        return self.size() == 0

    def peek(self):
        if not self.is_empty():
            return self.data[-1]
        else:
            return None


# Пузиркове сортування (Bubble Sort)
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return arr


# Сортування вибором (Selection Sort)
def selection_sort(arr):
    for i in range(len(arr)):
        min_value = i
        for j in range(i, len(arr)):
            if arr[min_value] > arr[j]:
                min_value = j
        if min_value != i:
            arr[min_value], arr[i] = arr[i], arr[min_value]
    return arr


# Сортування вставками (Insertion Sort)
def insection_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr


# Швидке сортування (Quick Sort)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left_arr = [x for x in arr if x < pivot]
    middle_arr = [x for x in arr if x == pivot]
    right_arr = [x for x in arr if x > pivot]
    return quick_sort(left_arr) + middle_arr + quick_sort(right_arr)


# Сортування злиттям (Merge Sort)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        merge_sort(left_arr)
        merge_sort(right_arr)
        i = j = k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

    return arr