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

# np.mean
# np.median
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