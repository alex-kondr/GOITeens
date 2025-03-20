my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# iterator = iter(my_list)
# print(next(iterator))
# next(iterator)
# next(iterator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

from itertools import cycle, count, repeat, accumulate, chain, zip_longest, dropwhile, takewhile, filterfalse
# Using itertools.cycle to cycle through a list
# cycled_list = cycle(my_list)
# for _ in range(15):  # Print 15 elements from the cycled list
#     print(next(cycled_list))

# Using itertools.count to generate a sequence of numbers
# for number in count(start=11, step=2):  # Start from 11, increment by 2
#     if number > 25:  # Stop when the number exceeds 25
#         break
#     print(number)

# Using itertools.repeat to repeat a value
# repeated_value = repeat('Python', times=5)
# for value in repeated_value:
#     print(value)

# Using itertools.accumulate to calculate the running total
# accumulated_values = accumulate(my_list)    # By default, accumulate calculates the running total
# for value in accumulated_values:
#     print(value)    # Print the running total

# Using itertools.chain to chain multiple iterables
# chain_list = chain([1, 2, 3], [4, 5, 6], [7, 8, 9]) # Chain multiple lists together
# print(chain_list)
# for value in chain_list:
#     print(value)    # Print the chained

# Using itertools.zip_longest to zip multiple iterables
# zipped_list = zip_longest([1, 2, 3], [4, 5, 6, 7], fillvalue='N/A')  # Zip multiple lists together
# for value in zipped_list:
#     print(value)    # Print the zipped lists

# Using itertools.dropwhile to drop elements from the iterable
# dropped_values = takewhile(lambda x: x % 2 != 0, my_list)  # Drop elements from the iterable until the condition is false
# for value in dropped_values:
#     print(value)    # Print the

# Using itertools.takewhile to take elements from the iterable
# taken_values = takewhile(lambda x: x % 2 != 0, my_list)  # Take elements from the iterable until the condition is false
# for value in taken_values:
#     print(value)    # Print the

# Using itertools.filterfalse to filter elements from the iterable
# filtered_values = filterfalse(lambda x: x % 2 != 0, my_list)  # Filter elements from the iterable
# for value in filtered_values:
#     print(value)    # Print the filtered values