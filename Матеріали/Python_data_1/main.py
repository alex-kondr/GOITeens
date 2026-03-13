import numpy as np


# array = np.arange(1000000)

# print(array.sum())

# array = [[j for j in range(i, i+3)] for i in range(1, 10, 3)]
# print(array)

# matrix = np.array(array)
# print(matrix.T)

# from sklearn.linear_model import LinearRegression


# X = np.array([[1], [2], [3], [4], [5]])
# y = np.array([2, 4, 6, 8, 10])

# model = LinearRegression()
# model.fit(X, y)

# prediction = model.predict(np.array([[7]]))
# print("Прогноз для 6:", prediction)


# from PIL import Image

# image = Image.open('image.jpg')
# image_array = np.array(image)

# brightened = image_array + 50
# brightened = np.clip(brightened, 0, 255)

# brightened_image = Image.fromarray(brightened.astype('uint8'))
# brightened_image.save('brightened_image.png')


# zeros_array = np.zeros(5)
# ones_tensor = np.ones((2, 3, 4), dtype=float)
# range_step_array = np.arange(0, 20, 2)
# linspace_array = np.linspace(0, 1, 5)

# Використовуючи функцію array(), створіть масив з наступного списку: [10, 20, 30, 40, 50].
# За допомогою функції zeros() створіть двовимірний масив розміру 2x3, заповнений нулями.
# Використовуючи функцію ones(), створіть тривимірний масив розміру 2x2x2, заповнений одиницями.
# Створіть масив з чисел від 5 до 15 з кроком 1 за допомогою функції arange().
# За допомогою функції linspace() створіть масив з 8 чисел, рівномірно розподілених між 0 та 2π (приблизно 6.283).

# flat_array = np.arange(12)
# reshaped_array = flat_array.reshape((3, 2, 2))
# print(reshaped_array)

# np.mean - Середнє значення
# np.median - Медіана
# np.std - Стандартне відхилення
# np.prod - добуток


# matrix = [
#     [2, 4, 6],
#     [8, 10, 12],
#     [14, 16, 18]
# ]
# Перетворіть цей список у масив NumPy та обчисліть суму всіх елементів матриці. Виведіть результат.


# two_d_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# two_d_array = np.array(two_d_data)
# array = two_d_array.reshape((1, 3, 3))
# ones = np.ones((1, 1, 3), dtype=float)
# print(np.concatenate((array, ones), axis=1))


# Створіть масив NumPy з числами [1, 2, 3, 4, 5] типу int64. Потім перетворіть цей масив у тип float32 та обчисліть суму елементів нового масиву.
# array_int64 = np.array([1, 2, 3, 4, 5], dtype=np.int64)
# array_float32 = array_int64.astype(np.float32)


# Створіть масив NumPy з булевими значеннями [True, False, True, False, True] типу bool. Виведіть масив та його тип даних.
# bool_array = np.array([....], dtype=...)
# print(bool_array)
# print(bool_array.dtype)


# Створіть масив NumPy з числами [2, 4, 6, 8, 10] типу int32. Перетворіть цей масив у тип complex64 та виведіть новий масив та його тип даних

# Створіть два масиви NumPy з числами від 0 до 9999. Перший масив має тип int64, а другий — int16. Порівняйте обсяг пам'яті, який займає кожен масив.
# large_int64 = np....(...)
# print(large_int64.nbytes)


# Створіть два масиви NumPy з 1,000,000 випадкових чисел типу float64 та float32. Обчисліть суму елементів кожного масиву та порівняйте час виконання.


# Створіть масив NumPy з числами від 1 до 1000 типу int32.
# Перетворіть цей масив у тип float32, а потім створіть новий масив,
# де кожен елемент дорівнює квадрату відповідного елемента перетвореного масиву. Обчисліть суму всіх елементів нового масиву.


# Створіть масив NumPy з числами [5, 10, 15, 20, 25] типу int16. Перевірте його тип даних та розмір масиву.
# array_int16 = ....
# print(array_int16)
# print(array_int16.dtype)
# print(array_int16.shape)


# Створіть масив NumPy з числами [2.2, 4.4, 6.6, 8.8] типу float64. Перетворіть його у тип int32 та обчисліть середнє значення нового масиву.


# Основні операції з масивами
# 1. Елементне додавання масивів
# 2. Елементне множення масивів

# Індексація окремого елемента
# matrix = np.array([[1, 2, 3],
#                    [4, 5, 6],
#                    [7, 8, 9]])
# element = matrix[1, 2]

# Зріз рядка
# row = matrix[0, :]
# Зріз стовпця
# column = matrix[:, 1]
# Зріз підмасиву
# sub_matrix = matrix[0:2, 1:3]

# Зміна форми масиву за допомогою reshape(): [[ 1 2 3 4 5 6 7 8 9 ]] (1, 9)
# Перетворення масиву у одновимірний за допомогою flatten(): [ 1 2 3 4 5 6 7 8 9 ] (9,)

# matrix = np.array([[1, 2], [3, 4]])
# reshaped = matrix.reshape(4)
# print(reshaped)

# Створіть двовимірний масив NumPy з числами від 1 до 9 розміром 3x3. Отримайте елемент на позиції рядка 2 та стовпця 3.

# Використовуючи створений масив matrix, отримайте перший рядок та другий стовпець.
# matrix = np.array([[4, 2, 4],
#                    [4, 2, 6],
#                    [3, 8, 1]])

# Створимо одновимірний масив з числами. Змінимо його форму на 2x3.
# array = np.array([1, 2, 3, 4, 5, 6])

# Використовуючи масив reshaped_array з попереднього завдання, перетворіть його у одновимірний масив.
# reshaped_array = np.array([[4, 3, 3], [4, 1, 615]])
# flattened_array = reshaped_array.flatten()
# print(flattened_array)


# Створіть масив NumPy з числами [2.2, 4.4, 6.6, 8.8] типу float64.
# Перетворіть його у тип int32 та обчисліть середнє значення нового масиву.


# Створіть масив NumPy з числами від 1 до 1000 типу int32.
# Перетворіть цей масив у тип float32, а потім створіть новий масив, де кожен елемент
# дорівнює квадрату відповідного елемента перетвореного масиву. Обчисліть суму всіх елементів нового масиву.