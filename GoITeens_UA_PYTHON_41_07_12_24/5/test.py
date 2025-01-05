# Організувати безперервне введення з клавіатури чисел.
# Якщо число більше 20, то вивести його на екран.
# Якщо число більше 100 — закінчити роботу програми.






# while True:
#     number = input("Введіть ціле число ")
#     number = int(number)
    
#     if number > 100:
#         print("роботу програми завершенно")
#         break
#     elif number > 20:
#         print(number)



# while True:
#     number = int(input("Введіть ваше число"))
    
#     if number > 100:
#         print("Ви завершили програму")
#         break

#     elif number > 20:
#         print(f"Ви обрали число {number}")

# sum_e_num = 0
# for number in range(0, 101, 2):
#     sum_e_num += number
# print(f"сума всіх парних чисел від 1 до 100 дорівнює {sum_e_num}")




# while True:
#  number = int(input('Ведите число '))
# if number > 100:
#    print ('число больше 100')
#    break
#  elif number > 20:
#     print(f'вы выбрали число: {number}')  

# while True:
#     try:                                 
#         number = float(input("Введіть число: "))
#         if number > 100:
#             print("Число більше 100. Завершення роботи програми.")
#             break
#         elif number > 20:
#             print(f"Число більше 20: {number}")
#     except ValueError:
#         print("Будь ласка, введіть коректне число.")

# while True:
#     number = int(input("Введіть число: "))
#     if number > 20:
#         print(number)
#     if number > 100:
#         print("Процес завершено")
#         break
        




# Написати програму, яка буде підраховувати суму всіх парних чисел від 1 до 100.

sum_even = 0

for number in range(1, 101):
    if number % 2 == 0:
        sum_even += number

print(f"Сума всіх парних чисел від 1 до 100 дорівнює {sum_even}")



sum_e_num = 0
for number in range(0, 101, 2):
    sum_e_num += number
print(f"сума всіх парних чисел від 1 до 100 дорівнює {sum_e_num}")



# Написати програму, яка приймає на вхід рядок, введений з клавіатури, ---------------2
# і підраховує кількість входження в рядок останньої літери,
# якою закінчується цей рядок.

# Дано ціле число, що лежить у діапазоні 1-999.
# Вивести рядок-опис виду «парне двозначне число», «непарне тризначне число» тощо.