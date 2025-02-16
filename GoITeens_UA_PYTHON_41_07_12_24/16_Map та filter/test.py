# numbers = [1, 5, 6, 7, 10, 11, 87, 102]



# numbers = [1, 5, 6, 7, 10, 11, 87, 102]

# filtered_numbers = list(filter(lambda number: number % 2 != 0, numbers))


# def filtered(number):
#     return number % 2 != 0

# filtered_numbers = [number for number in numbers if number % 2 != 0]
# print(filtered_numbers)


# products = ["Table", "CHAIR", "Desk", "SHELF"]

# products = ["Table", "CHAIR", "Desk", "SHELF"]
# lowercase_products = list(map(lambda x: x.lower(), products))
# print(lowercase_products)


# lower_str = [product.lower() for product in products ]

# print(lower_str)


# numbers = [34, -2, 0, 39, -8, 42, -99]
# plus_numbers = [number for number in numbers if number > 0]
# print(plus_numbers)

# filter_numbers = list(filter(lambda x: x > 0, numbers))
# print(filter_numbers)

# string_numbers = ["4", "11", "-20", "39", "0"]
# int_numbers = [int(number) for number in string_numbers]
# print(int_numbers)

# numbers = ["4", "11", "-20", "39", "0"]
# numbers_str = list(map(lambda x: int(x), string_numbers))
# print(numbers_str)


# Написати функцію, яка приймає два числа та повертає їх суму.

numbs = input("Введіть два числа через пробіл > ").split()
numbs = list(map(lambda x: float(x), numbs))
numbs = [float(numb) for numb in numbs]


def plus_numbers(*a):
    return sum(a)

print(plus_numbers(*numbs))


