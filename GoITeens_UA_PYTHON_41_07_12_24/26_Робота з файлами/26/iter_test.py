
# my_iter = iter(my_list)
# print(my_iter)

# first_number = next(my_iter)
# print(first_number)
# next(my_iter)
# next(my_iter)
# number = next(my_iter)
# print(number)

# for number in my_iter:
#     print(number)

# for number in my_list:
#     print(number)

# string = "Hello world!"

# my_iterator = iter(string)
# next(my_iterator)
# next(my_iterator)
# next(my_iterator)
# next(my_iterator)
# next(my_iterator)
# next(my_iterator)

# char = next(my_iterator)
# print(char)








# from itertools import cycle, count, repeat, accumulate, chain, zip_longest, dropwhile, takewhile, filterfalse

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# my_iter = filterfalse(lambda x: x < 5, my_list)

# for number in my_iter:
#     print(number)

# numbers = count(1)

# filter_numbers = takewhile(lambda x: x <= 50, numbers)

# new_list = [number ** 2 for number in filter_numbers]
# print(new_list)
# odd = filterfalse(lambda x: x % 2 != 0, my_list)
# for number in odd:
#     print(number)

# my_iter = accumulate(my_list)

# for number in my_iter:
#     print(number)
#     input()

# my_iter = count(10, 10)

# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))

# for number in my_iter:
#     print(number)


from itertools import count, filterfalse

counter = count(10, 10)
numbers = []
for number in counter:
    numbers.append(number)
    if number > 201:
        break

numbers = [str(number)+"\n" for number in numbers]

with open("numbers.txt", "w") as file:
    file.writelines(numbers)