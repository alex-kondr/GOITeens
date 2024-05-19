# Дано діапазон чисел від -100 до 0. Вивести на екран лише числа, які закінчуються на нуль
numbers_ends_zero = [number for number in range (-100, 1) if number % 10 == 0]
print(numbers_ends_zero)
